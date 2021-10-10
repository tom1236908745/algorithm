## 単純に考えると##
# # node のクラス
# class point:
#     def __init__(self, h, w):
#         self.h = h
#         self.w = w
#
# # pointの配列
# points = []
# temp_points = []
# first_row = list(map(int, input().strip().split()))
# h = first_row[0]
# w = first_row[1]
# n = first_row[2]
#
# h_arr = []
# w_arr = []
#
# for i in range(n):
#     input_point = list(map(int, input().strip().split()))
#     points.append(point(input_point[0],input_point[1]))
#     temp_points.append(point(input_point[0],input_point[1]))
#
# ## h
# for i in range(h):
#     for k in range(len(points)):
#         if str(i + 1) in str(points[k].h): continue
#
#         if temp_points[k].h > i + 1:
#             points[k].h -= 1
#         # if k == 0: print(points[k].h, " ", i + 1)
# ## w
# for i in range(w):
#     for k in range(len(points)):
#         if str(i + 1) in str(points[k].w): continue
#
#         if temp_points[k].w > i + 1:
#             points[k].w -= 1
# for i in range(len(points)):
#     print(points[i].h,points[i].w)
H,W,N=map(int,input().split())
X,Y=[],[]
for i in range(N):
  x,y=map(int,input().split())
  X.append(x)
  Y.append(y)
Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))}
Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(Y))))}
for i in range(N):
  print(Xdict[X[i]], Ydict[Y[i]])