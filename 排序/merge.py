def merge(left,right):
    c = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            c.append(left[l])
            l += 1
        else:
            c.append(right[r])
            r+= 1
    if l < len(left):
        c.extend(left[l:])
    else:
        c.extend(right[r:])
    return c


def split(arr):
    if len(arr)<2:
        return arr
    else:
        mid = len(arr)//2
        left = split(arr[:mid])
        right = split(arr[mid:])
    return merge(left,right)




if __name__ == '__main__':
    num = [5, 11, 1, 17, 10, 10, 18, 15, 13, 5, 19, 11, 6, 4, 8, 1, 2, 13, 11, 1]
    print(split(num))