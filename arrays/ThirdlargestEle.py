# Third largest Element

# given array is unsorted :
# 1- Sort the array
# 2 -Once sorted , loop from reverse side and check for value


# for sorting we can use any mechanism - mergeSort , quickSort or insertionSort


def sortarr(a1):
    n = len(a1)

    for i in range(n-1):
        for j in range(n-i-1):
            if a1[j] > a1[j+1]:
                a1[j], a1[j+1] = a1[j+1], a1[j]

    return a1


def findKthLargest(a1):
    n = len(a1)
    k = n-3
    sortarr(a1)

    for i in reversed(range(n)):
        if i == k:
            return a1[i]
    return None


print(findKthLargest([12, 1, 2, 5, 13]))
