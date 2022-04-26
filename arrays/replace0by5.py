# replace all 0 in int with 5
def reverseUtil(temp):
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev*10+digit
        temp = temp//10
    return rev


def replace0by5(a):
    if a == 0:
        return 5

    temp = 0

    while a > 0:
        digit = a % 10
        if digit == 0:
            digit = 5

        temp = temp*10 + digit

        a = a//10

    return reverseUtil(temp)


print(replace0by5(10023))
