# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

"""print(len(it_companies))
it_companies.add('Twitter')
more_ex = {'Yahoo','NVIDIA','Tesla','Instagram'}
it_companies.update(more_ex)
print(it_companies)
it_companies.remove('Oracle')
it_companies.discard('Un')
print(it_companies)"""

C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A,B,C
len_list = len(age)
set_age = set(age)
len_set = len(set_age)
print(f"{len_list},{len_set}")

Greeting = "I am a teacher and I love to inspire and teach people."
Greeting = Greeting.split()
print(Greeting)
Greeting = set(Greeting)
print(Greeting)
unique_words = len(Greeting)
print(f"The number of unique words are {unique_words}.")
