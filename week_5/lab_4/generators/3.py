#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, 
#between a given range 0 and n.

n = int(input())
a = [i for i in range(0, n+1)]
b = [i for i in a if i%3==0 and i%4==0]
print(b)