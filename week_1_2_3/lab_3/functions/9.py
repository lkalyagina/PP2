'''
Write a function that computes the volume of a sphere given its radius.
'''

r = int(input())
def vol(r):
    return((4/3)*3.14*r**3)
print(vol(r))