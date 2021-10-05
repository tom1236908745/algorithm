NIL = -1

class node:
    def __init__(self, p, r, l):
        self.p = p
        self.r = r
        self.l = l

# nodeの配列
nodes = []

# main関数
nodeNum = int(input('Enter node number: '))

# Nodesの値を全てNodeで初期化
for i in range(nodeNum):
    nodes.append(node(NIL,NIL,NIL))

i = 0
# TODO: 若干怪しい
left = 0
# 各Node、子の数、子の入力
# for i in range(nodeNum):
#     node = input('node')
#     childNum = input('child num')
#     for j in childNum:
#         child = input('child')
#         if j == 0:
#             nodes[node].l = child
#         # 兄弟をこの時点で設定
#         else:
#             nodes[left].r = child
#         left = child
#         nodes[child].p = node
i = 0
root = 0
# for i in range(nodeNum):
#     if nodes[i].p == NIL:
#         root = i;

# TODO: rec関数
i = 0

for i in range(nodeNum):
    print(f'node: parent->{nodes[i].p}, right->{nodes[i].r}, left->{nodes[i].l}')

