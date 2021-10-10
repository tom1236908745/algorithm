n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(0, n - 1):
    if arr[i] > arr[i + 1]:
        cnt += arr[i] - arr[i + 1]
        arr[i + 1] += arr[i] - arr[i + 1]

print(cnt)
