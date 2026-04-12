# def decorator_with_parameters(function):
#     def wrapper_accepting_parameters(para1, para2, para3):
#         function(para1, para2, para3)
#         print("I live in {}".format(para3))
#     return wrapper_accepting_parameters

# @decorator_with_parameters
# def print_full_name(first_name, last_name, country):
#     print("I am {} {}. I love to teach.".format(
#         first_name, last_name))

# print_full_name("Asabeneh", "Yetayeh",'Finland')

# map,filter

# import string
# num = [i for i in range(len(string.digits))]
# print(num)

# square_num = map(lambda x: x**2,num)
# print(list(square_num))

# def is_even_num(num: int):
#     if num%2 == 0:
#         return True
#     else:
#         return False
    
# even_num = filter(is_even_num,num)
# print(list(even_num))

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # for name in countries:
# #     print(name)
# # for name in names:
# #     print(name)
# # for name in (numbers):
# #     print(name)

# upper_country = map(lambda x: x.upper(),countries)
# print(list(upper_country))

# square_num = map(lambda x: x**2,numbers)
# print(list(square_num))

# upper_names = map(lambda x: x.upper(),names)
# print(list(upper_names))

# def check_land(name):
#     if 'land' in name:
#         return True
#     else:
#         return False
    
# land_country = filter(check_land,countries)
# print(list(land_country))

# def six_len(name):
#     if len(name) == 6:
#         return True
#     else:
#         return False
    
# six_len_country = filter(six_len,countries)
# print(list(six_len_country))

# def more_six_len(name):
#     if len(name) >= 6:
#         return True
#     else:
#         return False
    
# more_six_len_country = filter(more_six_len,countries)
# print(list(more_six_len_country))

# def check_E(name):
#     if 'E' in name:
#         return True
#     else:
#         return False
    
# E_country = filter(check_E,countries)
# print(list(E_country))

# upper_six_len_country = filter(six_len,list(map(lambda x: x.upper(),countries)))
# print(list(upper_six_len_country))

# def get_string_list(lst: list):
#     def string_item(lst_2: list):
#         i = 0
#         while type(lst_2[i]) == str:
#             i += 1
#             if i == len(lst_2)-1:
#                 return True
#         else:
#             return False
#     if string_item(lst) == True:
#         return lst
#     else:
#         return None
    
# print(get_string_list(numbers))

# from functools import reduce
# sum = reduce(lambda x,y: x+y,numbers)
# print(sum)

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# sentence = reduce(lambda x,y: x + (', and ' if y == countries[-1] else ', ') + y,countries) + ' are north European countries'
# print(sentence)

from countries import countries

# # 'land','ia','island','stan'
# def categorize_countries(lst):
#     land_country = [i for i in countries if 'land' in i]
#     ia_country = [i for i in countries if 'ia' in i]
#     island_country = [i for i in countries if 'Island' in i]
#     stan_country = [i for i in countries if 'stan' in i]
#     print(land_country)
#     print(ia_country)
#     print(island_country)
#     print(stan_country)

# categorize_countries(countries)

import string

Alphabet = list(string.ascii_uppercase)

def dic_country(lst: list):
    dictionary = {}
    for name in lst:
        for i in range(len(Alphabet)):
            if name.startswith(Alphabet[i]):
                if Alphabet[i] in dictionary:
                    dictionary[Alphabet[i]] += 1
                else:
                    dictionary[Alphabet[i]] = 1
    return dictionary

print(dic_country(countries))

def get_first_ten_countries(lst: list):
    return lst[:10]

print(get_first_ten_countries(countries))

def get_last_ten_countries(lst: list):
    return lst[-10:]

print(get_last_ten_countries(countries))

from countries_data import country

name_sort_country = country.sort(key=lambda x: x['name'])
print(name_sort_country)