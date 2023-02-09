'''
Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
'''

list1 = ["ab", "cd", "ef", "ab", "ac" ]
list2 = []
def func(list1):
    for i in list1:
        if i not in list2:
            list2.append(i)
    print (list2)
func(list1)