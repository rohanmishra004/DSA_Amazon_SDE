# max and second max element in an array
import sys


def maxAndsecond(arr):
    n = len(arr)
    first = arr[0]
    second = -sys.maxsize

    if n < 2:
        return "Invalid"

    for i in range(1, n):
        if arr[i] > first:
            second = first
            first = arr[i]

        elif arr[i] > second:
            second = arr[i]

    return (f"First {first} \nSecond {second}")


print(maxAndsecond([1, 12, 14, 15, 13, 2, 4]))
