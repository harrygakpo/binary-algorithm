def find_value(list, value):
    high = len(list)
    low = 0
    mid = (high + low)// 2
    while low <= high:
        if mid > value:
            high = mid
        elif mid < value:
            low = mid
        else:
            return mid

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = find_value(nums, 8)
print(index)