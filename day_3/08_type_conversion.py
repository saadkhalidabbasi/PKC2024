x=10            #integer
y=10.2          #float
z='hello world'  #string
print(type(x))
print(type(y))
print(type(z))

y=x*y
print(y)
print(type(y))
# implicit type conversion 
x=x+y
print(x)
print(x,'Type of x is :' , type(x))


# explicit type conversion 
age=input('What is your age ')
print(age,type(age))
print(age,type(int(age)))