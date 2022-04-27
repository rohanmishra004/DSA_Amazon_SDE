# Left Rotate --> Rotate the array by left one by one

# def leftRotateOne(a):
#     n = len(a)
#     temp = a[0]
#     for i in range(n-1):
#         a[i] = a[i+1]
#     a[n-1] = temp


# def leftRotate(a, d):
#     n = len(a)
#     if d == 0 or d == n:
#         return
#     for i in range(d):

#         leftRotateOne(a)
#     return a


# a = [1, 2, 3, 4, 5]
# d = 2
# print(leftRotate(a, d))


# Recursive method for reversal of array

def reverseArray(arr, s, end):
    while s < end:
        temp = arr[s]
        a[s] = a[end]
        a[end] = temp

        s += 1
        end -= 1


def leftRotate(arr, d):
    if d == 0:
        return

    n = len(arr)

    d = d % n
    reverseArray(a, 0, d-1)
    reverseArray(a, d, n-1)
    reverseArray(a, 0, n-1)

    return arr


a = [1, 2, 3, 4, 5]
d = 2
print(leftRotate(a, d))
