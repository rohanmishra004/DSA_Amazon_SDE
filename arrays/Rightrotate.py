def rightRotate(a, d):
    temp = []
    n = len(a)
    for i in range(n-d, n):
        temp.append(a[i])

    for i in range(0, n-d):
        temp.append(a[i])

    return temp


a1 = [1, 2, 3, 4, 5, 6]
d = 2
print(rightRotate(a1, d))
