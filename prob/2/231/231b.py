X = {}

N = int(input())
for i in range(N):
  s = input()
  if s in X:
    X[s] += 1
  else:
    X[s] = 1

print(max(X))