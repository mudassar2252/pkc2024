x=10              #integer
y=10.4              #float
z="Hello"       #string

print(type(z))
# if a integer is multiplied with a float number then the result will be a float number
# when a integer is added to a float number then the result will be a float number

# there are two types of conversion 
# 1)   implicit type conversion
# 2)   explicit type conversion
# implicit type conversion
# this is type of conversion which converts automatically from one data type to another data type
# example of implicit type conversion is as follows
x=10
y=20.4
print(type(x+y))
# from above example we can see that implicit conversion convert integer to a float number 

# explicit type conversion
# this is type of conversion which converts manually from one data type to another data type
# in this we have to convert manually from one datatype to another datatype 
# example of explicit type conversion is as follows
# int() functon is used to convert a number to a integers 
# float() function is used to convert a number to a float umber 
#str() function is used to convert a number to a string 
age="18"
y=int(age)

print(type(y))
# we can see from aboveexample in this class of age was string we put int function and now  it's converted to integer  type  and it's value is 18

x=10.4
z=int(x)
print(type(z))

a=10
b=float(a)
print(type(b))

# another example is that 
name=input("What is your name?")
print(name, type(str(name)))
