import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Load Titanic dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Generate Profile Report
profile = ProfileReport(df, title="Titanic Dataset Report", explorative=True)

# Streamlit app
st.title("Titanic Dataset Profiling")
st.write("## Exploratory Data Analysis")
st_profile_report(profile)
