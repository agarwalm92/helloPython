

#LISTS

#Copy vs Ref
x = [4, True, "hello"]
print(x)

y = x #stores a ref of the list
z = x [:] #stores a copy of the list
x[1] = False #change made in x triggers change in y as well, but not in z as its a copy of the list
print(x,y,z)

