num=[1,2,3,4,5]
left=0
right=len(num)-1
def reverse_list(num,left,right):
  if left>=right:
    return
  num[left],num[right]=num[right],num[left]
  reverse_list(num,left+1,right-1)
reverse_list(num,left,right)
print(num)