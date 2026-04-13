"""list_1 = []
fruits = ["banana", "orange", "apple", "lemon", "lime"]
print(len(fruits))
print(fruits[0])
print(fruits[2])
print(fruits[4])
prof = ["waha", 20, 170, "single", "Japan"]
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(prof)
print(companies)
print(len(companies))
print(f"{companies[0]}, {companies[3]}, {companies[6]}")
companies[4] = "Nintendo"
print(companies)
companies.insert(3, "IT")
companies[1] = companies[1].upper()
print(companies)
com_result = ' #;'.join(companies)
print(com_result)
print("Facebook" in companies)
companies.sort()
print(companies)
companies.reverse()
print(companies)
first_com = companies[0:3]
last_com = companies[len(companies)-3:]
print(f"{first_com}, {last_com}")
companies.remove(companies[0])
companies.remove(companies[len(companies)-1])
companies.clear()
print(companies)
del companies
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
print(front_end)
full_stuck = front_end.copy()
full_stuck.insert(5,"Python")
full_stuck.insert(6,"SQL")
print(full_stuck)"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.insert(0,ages[0])
ages.insert(len(ages)-1,ages[len(ages)-1])
print(ages)
if len(ages)%2 == 0:
    mid_ages = ((ages[round((len(ages)/2)-1)] + ages[round((len(ages)/2 + 1)-1)])/2)
else:
    mid_ages = ages[len(ages)//2]
print(mid_ages)
ave_age = sum(ages) / len(ages)
print(f"The average of ages is {ave_age}.")
range_of_age = max(ages) - min(ages)
print(f"The range of ages is {range_of_age}")
minus_value_1 = abs(min(ages) - ave_age)
minus_value_2 = abs(max(ages) - ave_age)
if minus_value_1 > minus_value_2:
    print("The average is close to the maximum")
else:
    print("The average is close to the minimum")
