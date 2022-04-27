# minimum distance between two numbers
'''
The task is to find the distance between two numbers
'''
# basic approach is to check only consecutive pairs of x and y for every occuring element is not similar to current element update the minimum distance
# 1- create prev = -1 and m = sys.maxsize
# 2 - traverse and check for x and y !=-1 and a[prev]!= a[i] , update dist max(m, i-prev)


# import sys


def minimumDist(a, x, y):
    i = 0
    n = len(a)
    prev = -1
    m = 99999999

    for i in range(n):
        if a[i] == x or a[i] == y:
            if(prev != -1 and a[i] != a[prev]):
                m = min(m, i-prev)

            prev = i

    if (m == 999999):
        return -1

    return m


arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]

x = 0
y = 8
print(minimumDist(arr, x, y))
