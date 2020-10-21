pizzas = ['dominos', 'pizza hut', 'papa johns']
for pizza in pizzas: 
    print(f'I like {pizza.title()}')
print('\nI love pizza!')

for value in range(0, 8, 3):
    print(value)
    #range and loops
#placing a range of numbers in a list
even_numbers = list(range(1,6))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#list comprehention

squares = [value**2 for value in range(1,11)]
print(squares)