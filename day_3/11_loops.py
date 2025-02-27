# there are two types of loops 
# while loop and for loop
# in while loop we have to enter the value so that it stop else it's infinity 

# x=0
# while (x<5):
#     print(x)
#     x=x+1


 #for loop is used when we know the number of times we want to execute the loop
for x in range(4,11):
    # print(x)

    # array  like we design a  dataset further  we'll discuss it i detail after 
    days = ["mon", "tue", "wed", "thru", "fri", "sat", "sun"]
    for d in days:
        # if (d=="fri"): break    # break is used to stop the loop
        if (d=="fri"): continue   # skipped fri
        print(d)  # it will print each day of the week  

