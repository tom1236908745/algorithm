# swap 交換
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


##### main ####

# first Array
arr1 = list(input())

# second Array
arr2 = list(input())

i = 0
while 1:

    if i == len(arr1) - 1:
        print("No")
        break

    if i == 0 and arr1 == arr2:
        print("Yes")
        break

    swap(arr1, i, i + 1)
    if arr1 == arr2:
        print("Yes")
        break
    swap(arr1, i, i + 1)

    i += 1