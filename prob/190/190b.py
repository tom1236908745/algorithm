X,Y,Z = map(int,input().split())

first_arr = []
second_arr = []

for i in range(X):
    temp_f,temp_s = map(int,input().split())
    first_arr.append(temp_f)
    second_arr.append(temp_s)

while i < X:
    if first_arr[i] < Y and second_arr[i] > Z:
        print("Yes")
        break
    i += 1
if i == X:
    print("No")