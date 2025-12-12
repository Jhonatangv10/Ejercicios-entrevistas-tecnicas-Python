def Triangular_Sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        for x in range(0, len(nums) - 1):
            newNums = []
            for i in range(0, (len(nums) - 1 )):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums 
    return nums[0]

result = Triangular_Sum([1, 3, 5, 7])
print(result)