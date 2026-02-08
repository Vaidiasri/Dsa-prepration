arr = [12, 3, 4, 16, 2]

def max_min(arr):
    if not arr:
        return
    max_val = arr[0]
    min_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    print("Max:", max_val)
    print("Min:", min_val)

max_min(arr)
