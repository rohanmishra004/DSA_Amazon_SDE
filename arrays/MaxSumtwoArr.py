# Max Sum of two array

def maxSum(a1, a2):
    m = len(a1)
    n = len(a2)

    i, j = 0, 0
    res = 0
    sum1 = 0
    sum2 = 0

    while i < m and j < n:
        if a1[i] < a2[j]:
            sum1 += a1[i]
            i += 1
        elif a1[i] > a2[j]:
            sum2 += a2[j]
            j += 1
        else:  # when both values are same
            res += max(sum1, sum2)+a2[j]

            sum1 = 0
            sum2 = 0
            i += 1
            j += 1

    # loop for remaining values

    while i < m:
        sum1 += a1[i]
        i += 1
    while j < n:
        sum2 += a2[j]
        j += 1

    res += max(sum1, sum2)

    return res


a1 = [2, 3, 7, 10, 12, 15, 30, 34]
a2 = [1, 5, 7, 8, 10, 15, 16, 19]

print(maxSum(a1, a2))
