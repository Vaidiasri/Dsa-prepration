nums=[1,2,3,4,5,6,7,8,9,10]
n=len(nums)
last_element=nums[n-1]
for i in range(n-1, 0, -1):
    nums[i] = nums[i-1]
nums[0] = last_element
print(nums)
    