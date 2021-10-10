# 未
n,k = map(int,input().split())

fre_dict = {}

for i in range(n):
    arr = list(map(int, input().split()))

    if (arr[0] in fre_dict):
        fre_dict[arr[0]] = fre_dict[arr[0]] + arr[1]
    else:
        fre_dict[arr[0]] = arr[1]

cnt = 0
while k > 0:
    if i in fre_dict:
        k += fre_dict[i]

    k -= 1
    cnt += 1

print(cnt)

