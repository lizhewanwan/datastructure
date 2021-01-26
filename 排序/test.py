def print_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        logger.info("消耗时间：" + str(round(end - start, 2)))
        return res

    return inner


# 选择，插入，冒泡都是on2的复杂度
@print_time
def bubble(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


@print_time
def bubble_impove(arr):
    l = len(arr)
    left = 0
    end = l - 1
    for i in range(l - 1):
        for j in range(end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                left = j
        arr[end] = arr[left]
    print(arr)


@print_time
def select(arr):  # 选择排序可以用堆排序优化一下
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    print(arr)


@print_time
def insert(arr):  # 插扑克牌，初始状态手里有第一张牌,优化可以用二分查找优化，查找插入的右边界，直接改就行，不用n遍历了。
    l = len(arr)
    for i in range(1, l):
        val = arr[i]
        init = i - 1
        for j in range(init, -1, -1):
            if arr[j] > val:
                arr[i] = arr[j]
                i -= 1
            else:
                break
        arr[i] = val
    print(arr)


# 以下是nlogn的复杂度
@print_time
def heap(arr):  # 堆排序可以看做是选择排序的优化,一共构建n次堆，构建以此，添加头结点，最小的
    l = len(arr)
    res = []
    for i in range(l):
        tmp = len(arr)
        for j in range((tmp>>1)-1,-1,-1):
            min_son = (j << 1) + 1
            while (j<<1) + 1 < tmp:
                if min_son + 1 < tmp and arr[min_son+1] < arr[min_son]:
                    min_son = min_son + 1
                if arr[min_son] < arr[j]:
                    arr[min_son],arr[j] = arr[j],arr[min_son]
                    j = min_son
                else:
                    break
        res.append(arr.pop(0))
    print(res)


def quick(arr):  # 快拍就是把中间那个取出来，小于中间，放left，否则放右边，然后递归
    if len(arr) < 2:
        return arr
    mid = arr[len(arr) >> 1]
    arr.remove(mid)
    left = []
    right = []
    for i in arr:
        if i < mid:
            left.append(i)
        else:
            right.append(i)
    return quick(left) + [mid] + quick(right)


def merge(left, right):
    l = 0
    r = 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    if r<len(right):
        res.extend(right[r:])
    else:
        res.extend(left[l:])
    return res


def split(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) >> 1
    left = split(arr[:mid])
    right = split(arr[mid:])
    return merge(left, right)


if __name__ == '__main__':
    import random
    import time
    from loguru import logger

    num = [24, 6, 9, 28, 9, 45, 10, 40, 39, 22, 46, 50, 39, 38, 15, 12, 39, 47, 40, 24, 10, 3, 42, 50, 47, 49, 48, 46, 48, 44, 8, 12, 48, 15, 1, 21, 35, 28, 7, 19, 20, 9, 45, 30, 5, 47, 5, 13, 24, 21]
    #bubble(num)
    #bubble_impove(num)
    #select(num)
    # insert(num)
    # t1 = time.time()
    # print(quick(num))
    # t2 = time.time()
    # logger.info("消耗时间：" + str(round(t2-t1, 2)))
    # print(split(num))
    # t3 = time.time()
    # logger.info("消耗时间：" + str(round(t3-t2, 2)))
    heap(num)
