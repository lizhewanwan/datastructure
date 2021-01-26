def quick(nums):
    if len(nums) < 2:
        return nums
    mid = nums[len(nums)//2]
    nums.remove(mid)
    left = []
    right = []
    for i in nums:
        if i < mid:
            left.append(i)
        else:
            right.append(i)
    return quick(left) + [mid] + quick(right)


# 复杂度平均和最坏nlogn
if __name__ == '__main__':
    num = [5, 11, 1, 17, 10, 10, 18, 15, 13, 5, 19, 11, 6, 4, 8, 1, 2, 13, 11, 1]
    print(quick(num))