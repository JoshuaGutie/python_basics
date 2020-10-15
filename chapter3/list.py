#changing lists
bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles[0].title())

bicycles[0] = "redline2"
bicycles.append('trek')
print(bicycles)

#creating list from scratch
people  = []
people.append('josh')
people.append('joel')
people.append('josiah')
people.append('john')

print(people)
#delete from list
del people[0]
#popping
popping_people = people.pop()
first_name = people.pop(0)
print(people)
print(popping_people)
print(first_name)

