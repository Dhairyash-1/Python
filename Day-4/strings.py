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

# ### Skipping character while slicing
# [startIndex:lastIndex:step] step means if step 2 so will be 0,2,4,6 charcter shown

print(programming[0:6:2]) # charc at 0,2,4 shown step is 2
print(programming[0:6:3]) # char at 0,3,6 shown step is 3


########################### String Methods ############
##################

# 1. capitalize() : convert first char of string to capital

challange = 'thirty days of python'
print(challange.capitalize())

# 2. count() : returns the occurens of substring in string 
# count(substring,startIn,lastInd)

print(challange.count('y')) # how many times 'y' occur in string
print(challange.count('y',7,14))  # occurence of y between index 7 to 14

# 3. endswith() : check if string end with specified ending
print(challange.endswith('on'))
print(challange.endswith('one'))
print(challange.endswith('python'))

# 4. expandtabs() : replace tab char with spaces, default tab size is 8 it take tab size argument
challanges = 'thirty\tdays\tof\tpython'
print(challanges.expandtabs())
print(challanges.expandtabs(20))

# 5. find(): Returns the index of the first occurrence of a substring, if not found returns -1

challange = 'thirty days of python'
print(challange.find('y'))
print(challange.find('th'))
print(challange.find('the'))

#  rfind() :- return last occurence of substring in string
print(challange.rfind('th'))
print(challange.rfind('y'))

# 6. index() : it return lowest index of substirng,additional argument indicate start and last index if substring not found valueerror

print(challange.index('py'))
print(challange.index('da'))
print(challange.index('y',6,10))

# rindex() return higest index substring
print(challange.rindex('y'))

# 7. isalnum() : check alphanumeric char
# isalpha() : check if string elem are alphabet char a-z and A-Z
string = 'days'
print(string.isalnum())
string = 'days23'
print(string.isalnum())
string = 'days of ' # spaces and special char are not alphanumeric
print(string.isalnum())

alpha = 'thirtyDays'
print(alpha.isalpha())
alpha1 = 'thirty Days' # space is not alpha
print(alpha1.isalpha())
alpha2 = '30Days'
print(alpha2.isalpha())

# 8. isdecimal() : check for all char between (0-9)
# isdigit() : check of all char string are numbers (0-9) and other unicode char
print('######')
testnum = 'Thirty'
print(testnum.isdecimal())
testnum = '30'
print(testnum.isdecimal())
testnum = '\u00B2'
print(testnum.isdecimal()) 

# isdigit : check for number as well as unicode
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True


# isnumric() : same as isdigit  just accetpt more symbole like 1/2
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

# 9. isidentifier() : check for vaild variable name
print(' ####identifier result ######')
variable_test = '30daysofpython'
print(variable_test.isidentifier())
variable_test = 'days_of_python'
print(variable_test.isidentifier())

# 10. islower() : check if all char are lowercase
# isupper() : check if all char are uppercase
challange = '30 days of python'
print(challange.islower())
print(challange.isupper())
challange = '30 DAYS OF PYTHON'
print(challange.islower())
print(challange.isupper())

# 11. join() : return a concatenated string
# replace('substring','newstring')

web_tech = ['HTML','CSS','JavaScript','React']
print(' '.join(web_tech))
print('# '.join(web_tech))

challange = '30 days of python'
print(challange.replace('python','JavaScript'))

# 12. strip(): Removes all given characters starting from the beginning and end of the string

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

# 13. split(): Splits the string, using given string or space as a separator

print(challange.split())
print(challange.split(', '))

# 14. title() : return title case string
challenge = 'thirty days of python hai'
print(challenge.title()) # Thirty Days Of Python Hai

# 15.swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# 16. startswith() check if string start with specified  string

challange = 'thirty days of python'
print(challange.startswith('thirty'))

challange = '30 days of python'
print(challange.startswith('thirty'))