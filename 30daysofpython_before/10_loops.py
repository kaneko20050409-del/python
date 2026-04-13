'''language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

print(person.items())

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

for i in range(11):
    print(i)
number = 0
while number < 11:
    print(number)
    number += 1 

for i in range(10,-1,-1):
    print(i)
number = 0
while number < -1:
    print(number)
    number -= 1 

for i in range(1,8):
    print('#'*i)

for i in range(1,9):
    print('# '*8) 

for i in range(11):
    print(f'{i} * {i} = {i*i}')

library = ['Python','Numpy','Pandas','Django','Flask']
for i in range(len(library)):
    print(library[i]) 

for i in range(101):
    if i%2 == 0:
        print(i) 

for i in range(101):
    if i%2 == 1:
        print(i) 

number = 0
for i in range(101):
    number += i
print(f'The sum of all numbers is {number}.')

even_num = 0
odd_num = 0
for i in range(101):
    if i%2 == 0:
        even_num += i
    else:
        odd_num += i
print(f'The sum of all evens is {even_num}. And the sum of all odds is {odd_num}.') 

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

for i in range(len(countries)):
    if 'land' in countries[i]:
        print(countries[i])

def kaijou(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

fruits = ['banana','orange','mango','lemon']
fruits_ex = []

for i in range(len(fruits)-1,-1,-1):
    fruits_ex.append(fruits[i])
print(fruits_ex) '''

from countries_data import country

languages_lst = []
for i in range(len(country)):
    langs = country[i]["languages"]
    if isinstance(langs, list):
        languages_lst.extend(langs)
    if isinstance(langs, str):
        languages_lst.append(langs)
print(len(languages_lst))
languages_set = set(languages_lst)
print(len(languages_set))

lang_dic = {}
for i in range(len(country)):
    for j in range(len(country[i]["languages"])):
        if country[i]["languages"][j] in lang_dic:
            lang_dic[country[i]["languages"][j]] += country[i]["population"]
        else:
            lang_dic[country[i]["languages"][j]] = country[i]["population"]

item = list(lang_dic.items())
item.sort(key=lambda x:x[1], reverse=True)

for i in range(10):
    print(item[i][0])

country.sort(key=lambda x:x["population"], reverse=True)
for i in range(10):
    print(country[i]["name"])
