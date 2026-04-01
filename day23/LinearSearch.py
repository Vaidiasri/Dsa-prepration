nums=[1, 2, 3, 4, 5]
target=4
def LinearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

result = LinearSearch(nums, target)
print(result)