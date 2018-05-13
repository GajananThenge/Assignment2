'''
Problem Statement 1:
Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()'''


def myreduce(func, lst):
    try:
        if len(lst) == 0:
            raise Exception("Empty list")
        first_val = lst[0]

        if len(lst) == 1:
            return first_val

        for i in lst[1:]:
            first_val = func(first_val, i)
        return first_val
    except Exception as e:
        print(e)


print(myreduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))

''' Problem Statement 2:
Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()'''


def my_filter(func, lst):
    try:
        result = []
        for i in lst:
            if func(i) is True:
                result.append(i)
        print(result)
    except Exception as e:
        print(e)


my_filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6])
