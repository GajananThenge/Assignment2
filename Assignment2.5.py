'''
Problem Statement 1:
Write a Python program using function concept that maps list of words into a list of
integers representing the lengths of the corresponding words.
Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as
[2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.'''


# Using in-built function len()
def getlength(word):
    return len(word)


# Without using in-built function
def getlength(word):
    j = 0
    for i in word:
        j += 1
    return j


print(list(map(getlength, ['ab', 'cde', 'erty'])))

'''Problem Statement 2:
Write a Python function which takes a character (i.e. a string of length 1) and returns
True if it is a vowel, False otherwise.'''


def findvowels(string):
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u']:
            return True
        return False


input_data = input()
print(findvowels(input_data))
