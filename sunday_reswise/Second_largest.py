# arr=[10,5,20,8]

# def second_largest(arr):
#     n=len(arr)

#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

#     return arr[n-2]

# print(second_largest(arr))
# this is the code for second largest element in an array using bubble sort algorithm. The time complexity of this algorithm is O(n^2) and space complexity is O(1).
arr=[10,5,20,8]
def second_largest(arr):
    n=len(arr)
    largest=float("-inf")
    second_largest=float("-inf")

    for i in range(0,n):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest=arr[i]

    return second_largest
print(second_largest(arr))