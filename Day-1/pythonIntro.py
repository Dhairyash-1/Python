############################### comments in Python
# This is signle line comment
# Multiline comment :- """using triple quote ""

"""In python this is 
a multiline comment"""


############# Data Types in Python ##########

# 1. Number
# integer :- positive negative and zero number
# float :- decimal number negative also -3.3,2.0,23.23
# Complex number:- 1+j, 2+4j

# 2. Strings

# A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.
# example:-
'dhairyash'
'python'
"Learning"
""""more than
one sentence
"""

# 3. Booleans
True, False

# 4. List

# list allow to store different data type value in order collection like array in JS

numbers = [1,2,3,4,5,6]
fruits = ['apple',True,2,0.3,1+2j]

# 5. tuples

# A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

tuple = ('earth','moon',1,True)

# 6. Dictionary

# dictionary is an object an unordered collection of data in key value pair format

python_dictionary = {
    'first_name':'dhairyash',
    'last_name':'gupta',
    'age':19,
    'isMarried':False,
    'skills':['HTML','CSS','JAVASCRIPT','REACT','PYTHON'],
    'tuple':('india','usa','germany')
}

# 7. Sets

# set in python is collection of data type simliar to list and tuple. unlike list and tuple set is not a ordered collection of items,like in maths it stores only unique value no duplicates allowed

set = {9,23,423,22} # order is not imp in sets
set2 = {23,23,2,85,75} # duplicate number will be ignore in sets

######################################
# Checking data types in python using type() funcion 

print(type(2)) # class 'int'
print(type(-2.3)) # class 'float'
print(type(2-3J)) # class 'complex'
print(type('string')) # class 'str'
print(type("dhairyash")) # class 'str'
print(type(True)) # class 'bool'
print(type(['apple',True,2,0.3,1+2j]))
print(type(('earth','moon',1,True)))
print(type(set),set)
print(type(set2),set2)
print(type(python_dictionary))
