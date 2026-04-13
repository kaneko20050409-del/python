from random import random, randint
import string

# def id_generator():
#     id = ''
#     random_num = []
#     character = list(string.digits) + list(string.ascii_lowercase)
#     for i in range(6):
#         random_num.append(randint(0,len(character)-1))
#     for i in range(6):
#         id += character[random_num[i]]
#     return id

# print(id_generator())

# def user_id_gen_by_user():
#     num_of_characters = int(input('Enter the number of characters: '))
#     num_of_id = int(input('Enter the number of id: '))
#     id = []
#     character = list(string.digits) + list(string.ascii_letters)
#     for i in range(num_of_id):
#         kari = ''
#         random_num = []
#         for i in range(num_of_characters):
#             random_num.append(randint(0,len(character)-1))
#         for i in range(num_of_characters):
#             kari += character[random_num[i]]
#         id.append(kari)
#     for i in range(len(id)):
#         print(id[i])

# user_id_gen_by_user()

# def rgb_color_gen():
#     rgb = []
#     for i in range(3):
#         rgb.append(randint(0,255))
#     return rgb

# print(f'rgb({rgb_color_gen()[0]},{rgb_color_gen()[1]},{rgb_color_gen()[2]})')

hexadigit = list(string.hexdigits)[0:16]

def hexdigit_gen(num: int):
    hex_dig = []
    ten_degree = num//16
    one_degree = num - (16 * ten_degree)
    hex_dig.append(hexadigit[ten_degree])
    hex_dig.append(hexadigit[one_degree])
    return f'{hex_dig[0]}{hex_dig[1]}'

def list_of_hexa_colors():
    num_of_colors = int(input('Enter the number of colors: '))
    rgb = []
    for i in range(num_of_colors):
        kari = ''
        for i in range(3):
            kari += (hexdigit_gen(randint(0,255)))
        rgb.append(kari)
    for item in rgb:
        print(f'#{item}')

# list_of_hexa_colors()

def list_of_rgb_colors():
    num_colors = int(input('Enter the number of colors: '))
    rgb = []
    for i in range(num_colors):
        kari = []
        for i in range(3):
            kari.append(randint(0,255))
        rgb.append(kari)
    for i in range(num_colors):
        print(f'({rgb[i][0]},{rgb[i][1]},{rgb[i][2]})')

# list_of_rgb_colors()

def generate_colors(type: str,num: int):
    if type == 'hexa':
        rgb = []
        for i in range(num):
            kari = '#'
            for i in range(3):
                kari += (hexdigit_gen(randint(0,255)))
            rgb.append(kari)
        print(rgb)
    elif type == 'rgb':
        rgb = []
        result = []
        for i in range(num):
            kari = []
            for i in range(3):
                kari.append(randint(0,255))
            rgb.append(kari)
        for i in range(num):
            result.append(f'rgb({rgb[i][0]},{rgb[i][1]},{rgb[i][2]})')
        print(result)
            

# generate_colors('rgb',4)
# generate_colors('hexa',6)

def shuffle_list(lst: list):
    len_list = len(lst)
    random_num = []
    new_list = []
    while len(random_num) != len(lst):
        random_kari = randint(0,len(lst)-1)
        if random_kari in random_num:
            pass
        else:
            random_num.append(random_kari)
    for i in range(len_list):
        new_list.append(lst[random_num[i]])
    return new_list

fruits = [1,2,3,4,5,6,7,8]
number = ['Apple','lemon','grape','orange']

# print(shuffle_list(fruits))
# print(shuffle_list(number))

# かしこい
def kosiro_shuffle_list(lst: list):
    shuffled_list = []
    for i in range(len(list)):
        shuffled_list.append(list.pop(randint(0,len(list)-1)))
    return shuffled_list

def random_num_gen():
    result = []
    digit = list(string.digits)
    for i in range(7):
        result.append(digit.pop(randint(0,len(digit)-1)))
    return result

# print(random_num_gen())

# かしこい
def kosiro_random_num_gen():
    return shuffle_list([0,1,2,3,4,5,6,7,8,9])[0:7]

print(kosiro_random_num_gen())

