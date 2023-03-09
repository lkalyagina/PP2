#Implement a generator that returns all numbers from (n) down to 0.
n = int(input())

a = [i for i in range(n, 0, -1)]
b = [i for i in a]
print(b)