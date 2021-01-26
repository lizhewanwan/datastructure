def bubble(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(i + 1, l):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


def bubble1(arr):
    # 第一个跟第二个比
    # 一共比l-1次
    l = len(arr)
    flag = True  # 用一个标志优化
    for i in range(l - 1):
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag == True:
            break
    print(arr)


def bubble2(arr):
    # 第一个跟第二个比
    # 一共比l-1次
    l = len(arr)
    start = 0  # 从这里往后就不用比了，因为这以后，就最大了。
    end = l - 1
    for i in range(l - 1):
        for j in range(end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                start = j
        end = start
    print(arr)

# 最坏，平均复杂度为on2


if __name__ == '__main__':
    num = [5, 11, 1, 17, 10, 10, 18, 15, 13, 5, 19, 11, 6, 4, 8, 1, 2, 13, 11, 1]
    bubble2(num)
