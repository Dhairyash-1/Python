# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

person = {
    'name':'dhairyash',
    'surname':'gupta',
    'age':19,
    'isGraduate':False,
    'skills':['HTML','CSS','JS','REACT','TAILWIND'],
    'address':{
    'street':'space street',
    'zipcode':29232,
    }
}
print(person)
# Dictinary length :tell the number of key value pairs in person dictionary

print(len(person))

# ----------- Accessing dictionary item---------
#  we can access item using its key nam;e

print(person['name'])
print(person['skills'][-1])
print(person['address']['street'])
print(person['isGraduate'])

# to access key first it exist in dict if not exist the raise error
# to check first exist and get use get method
# if not exist any key then return empty object

print(person.get('name'))
print(person.get('skills'))
print(person.get('city'))


# Adding item to a dictinary
#  we can add new key and value pair to dictionary

person['city'] = 'Mumbai'
person['skills'].append('python')
print(person)

# Modifying item in dictionary 
person['name']= 'Robin'
person['skills'][2]='JAVASCRIPT'
print(person)

# Checking keys exist in dict 
#  we use in operator

print('skills' in person)
print('country' in person)

# ----------------------------------------------------
# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

print(person.pop('surname'))
print(person.popitem())
print("update after popitem",person)

del person['isGraduate'] # removes this key and its value
print("update after del",person)

# Changing Dictionary to a List of Items

# syntax
dct = {
   'key1':'value1',
   'key2':'value2',
   'key3':'value3',
   'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# clear items of dictinary
print('clear dct',dct.clear())
# delete dct completely
del dct

# Copy a dictinary 
person_copy = person.copy()
print('copy ver person',person_copy)

print('-------------------------------------')
# we can get items of dictionary like key and value as a list

keys = person_copy.keys()
values = person_copy.values()
print('keys',keys)
print('values',values)
