

def selection(arr): # 选择排序就是选一个最小的，然后更新这个最小的，把最小的放到第一位 平均复杂度和冒泡一样是o（n2）

    l = len(arr)
    for i in range(l): # 第i个，跟第i+1个之后的比，选一个最小的
        min_index = i
        for j in range(i+1,l):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    print(arr)


# 复杂度平均和最坏on2
if __name__ == '__main__':
    num = [5, 11, 1, 17, 10, 10, 18, 15, 13, 5, 19, 11, 6, 4, 8, 1, 2, 13, 11, 1]
    selection(num)