richest_country = 'USA'
richest_person = '''Elon Musk'''
net_worth = "220 Billion dollar"

string_concatenation = richest_country + ' is richest country and '+ richest_person + ' is richest person with '+net_worth 
print(string_concatenation)

# Escape sequence in strings
# \\ for write \
# \' for single quote (')
# \n for new line
# \t for tab means 8 spaces

print('This is a blackslash symbol \\')
print('This is a forwardslash symbol /')
print('you don\'t know anything')
print('my name is dhairyash \nI live in Mumbai India')
print('tab space in python tab\t3\tspace')


# Old string formattin in python
# %s for string
# %d for integers
# %f for float number

# #### Only string formating
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'

formated_string = 'I %s %s and I teach %s'%(first_name,last_name,language)
print(formated_string)

# #### Only string  and number formating


age = 45
CGPA = 9.97

formated_string_number = "I %s %s and I teach %s. my age is %d college cgpa is %.2f "%(first_name,last_name,language,age,CGPA) # .2f for 2 significant digit
print(formated_string_number)

python_library = ['Django','Flask','Numpy','Pandas']
string_formated = 'The following are python libraries: %s'%(python_library)
print(string_formated)

# ### New String formating method in Python 3

new_formated_string = 'I am {} {}. I teach {}'.format(first_name,last_name,language)
print(new_formated_string)

a= 3
b = 4
print('{} + {} = {}'.format(a,b,a+b))
print('{} / {} = {:.3f}'.format(a,b,a /b)) 

# ### String Interpolation/ f-strings

print(f'{a} + {b} = {a+b}')
print(f'{a} ** {b} = {a**b}')
print(f'{a} / {b} = {a / b:.2f}')

# ### Unpacking strings characters
programming = 'Python'
b,c,d,e,f,g = programming
print(b,c,d,e)

# ### Acessing String characters by index

first_letter = programming[0]
print(first_letter)
last_letter = programming[-1]
print(last_letter)


# ### Slicing Python strings
# slice strings into substrings

first_three = programming[0:2] # str.[start index: end index] it not include chart at index 2
print(first_three)
last_three = programming[3:6]
print(last_three) # hon

# Another way of same thing
last_threes = programming[-3:] # start from -3 to end -1
print(last_threes) #hon

last_threess = programming[3:]
print(last_threess)


# ### Reverse string
greeting = 'Hello, World'
print(greeting[::-1])
