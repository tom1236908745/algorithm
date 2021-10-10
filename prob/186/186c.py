num = int(input())
cnt = 0

for i in range(num):
    if '7' in str(i + 1) or '7' in oct(i + 1):
        continue
    cnt += 1

print(cnt)