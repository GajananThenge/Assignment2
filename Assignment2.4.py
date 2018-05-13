'''
Problem Statement 1:
Write a Python Program(with class concepts) to find the area of the triangle using the
below formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the
parent class and function to calculate the area should be defined in subclass.'''


class Dimensions:
    def __init__(self, s, a, b, c):
        self.s = s
        self.a = a
        self.b = b
        self.c = c


class AreaOfTriangle(Dimensions):
    def getarea(self):
        return (self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5


area = AreaOfTriangle(8, 2, 3, 4)
print((area.getarea()))

'''Problem Statement 2:
Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
'''


def filter_long_words(input_lst, n):
    return [i for i in input_lst if len(i) > n]


filter_long_words(['Can', 'Do', 'Encourge', 'Positive'], 1)
