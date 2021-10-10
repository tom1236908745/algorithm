# 作成中
# ref https://tech-shelf.hatenablog.com/entry/algorithm/quicksort
import random


def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] <= pivot:
            # A[i+1]の要素はピボットより大きい要素なので
            # A[i+1]とピボット以下の大きさの要素A[j]の位置を入れ替える
            i += 1
            A[i], A[j] = A[j], A[i]
    A.insert(i + 1, pivot)
    A.pop()
    return


A = list(range(1, 11))
random.shuffle(A)
print(A)
partition(A, 0, len(A) - 1)
print(A)
