dog = {}
dog['name'] = 'John'
dog['color'] = 'Brown'
dog['Breed'] = 'Siba'
dog['legs'] = 4
dog['age'] = 16
student = {}
student['first_name'] = 'jack'
student['last_name'] = 'Hay'
student['gender'] = 'male'
student['age'] = 29
student['martial_status'] = 'single'
student['skills'] = ['Math', 'English', 'Physics', 'Chemistry']
student['country'] = 'Jp'
student['City'] = 'Gifu'
student['address'] = '7283-1748'
print(len(student))
print(student['skills'])
print(type(student['skills']))
if isinstance(student['skills'], list):
    print('Skills is list')
student['skills'].append('PE')
dic_key = student.keys()
dic_value = student.values()
print(dic_key)
print(dic_value)
# student = student.items()
# print(student)
student.pop('first_name')
print(student)
del student