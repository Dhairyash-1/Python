# Variables
# while writing variable name in python we use snake case convention
# example:- first_name, country , year_2023, num1, capital_city

name = 'dhairyash'
age = 19
is_graduate = False
print(name)
print(age)
print(is_graduate)

#  we can declare multiple variables in one line

first_name,last_name,age = 'dhairya','gupta',19
print(first_name,last_name,age)


# ###### Data Casting
# converting one data type to other we use
# float() ,int(),str(), list()

# str to list

country = 'Indiaa'
str_to_list_of_country = list(country)
print(str_to_list_of_country)
# str to set
print(set(country)) # avoid repeated small a