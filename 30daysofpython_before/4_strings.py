challenge_1 = ['Thirty', 'Days', 'Of', 'Python']
result_1 = ' '.join(challenge_1)
print(result_1)
challenge_2 = ['Coding', 'For', 'All']
result_2 = ' '.join(challenge_2)
print(result_2)
company = result_2
'''print(company)
print(len(company))
Com_uppercase = company.upper()
print(Com_uppercase)
Com_lowercase = company.lower()
print(Com_lowercase)
Com_capi = company.capitalize()
print(Com_capi)
Com_title = company.title()
print(Com_title)
Com_swap = company.swapcase()
print(Com_swap)
first_word = company[0:6]
print(first_word)
result_3 = company.strip(first_word)
result_3 = result_3.strip( )
print(result_3)
sub_string = 'Coding'
if sub_string in company:
    print('String has the word')
print(company.replace('Coding For All' , 'Python'))
intro = 'Python For Everyone'
intro_1 = intro.replace('Everyone' , 'All')
print(intro_1)
print(intro.split())
Tech_com = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(Tech_com.split(', '))'''
print(company[0])
last_index = len(company) - 1
print(last_index)
print(company[13])
print(company[10])
name = 'Python For Everyone'
namex = name.split()
result_3 = ''
for word in namex:
    result_3 += word[0]
acronym_1 = result_3.upper()
print(acronym_1)

name_2 = 'Coding For All'
result_4 = ''
name_2x = name_2.split()
for word in name_2x:
    result_4 += word[0]
acronym_2 = result_4.upper()
print(acronym_2)
print(name_2.index('C'))
print(name_2.index('F'))
name_3 = 'Coding For All People'
print(name_3.rfind('l'))
sentence_1 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_1.index('because'))
print(sentence_1.rfind('because'))
because_3 = sentence_1[31:54]
print(because_3)
print(sentence_1[:31] + sentence_1[54:])
print(name_3.startswith('Coding'))
print(name_3.startswith('coding'))
name_plus = '   Coding For All      '
print(name_plus.strip())
py_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result_5 = ' '.join(py_lib)
print(result_5)
print(f'{"Name":<15}{"Age":<15}{"Country":<15}{"City":<15}')
print(f'{"Asabeneh":<15}{"250":<15}{"Finland":<15}{"Helsinki":<15}')
radius = 10
area = 3.14 * radius ** 2
print(f"radius = {radius}")
print(f"area = 3.14 * {radius} ** 2")
print(f"The area of circle with radius {radius} is {area} meters square")
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")