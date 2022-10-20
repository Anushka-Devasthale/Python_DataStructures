#Print all values under 10
a = [i for i in range(0,11)]
print(a)


#Squares under 10
b = [sq**2 for sq in range(1,11)]
print(b)

#Odd numbers till 10

c = [odd for odd in range(1,10,2)]
print(c)

#print even numbers

d = [even for even in range(1,11) if even%2==0]
print(d)

#Print Multiples of 10
e =[mul*5 for mul in range(1,6)]
print(e)

#Fetch all numbers from a string
s = 'My name is El. I am learning Python 3. I am born in 1998.'
f = [num for num in s if num.isnumeric() ]
print(f)