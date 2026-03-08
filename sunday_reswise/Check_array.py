arr=[1,2,3,4]
n=len(arr)
def check(arr,n):
  for  i in range(n-1):
    if arr[i]>arr[i+1]:
      return False
  return True
print(check(arr,n))