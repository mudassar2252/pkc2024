import streamlit as st
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Random Forest Classifier App
## Made by Mudassar Murtaza
This app pridicts the type of iris based on spal length sepal width, petal length and petal width.
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Iris Parameters')
st.write(df)
iris = sns.load_dataset('iris')

st.subheader('Plotly Plots')
fig = px.bar(iris, x='species', y='petal_length',color = 'species')
st.plotly_chart(fig)

st.subheader('Box Plot')
fig1 = px.box(iris,x='species', y= 'petal_length',color= 'species')
st.plotly_chart(fig1)

st.subheader('GDP Plot, Animated')
df2 = px.data.gapminder()
fig2 =px.scatter(df2, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
st.plotly_chart(fig2)

st.subheader('3D Scatter Plot')
fig3 = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_length', color='species')
st.plotly_chart(fig3)



st.subheader('Iris Dataset')
st.write(iris)
X = iris[['sepal_length','sepal_width','petal_length','petal_width']]
y = iris['species']



model = RandomForestClassifier()
model.fit(X,y)
prediction = model.predict(df)
prediction_proba = model.predict_proba(df)
st.subheader('Class Labels and their corresponding index number')
st.write(iris['species'].unique())

st.subheader('Prediction')
p = st.write(prediction[0])
st.write(p)
st.subheader('Prediction Probability')
st.write(prediction_proba) 
