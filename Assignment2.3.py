'''
2.​ Problem Statement

Implement a function longestWord() that takes a list of words and returns the longest
one.
'''


def findlongestword(lst):
    try:
        length = [len(i) for i in lst]
        return lst[length.index(max(length))]
    except Exception as e:
        print(e)


lst = ['Acadgild', 'Data Scence Acadgild']
print(findlongestword(lst))

a = [1, 2, 3, 4, 6, 7, 99, 88, 999]
max = 0
for i in a:
    if i > max:
        max = i
print(max)
