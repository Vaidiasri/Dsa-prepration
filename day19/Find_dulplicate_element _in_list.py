nums=[1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
n=len(nums)
freq_count={}
for i in range(n):
    if(nums[i] in freq_count):
        freq_count[nums[i]]+=1
    else:
        freq_count[nums[i]]=1
print(freq_count)

for key,value in freq_count.items():
    if(value>1):
        print(key)

        