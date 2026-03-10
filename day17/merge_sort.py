from merge_two_array import merge_two_array

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge_two_array(left,right)

arr=[1,3,5,7,2,4,6,8]
print(merge_sort(arr))