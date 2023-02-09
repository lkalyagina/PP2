'''
Write a Python function that checks whether a word or phrase is palindrome or not. Note: 
A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
'''

a = str(input())
print(a)
def rev(a):
    b = a[::-1]
    print (b)
    if a==b:
        print("Palindrome")
    else:
        print("Not palindrome")
rev(a)