n = int(input())
ans = []

while n > 0:

    if n % 2 == 0:
        n /= 2
        ans.append("B")
    else:
        n -= 1
        ans.append("A")
ans.reverse()

[print(x,end="") for x in ans]