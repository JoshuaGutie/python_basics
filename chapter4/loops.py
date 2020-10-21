#listing numbers 1-20s
for value in range(1,21,2):
    print(value)

list = []
for value in range(1,10):
    list.append(value)
#print(sum(list))

#multiples of 3
multiples = []
for value in range(3,30):
    multi = value *3
    multiples.append(multi)
#print(multiples)

#list compression of first 10 cubes with a slice
cubes = [value**3 for value in range(1,10)]
print(cubes[1:5:3])

