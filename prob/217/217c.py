length = int(input())
arr = []
ans_arr = []
for _ in range(length):
    arr.append(None)

temp_arr = list(map(int, input().strip().split()))

for i in range(length):
    index = int(temp_arr[i])
    arr[index - 1] = i


for i in range(length):
    if i == length - 1:
        print(arr[i] + 1)
    else:
        print(arr[i] + 1, end=' ')