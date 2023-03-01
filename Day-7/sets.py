# In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
# creating empty sets
set_in_python = {}
# or
set_in_python = set()

# with inital value
fruits_set = {'banana','apple','mango','kiwi'}

# Getting sets length
print(len(fruits_set))

# ####################################################
# -------------------Accessing items in a Set------------
# we use loop to access item in set in loop section

# ############################
# ---------------- Checking an item--------------------
print('does fruits set contain apple:-','apple' in fruits_set)

# Adding item in set using add()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

#  add multiple item using update()
fruits.update(['kiwi','berri'])
print(fruits)

# remove items from set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print('using reomove',st)

# remove using pop() , it reomve random item and return that item
print(st.pop())

# clearing items from set or empty the set
st.clear()
print('item clear',st)

# if we want to delete the set

sample_set = ('item1','item2','item3')
del sample_set
# print(sample_set)

# ------Converting the List to Set--------------
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
print(st)

# -------------------Joining the sets--------------
#  we can use union() or update() to join set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

#  we can also join using update() method
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
print(st1)

##################################3
#-----------------Finding Intersection Items-------------
# Intersection returns a set of items which are in both the sets. See the example

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
result =whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(result)

# #############################################33
#----------------Checking Subset and Super Set---------
# A set can be a subset or super set of other sets:
# Subset: issubset()
# Super set: issuperset

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

########################################
# Checking the Difference Between Two Sets
# It returns the difference between two sets.

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}


# --------------Finding Symmetric Difference Between Two Sets-----------

# It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

whole_num = {'0','1','2','3','4','5','6','7'}
some_num = {'2','3','4','6'}
symdiff =whole_num.symmetric_difference(some_num)
print('symdiff',symdiff)

# ------------------------------------------------------
# Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.

even_num = {0,2,4,6,8}
odd_num = {1,3,5,7}
isdisjointset = even_num.isdisjoint(odd_num)  # True because both are different
print('isdisjoint',isdisjointset)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}


string = 'I am a teacher and I love to inspire and teach people. '
split = string.split()
print(split,'lenght:-',len(split))
unique_word = set(split)
print(unique_word,'length:-',len(unique_word))