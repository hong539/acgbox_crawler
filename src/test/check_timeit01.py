import timeit

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5

# 測試算法運行時間
t = timeit.timeit(lambda: linear_search(arr, x), number=1000)
print('Time taken: {:.6f} s'.format(t))