'''
Define a function histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******

'''
num = [1,3,5,4]
def histogram(num):
    for i in num:
        print("*"*i)
histogram(num)