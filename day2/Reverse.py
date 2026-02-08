arr = [2, 1, 4, 5]
dup = []

def reverse(arr, dup):
    for i in range(len(arr) - 1, -1, -1):
        dup.append(arr[i])
    print(dup)

reverse(arr, dup)
