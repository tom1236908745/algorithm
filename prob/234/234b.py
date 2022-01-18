import math

n = int(input())
arr = [ list(map(int,input().split(" "))) for i in range(n)]


res = 0
for i in range(n):
  for j in range(n):
    temp = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
    if temp > res:
      res = temp
print(math.sqrt(res))