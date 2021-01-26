def heapsort(arr):  # 选择排序的优化
    l = len(arr)
    res = []
    for i in range(l):  # 让arr符合堆的性质，然后把第一个踢出去
        tmpl = len(arr)
        for j in range(tmpl//2-1, -1, -1): # 从len/2 -1的位置开始
            min_son = 2 * j + 1
            while 2 * j + 1 < tmpl:
                if min_son + 1 < tmpl and arr[min_son + 1] < arr[min_son]:
                    min_son = min_son + 1
                if arr[min_son] < arr[j]:
                    arr[min_son], arr[j] = arr[j], arr[min_son]
                    j = min_son
                else:
                    break
        res.append(arr.pop(0))
    print(res)


# 复杂度 nlogn
if __name__ == '__main__':
    num = [5, 11, 1, 17, 10, 10, 18, 15, 13, 5, 19, 11, 6, 4, 8, 1, 2, 13, 11, 1]
    heapsort(num)
