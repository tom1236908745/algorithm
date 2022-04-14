list_x = []
list_y = []

for i in range(3):
  x,y= input().split()
  list_x.append(x)
  list_y.append(y)

list_t_x = list(range(2))
list_t_y = list(range(2))
list_t_x[0] = list_x[0]
list_t_y[0] = list_y[0]
cntx = 0
cnty = 0
for i in range(2):
  if list_x[0] != list_x[i + 1]:
    list_t_x[1] = list_x[i+1]
    cntx += 1
  if list_y[0] != list_y[i + 1]:
    list_t_y[1] = list_y[i+1]
    cnty += 1

if cntx == 1:
  print(list_t_x[1])
else:
  print(list_t_x[0])


if cnty == 1:
  print(list_t_y[1])
else:
  print(list_t_y[0])
