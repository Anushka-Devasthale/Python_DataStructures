#Tuples are Immutable, cannot be chnaged. used for fixed data
x = tuple()
y =(1,2,3)
z = 1,2,3
a =2,
print(x)
print(y)
print(z)
print(a)

#Tuples are Immutable, but list members in tuple can be changed
a = [i for i in range(1,15,2)]
print(a)
list = [10,80,90]
a.extend([list])
print(a)
del(a[7][2])
print(a)