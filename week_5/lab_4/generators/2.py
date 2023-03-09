#Write a program using generator to print the even numbers between 0 and n in comma separated 
#form where n is input from console.

n=int(input())
a = [i for i in range(0, n) if i%2==0]
print(a)
