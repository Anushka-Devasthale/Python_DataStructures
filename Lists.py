#Create a List
x = []
y = ['a', 1, 'ab', 2, 3, 4] #Not homegeneous. can contain anything

x.append(2) #add item towards the end
x.append(3)
x.extend(y)#add another list towards the end
print(x)
print(y)

x.pop() #pops the last item
x.remove(1) #removes 1 from list
print(x)

del(y)
del(x[1])
print(x)

#List Comprehension
a= [i for i in range(8) ]
print(a)
b =[i**2 for i in range(5) if i>1]
print(b)

#insert
x.insert(1,'python')
print(x)

#Reverse
x.reverse()
print(x)

#Sort
a.sort(reverse = True)
print(a)

#Length
print(len(a))