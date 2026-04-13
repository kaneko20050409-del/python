numbers = [-4,-3,-2,-1,0,2,4,6]
neg_num = [i for i in numbers if i <= 0]
print(neg_num)

list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
num_list = [i for row in list_of_list for i in row]
print(num_list)

tuple_of_list = [(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
for i in range(11):
    print(tuple_of_list[i])

country = [[('Finland','Helsinki')],[('Sweden','Stockholm')],[('Norway','Oslo')]]

output = [[name.upper(),name[:3].upper(),capital.upper()] for sublist in country for name,capital in sublist]
print(output)

output_2 = [{f'country: {name.upper()}, city: {capital.upper()}'} for sublist in country for name,capital in sublist]
print(output_2)

names = [[('Asabeneh','Yetayeh')],[('David','Smith')],[('Donald','Trump')],[('Bill','Gates')]]

output_3 = [(last + ' ' + family) for sublist in names for last,family in sublist]
print(output_3)

print(f'The slope of 6x+3y+6=0 is {(lambda a,b,c: -b/a)(6,3,6)}.')
print(f'The interception of y of 8x+9y+3=0 is {(lambda a,b,c: -c/b)(8,9,3)}.')
