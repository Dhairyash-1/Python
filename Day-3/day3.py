############################# Operators ###################################

# 1. Assignment operator

# assignment operator used to assign a value in python
# = , += . -=. *= , /=

# 2. Arithmetic operators
# addition,subtraction,multiply,divide,modulus,floor division , exponent **

# 3. Comparison operators
# equal = , less than < ,greaer than > , not equal != ,<=,>=

#  comparing something gives true or false value in python

# print(2<3)
# print(22>3)
# print(22==3)
# print(22==22)
# print(22!=922)

# print(len('mango') == len('avocado'))  # False
# print(len('mango') != len('avocado'))  # True
# print(len('mango') < len('avocado'))   # True
# print(len('milk') != len('meat'))      # False
# print(len('milk') == len('meat'))      # True
# print(len('tomato') == len('potato'))  # True
# print(len('python') > len('dragon'))   # False

#  In addition python also use 

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

print('ram' is 'ram')
print('ram' is 'rama')
print(2 is 3)
print(2 is 2)
print( 83 is not 2) # True

print('i' in 'dhairyash')
print('A' in 'dhairyash')

print( 'm' not in 'ram')
print( 'm' not in 'raM')


#  Logical operators

#  and : -  if both are true than return true otherwise false
#  or :- if any one in both is true than true if all true than also true if all false than only false
#  not :- it reverse the result True to False, False to True

print('Logical operators')
print(4<2 and 2>1) # false because one is false
print(0.4<2 and 2>1)

print(4<2 or 2>1) # true because one is false
print(0.4<2 or 2>1)
print(4<2 or 2>11)

print(not True)
print(not False)

print(not 5>55)
print(not 554>55)