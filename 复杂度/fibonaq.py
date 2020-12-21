# 方法1：递归


def fib1(n):
    if n in (0, 1):
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)

# 1 + 2 + 4 + 8 +16 = 2^n
# 第一次调用，计算一次，第二次调用，计算2次，第三次调用，计算4次，一次类推。
# 空间复杂度 每次新增两个。


# 方法2：手递手
def fib2(n):
    if n in (0, 1):
        return n
    else:
        first = 0
        second = 1
        third = None
        for i in range(n-1):
            third = first + second
            first = second
            second = third
        return third

# 3+ n*(1+1+1) = o(n)
# 3 + o(1)


# 方法3：动态规划

if __name__ == '__main__':
    print(fib1(10))
    print(fib2(10))


