'''age = int(input("Enter your age: "))
if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18-age} more years to learn to drive.')

your_age = age
my_age = 20
difference = abs(my_age - your_age)
if my_age >= your_age:
    if difference > 1:
        print(f'You are {difference} years younger than me.')
    else:
        print(f'You are {difference} year younger than me.')
else:
    if difference > 1:
        print(f'You are {difference} years older than me.')
    else:
        print(f'You are {difference} year older than me.')

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else:
    print('a is equal to b')

score = int(input('Enter your score: '))
if score >= 90:
    print('Your grade is A.')
elif score >= 80:
    print('Your grade is B.')
elif score >= 70:
    print('Your grade is C.')
elif score >= 60:
    print('Your grade is D.')
else:
    print('Your score is F.')

month = input('Enter the month: ')
if month == 'September' or month == 'October' or month == 'November':
    print('Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruits = input('Enter the fruit: ')
if add_fruits in fruits:
    print('That fruit already exists in the list.')
else:
    fruits.append(add_fruits)
    print(fruits)'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    print(person['skills'][int(len(person['skills'])/2)])
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python exists in skills')
if 'Javascript' in person['skills'] and 'React' in person['skills'] and int(len(person['skills'])) == 2:
    ('He is a front end developer.')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a back end developer.')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a full stuck developer.')
else:
    print('Unknown title.')

full_name = person['first_name'] + ' ' + person['last_name']

if person['is_married'] == True and person['country'] == 'Finland':
    print(f'{full_name} lives in {person['country']}. He is married.')