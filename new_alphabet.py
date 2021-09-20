# 作成中
s = list()
res = list()

# 入力
x = input()
n = int(input())
for i in range(n):
     s.append(input())

# 新しいアルファベットの辞書型配列
dict = {}
numArray = []
res = []
cnt = 1
for w in x:
    dict[w] = cnt
    cnt = cnt + 1
print(dict)

for w in range(len(s)):
    for char in range(len(s[w])):
        if char == 0:
            numArray.append(dict[s[w][char]])
            print(numArray)
        else:
            temp = str(numArray[w]) + str(dict[s[w][char]])
            numArray[w] = int(temp)
            print(numArray)

numArray.sort()
for num in range(len(numArray)):
    for i in range(len(str(numArray[num]))):
        for j,v in dict.items():
            if str(v) == str(numArray[num])[i]:
                if i == 0:
                    res.append(j)
                    print(res)
                else:
                    res[num] = res[num] + j
                    print(res)

for r in res:
    print(r)
