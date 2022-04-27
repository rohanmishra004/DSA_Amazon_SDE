# Third largest Element

# given array is unsorted :
# 1- Sort the array
# 2 -Once sorted , loop from reverse side and check for value


# for sorting we can use any mechanism - mergeSort , quickSort or insertionSort
# in the above for sorting we can use more optimise solution

# import sys


# def sortarr(a1):
#     n = len(a1)

#     for i in range(n-1):
#         for j in range(n-i-1):
#             if a1[j] > a1[j+1]:
#                 a1[j], a1[j+1] = a1[j+1], a1[j]

#     return a1


# def findKthLargest(a1):
#     n = len(a1)
#     k = n-3
#     sortarr(a1)

#     for i in reversed(range(n)):
#         if i == k:
#             return a1[i]
#     return None


# print(findKthLargest([12, 1, 2, 5, 13]))


# naive approach -->
# First find highest ele , then 2nd highest and exlude both
# then find third highest ele and print the result


# def thirdLargest(a):
#     # check base condition

#     n = len(a)
#     if n < 3:
#         return "Invalid"

#     first = a[0]
#     for i in range(1, n):
#         if a[i] > first:
#             first = a[i]

#     second = -sys.maxsize
#     print(second)

#     for i in range(0, n):
#         if (a[i] > second and a[i] < first):
#             second = a[i]

#     third = -sys.maxsize
#     print(third)

#     for i in range(0, n):
#         if a[i] > third and (a[i] < second and a[i] < first):
#             third = a[i]

#     return third


# print(thirdLargest([1, 2, 3, 4, 23, 12, 32]))


# optimized solution of the above approach
# we defind three elements as first , second and third


import sys


def third(a):
    n = len(a)
    if n < 3:
        return "Invalid"

    first = a[0]
    second = -sys.maxsize
    third = -sys.maxsize

    for i in range(1, n):
        if a[i] > first:
            third = second
            second = first
            first = a[i]

        elif a[i] > second:
            second = a[i]
            third = second

        elif a[i] > third:
            third = a[i]

    return third


arr = [12, 7, 14]
print(third(arr))
