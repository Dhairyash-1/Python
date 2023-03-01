# A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple
# Creating a Tuple


# Creating a tuple

# tuple = ()
# or using tuple constructor
# empty_tuple = tuple('a')

tp1 = ('item1','item2','item3','item3') # duplicate allow in tuple
print(tp1)

print(len(tp1))

# Accessing tuples items using +ve and -ve indexing

first_item = tp1[0]
last_item = tp1[-1]
print(first_item)
print(last_item)


# Slicing tuples
# ----range of positive index
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]
middle_two_items = tpl[1:3]
print(all_items,middle_two_items)
# ----range of negative index

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
last_two_fruits = fruits[-2:]
print(all_fruits,last_two_fruits)


# Changing tuples to List or list to tuples

tpl = ('item1','item2','item3','item4')
lst = list(tpl)
print(lst)
fruits_list = ['mango','orange','grapes']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# checking item in tuples

print('item2' in tpl)
print('item6' in tpl)

# Joining tuple

tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)

# Deleting tuples

fruits = ('apple','mango','orange')
del fruits
# print(fruits)  throw error because fruits tuple deleted
