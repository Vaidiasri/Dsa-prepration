def merge_two_array(left,right):
    result=[]
    i=j=0
    n,m=len(left),len(right)
    while(i<n and j<m):
        if(left[i]<=right[j]):
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    if(i<n):
        while(i<n):
            result.append(left[i])
            i=i+1
    if(j<m):
        while(j<m):
            result.append(right[j])
            j=j+1
    return result

if __name__ == "__main__":
    left=[1,3,5,7]
    right=[2,4,6,8]
    print(merge_two_array(left,right))
    