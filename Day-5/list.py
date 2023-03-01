# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.

lst = list() #empty list 
print(lst)

fruits = ['banana','orange','mango','lemon','lime','apple']
print(fruits)
print("Number of fruits",len(fruits))

print(fruits[0]) #first item
print(fruits[-1]) #last item

# Unpacking list items
# ex1
first_fruit,second_fruit,third_fruit,*rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

# ex2
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr,fr,be,*scandic,ice,es = countries
print(gr)
print(fr)
print(be)
print(scandic)
print(ice)
print(es)

#### Slicing items from list

# Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
print(all_fruits)
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(all_fruits)
orange_and_mango = fruits[1:3] # it does not include the first index
print(orange_and_mango)
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)
banana_and_mango = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
print(banana_and_mango)

# Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']


####### Modifying Lists
# List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

##### Checking Items in a List
# Checking an item if it is a member of a list using in operator. See the example below.
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# ###############################
# Adding items to a list

# To add item to the end of an existing list we use the method append().

list = ['item1','item2']
list.append('item3')
print(list)

####### Inserting Items into a List
# We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.
lst = ['item1','item2']
lst.insert(3,'item3')  # it update the existing list

# Removing item from list

lst = ['a','b','c']
lst.remove('b')
print(lst)

# Remove item using pop() default remove last item or we can pass index of item

lst = ['html','css','js','react']
lst.pop()  
print(lst)  # remove last item react
lst.pop(0)  
print(lst)  # remove index 0 item

# Remove item using Del

lst = ['a','b','c']
del lst[1] # delete index 1 item
print(lst)
del lst  # delete list completely give error 

# clearing list items
lst = ['banan','orange','mango']
lst.clear()
print(lst)


# #################################################
#-------------------Copying a List-------------------
# we can copy list by reassigning it to new var like list2 = list1 now list2 is reference of list1
# any changes we make in list1 affect list2 but don't want to do it
# here come in use : copy()
fruits = ['kiwi','grapes','blueberries']
fruits_copy = fruits.copy()
print(fruits_copy)


# ####################################################
#---------------Joining the list---------------------
# two ways one is plus opeartor other one is extend()

positive_numbers = [1,2,3,4,5]
negative_numbers = [-1,-2,-3,-4,-5]
zero = [0]
integers = negative_numbers + zero + positive_numbers
print(integers)

# 2nd way:- extend()
# it allow to append other list in existing one no need to create new list

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('negaitve numbers',negative_numbers)

# count item in list using count()
# it returns nukmber of times an item appear in list
fruits = ['mango','apple','kiwi','grapes','apple','mango','mango']
print(fruits.count('mango'))
print(fruits.count('kiwi'))
print(fruits.count('apple'))

# index() 
# return the index of give item
print('index of kiwi',fruits.index('kiwi'))
print('index of apple',fruits.index('apple')) # first occurence

############################################
#---------------Reversing item in list-------------
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)
# sort items in the list and sorts string in alphabetical order
ages.sort()  # it gives in ascending order
print('ascending',ages)
ages.sort(reverse=True)  # it gives in ascending order
print('descending',ages)

# ########################################
# sorted() :- it returns the orderd list without modifying orignal list
fruits = ['banana', 'orange', 'mango', 'lemon']
print('new sorted list',sorted(fruits)) # ascending
print('new sorted list',sorted(fruits, reverse=True)) # descending


