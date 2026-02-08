arr = [2, 4, 15, 1, 3, 8]
m = 3


def chocolate_distribution(arr, m):
    n = len(arr)

    # Step 1: Sort the array (Essential for finding min difference)
    arr.sort()

    # Step 2: Initialize min with a very large number
    min_diff = float("inf")

    # Step 3: Loop through the array to find the window
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]  # Last - First element of window

        if diff < min_diff:
            min_diff = diff

    return min_diff  # Loop khatam hone ke baad final answer return karo


print("Minimum Difference:", chocolate_distribution(arr, m))
