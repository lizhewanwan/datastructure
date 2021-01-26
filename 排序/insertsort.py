def insert(arr):  # 扑克牌排序,手里从第一张牌开始，没抽一张牌，都跟之前的比
    l = len(arr)
    for i in range(1, l):
        cur = i  # 新摸得一张牌
        for j in range(i - 1, -1, -1):
            if arr[cur] < arr[j]:
                arr[j], arr[cur] = arr[cur], arr[j]
                cur = j
            else:
                break
    print(arr)


# 优化1，先把新模的一张牌备份一下，不用每一步都替换
def insert1(arr):
    for i in range(1,len(arr)):
        cur = i
        cur_val = arr[cur]
        for j in range(i-1,-1,-1):
            if cur_val < arr[j]:
                arr[cur] = arr[j]
                cur -= 1
        arr[cur] = cur_val

    print(arr)


def insert2(arr): # 插入排序可以用二分搜索优化,找右侧边界
    def search(index):
        left = 0
        right = index
        while left < right:
            mid = (left + right) >> 2
            if arr[mid] < arr[right]:
                right = mid

            else:
                left += 1
        return left
    for i in range(1,len(arr)):
        dest = search(i)
        val = arr[dest]
        cur = i
        arr_cur = arr[cur]
        for j in range(dest,-1,-1):
            if arr[j] > arr[cur]:
                arr[cur] = arr[j]
                cur -= 1
        arr[cur] = arr_cur

    print(arr)
if __name__ == '__main__':
    num = [5, 11, 1, 17, 10, 10, 18, 15, 13, 5, 19, 11, 6, 4, 8, 1, 2, 13, 11, 1]
    insert2(num)
