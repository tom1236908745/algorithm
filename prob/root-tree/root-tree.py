NIL = -1

# node のクラス
class node:
    def __init__(self, p, r, l):
        self.p = p
        self.r = r
        self.l = l




# 最後の表示をする関数
def view(u):
    print(f'node {u}:', end='')
    print(f'parent = {nodes[u].p}, ', end='')
    print(f'depth = {Deep[u]}, ', end='')

    if nodes[u].p == NIL:
        print('root, ', end='')
    elif nodes[u].l == NIL:
        print('leaf, ', end='')
    else:
        print('internal node, ', end='')


    i = 0
    c = nodes[u].l
    print('[', end='')
    while c != NIL:

        if i > 0:
            print(', ', end='')
        print(f'{c}', end='')
        c = nodes[c].r
        i += 1

    print(']')

# 各ノードの深さを求める
def rec(top, depth):
    Deep[top] = depth
    if nodes[top].r != NIL:
        rec(nodes[top].r, depth); # 右の兄弟に同じ深さを設定する
    if nodes[top].l != NIL:
        rec(nodes[top].l, depth + 1)

# nodeの配列
nodes = []

##############################################
# main関数

nodeNum = int(input())

# 深さ調べる用の配列
Deep = [NIL] * nodeNum

# Nodesの値を全てNodeで初期化
for i in range(nodeNum):
    nodes.append(node(NIL,NIL,NIL))

i = 0
left = 0
# 各Node、子の数、子の入力
for i in range(nodeNum):
    node = int(input())
    childNum = int(input())
    for j in range(childNum):
        child = int(input())
        if j == 0:
            nodes[node].l = child
        # 兄弟をこの時点で設定
        else:
            nodes[left].r = child
        left = child
        nodes[child].p = node

i = 0

root = 0
for i in range(nodeNum):
    if nodes[i].p == NIL:
        root = i

rec(root, 0)

i = 0
for i in range(nodeNum):
    view(i)



