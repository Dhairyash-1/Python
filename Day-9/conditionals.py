# If else condition in python
a=-5
if a>0:
    print('It is positive number')
else:
    print('it is negative number')

# If ellif in python for multiple condition

age = int(input('Enter your age:- '))
if age<18:
    print('You have no driving license can\'t drive')
elif age>60:
    print('You are too old ')
else:
    print('You can drive')

# short hand

b = 3
# print(type(b))
print('b is positive') if b>=0 else print('b is negative')

# nested if else

a = 4

if a>0:
    if a%2==0:
        print('a is positive and even')
elif a ==0:
    print('a is zero')
else:
    print('a is negative number')


#  we can avoid nested condition using logical operator

#  and logical operator when both true then only run

a=5
if a>0 and a%2==0:
    print('a is positive and even')
elif a>0 and a%2!=0:
    print('a is positive and odd')
elif a==0:
    print('a is zero')
else:
    print('a is negative')


# Or logical operataor

user = 'james'
access_level = 3

if user =='admin' or access_level>=4:
    print('acess is granted')
else:
    print('access is denied')