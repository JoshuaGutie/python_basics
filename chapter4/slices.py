food = ['pizza', 'cream', 'waffles', 'cake', 'eggs', 'steak', 'chicken', 'ice']
print('my favorite foods are:')
print(food)

friends_food = food[:]
friends_food.append('pork')
food.append('seafood')
print('friends', friends_food)
print('mine', food)


for foods in food:
    print(foods)