def erfen(li, target):
    left = 0
    right = len(li) - 1
    while left <= right:  # 用while循环一定看终止条件
        mid = (left + right) // 2
        if li[mid] == target:
            return mid
        elif li[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def zuocebianjie(li, target):  # 目标值右边那个
    if len(li) == 0:
        return -1
    left = 0
    right = len(li)  # 注意
    while left < right:  # 注意
        mid = (left + right) // 2
        if li[mid] >= target:
            right = mid
        else:
            left = mid + 1

    if left == len(li):
        return -1
    return left


def youcebianjie(li, target):  # 目标值左边那个
    if len(li) == 0: return -1
    left = 0
    right = len(li)
    while left < right:
        mid = (left + right) // 2
        if li[mid] <= target:
            left = mid + 1
        else:
            right = mid
    if left == 0: return -1
    return left


if __name__ == '__main__':
    import numpy as np

    li = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 777, 888, 999]
    print(li)
    # print(li[10])
    # print(erfen(li, li[10]))
    # print(zuocebianjie(li, 1))
    print(youcebianjie(li, 4))
