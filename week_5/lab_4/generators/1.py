#Create a generator that generates the squares of numbers up to some number N.

n=int(input())
a = [i for i in range(0, n+1)]
b = [i**2 for i in a]

print(b)