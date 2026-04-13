"""tuple_1 = ()
brothers = ('John','Ben','Henry','Jackson','Gangpin')
sisters = ('Nancy','Yui','Ray','Octan')
siblings = brothers + sisters
print(len(siblings))
Family = siblings + ('Tacky','Ung')
print(Family)
siblings = Family[0:9]
parents = Family[9:]
print(siblings)
print(parents)"""
fruits = ('banana','apple','grape','kiwi','lemon')
vegetables = ('cucumber','tomato','potato','onion','carrot')
animal = ('cow','chicken','camel','elephant','lion')
food_stuff_tp = fruits + vegetables + animal
food_stuff_lst = list(food_stuff_tp)
print(food_stuff_lst)
if len(food_stuff_lst)%2 == 0:
    mid_food = (food_stuff_lst[(round(len(food_stuff_lst)/2))-1], food_stuff_lst[(round((len(food_stuff_lst)+1)/2))-1])
else:
    mid_food = (food_stuff_lst[((round(len(food_stuff_lst)/2))-1)])
print(mid_food)
del food_stuff_tp