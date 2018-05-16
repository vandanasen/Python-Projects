#Two sum
def two_sum():
    nums = [2, 7, 11, 15]
    target = 13
    num_dict = {}
    for i, num in enumerate(nums):
        print(num)
        if num in num_dict:
            return [num_dict[num], i]
        num_dict[target - num] = i

    return [-1, -1]
    print(num_dict)
two_sum()