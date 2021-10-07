def factorial(num, r):
    res = 1
    if r != 0:
        for i in range(r):
            res *= num

    return res


##### main @@@@@
base = int(input())
arr1, arr2 = input().strip().split()
len_arr1 = len(arr1)
len_arr2 = len(arr2)
n = len_arr1 if len_arr1 >= len_arr2 else len_arr2

i = 0
val1 = 0
val2 = 0

while i < n:
    if i < len(arr1):
        len_arr1 -= 1
        val1 += factorial(base, len_arr1) * int(arr1[i])

    if i < len(arr2):
        len_arr2 -= 1
        val2 += factorial(base, len_arr2) * int(arr2[i])
    i += 1

print(val1 * val2)


def factorial(num, r):
    res = 1
    if r != 0:
        for i in range(r):
            res *= num

    return res


##### main @@@@@
base = int(input())
arr1, arr2 = input().strip().split()
len_arr1 = len(arr1)
len_arr2 = len(arr2)
n = len_arr1 if len_arr1 >= len_arr2 else len_arr2

i = 0
val1 = 0
val2 = 0

while i < n:
    if i < len(arr1):
        len_arr1 -= 1
        val1 += factorial(base, len_arr1) * int(arr1[i])

    if i < len(arr2):
        len_arr2 -= 1
        val2 += factorial(base, len_arr2) * int(arr2[i])
    i += 1

print(val1 * val2)
