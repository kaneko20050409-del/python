# def add_two_numbers(a,b):
#     sum = a + b
#     return sum

# print(add_two_numbers(7,3))

# def area_of_circle(r):
#     pi = 3.14
#     area = pi * r * r
#     return area

# print(area_of_circle(7))

def add_all_nums(*nums):
    result = 0
    for num in nums:
        if type(num) != int:
            result = 'The argument has not-number.'
            break
        else:
            result += num
    return result

print(add_all_nums(1,3,4,5,6,7))

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5)) + 32
    return fahrenheit

print(f"35.0C degree equal {convert_celsius_to_fahrenheit(35)}F.")

def check_season(month):
    if month=='December' or month=='January' or month=='February':
        return 'Winter'
    if month=='March' or month=='April' or month=='May':
        return 'Spring'
    if month=='June' or month=='July' or month=='August':
        return 'Summer'
    if month=='September' or month=='October' or month=='November':
        return 'Autumn'
    
print(f'March is {check_season('March')}.')

def calculate_slope(a,b,c):
    slope = -(b/a)
    return slope

print(f'The slope of [2x+5y+9=0] is {calculate_slope(2,5,9)}.')

def solve_quadratic_equation(a,b,c):
    answer_1 = -((-b+(b^2-4*a*c)**(1/2))/2*a)
    answer_2 = -((-b-(b^2-4*a*c)**(1/2))/2*a)
    answer = [answer_1,answer_2]
    return answer

print(f'The answer of 3x^2+4x+7=0 is {solve_quadratic_equation(3,4,7)[0]} and {solve_quadratic_equation(3,4,7)[1]}.')

def print_list(lst: list):
    for item in lst:
        print(f'*{item}')

print_list(['apple','banana','grape','orange','lemon'])

def reverse_list(lst: list):
    len_lst = len(lst)
    for i in range(1,len_lst):
        for j in range(len_lst-i):
            kari = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = kari
    return lst

fruits = ['apple','banana','grape','orange','lemon']
print(reverse_list(fruits))

def capitalize_list_item(lst: list):
    for i in range(len(lst)):
        lst[i] = lst[i].upper()
    return lst

print(capitalize_list_item(fruits)) 

def add_item(lst: list,new):
    lst.append(new)
    return lst

print(add_item(fruits,'Strawberry'))

def removed_item(lst: list,remove):
    lst.remove(remove)
    return lst

print(removed_item(fruits,'BANANA'))

def sum_of_numbers(num: int):
    result = 0
    for i in range(num+1):
        result += i
    return result

print(sum_of_numbers(8))

def sum_of_odd(num: int):
    result = 0
    for i in range(num+1):
        if i%2==0:
            pass
        else:
            result += i
    return result

print(sum_of_odd(8))

def sum_of_even(num: int):
    result=0
    for i in range(num+1):
        if i%2==0:
            result += i
        else:
            pass
    return result

print(sum_of_even(8))

def evens_and_odds(num: int):
    num_of_odds = 0
    num_of_evens = 0
    for i in range(num+1):
        if i%2==0:
            num_of_evens += 1
        else:
            num_of_odds += 1
    return [num_of_odds,num_of_evens]

print(f'The number of odds are {evens_and_odds(100)[0]}.')
print(f'The number of evens are {evens_and_odds(100)[1]}.')

def factorial(num: int):
    result = 1
    for i in range(1,num+1):
        result *=i
    return result

print(factorial(7))

def is_empty(name,para):
    if len(para)==0:
        return f'{name} is empty.'
    else:
        return f'{name} has item.'
    
print(is_empty('fruits',fruits))
company = []
print(is_empty('company',company))

def statistic_calculator(num: list):
    mean = 0
    median = 0
    mode = []
    num_range = 0
    variance = 0
    std = 0
    sum_1 = 0
    sum_2 = 0
    appeal_num = {}
    num.sort()

    # 平均値
    for i in num:
        sum_1 += i
        mean = sum_1/len(num)

    # 中央値
    if len(num)%2 == 1:
        median = num[int(len(num)/2)]
    else:
        median = (num[int((len(num)-1)/2)] + num[int((len(num))/2)])/2

    # 最頻値
    for i in num:
        appeal_num[i] = num.count(i)
    item_list = list(appeal_num.items())
    count = [item[1] for item in item_list]
    max_count = max(count)
    min_count = min(count)
    if max_count == min_count:
        mode = 'They don\'t have mode.'
    else:
        for i in range(len(item_list)):
            if item_list[i][1] == max_count:
                mode.append(item_list[i][0])
    
    # 範囲
    max_num = max(num)
    min_num = min(num)
    num_range = max_num - min_num

    # 分散
    for number in num:
        sum_2 += (number - mean)**2
    variance = sum_2/len(num)

    # 標準偏差
    std = variance**(1/2)

    return [mean,median,mode,num_range,variance,std]

number_1 = [2,5,6,13,19,30]
for i in range(6):
    print(statistic_calculator(number_1)[i])

def greet(name = 'Guest'):
    print(f'Hello, {name}!')

greet('John')
greet()

def show_args(**args):
    print('Received: ')
    for key, value in args.items():
        print(f'{key}: {value}')

profile = {
    'name':'Alice',
    'age':30,
    'city':'New York',
}
show_args(**profile)
show_args(name="Bob", pet="Fluffy, the bunny")

def is_prime(num: int):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False  
    return True  
        
print(is_prime(43))

# 中級編　素数判定するにはルートnまで調べれば十分　必ずルートnまでに一つ約数が存在するはずだから
# 計算効率がとても上がる
import math
def intermediate_is_prime(num: int):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    limit = int(math.sqrt(num))
    for i in range(3,limit+1,2):
        if num%i == 0:
            return False
    return True

print(intermediate_is_prime(100003))

def check_unique_item(lst: list):
    dic = {}
    for item in lst:
        dic[item] = lst.count(item)
    for item in lst:
        if dic[item] != 1:
            return False
    return True

print(check_unique_item(fruits))

def efficient_check_unique(lst: list):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False
    
print(efficient_check_unique(fruits))

# another example
# def check_unique_item(lst: list):
#     seen = set()  # すでに現れた要素を記録するセット
#     for item in lst:
#         if item in seen:
#             return False  # すでに出現していたらその時点で終了
#         seen.add(item)
#     return True

def check_data_type(lst: list):
    if not lst:
        return False
    represent_type = type(lst[0])
    for item in lst:
        if type(item) != represent_type:
            return False
    return True

print(check_data_type(fruits))

# pythonらしい書き方
# def check_data_type(lst: list):
#     if not lst: return True
    
#     first_type = type(lst[0])
#     # 「すべての要素の型が、最初の要素の型と同じであること」を確認
#     return all(type(item) == first_type for item in lst)

# map(関数,引数)で引数にはリストなど複数のデータを持つものをとる。すべての引数に関数を適用する

def check_variable(variable: str):
    print(variable.isidentifier())

check_variable('Jack')

from countries_data import country

def most_spoken_languages(lst: list):
    lang_dic = {}
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i]["languages"])):
            if lst[i]["languages"][j] in lang_dic:
                lang_dic[lst[i]["languages"][j]] += lst[i]["population"]
            else:
                lang_dic[lst[i]["languages"][j]] = lst[i]["population"]

    item = list(lang_dic.items())
    item.sort(key=lambda x:x[1], reverse=True)

    for i in range(10,21):
        result.append(item[i][0])

    return reverse_list(result)

print(most_spoken_languages(country))

def most_populated_countries(lst: list):
    result = []
    country.sort(key=lambda x:x["population"], reverse=True)
    for i in range(10,21):
        result.append(country[i]['name'])
    return reverse_list(result)

print(most_populated_countries(country))