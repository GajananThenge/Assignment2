'''
2.​ Problem Statement

Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
'''
print([i for i in 'ACADGILD'])

print([i * j for i in [1, 2, 3, 4] for j in ['x', 'y', 'z']])

print([i * j for i in ['x', 'y', 'z'] for j in [1, 2, 3, 4]])

print([[i + j] for i in range(1, 4) for j in range(1, 4)])

print(([i + j for i in range(1, 5) for j in range(1, 5)]))

print([(j, i) for i in range(1, 4) for j in range(1, 4)])
