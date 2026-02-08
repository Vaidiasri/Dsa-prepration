arr = [2, 1, 4, 5]


def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap values
        arr[left], arr[right] = arr[right], arr[left]

        # Move pointers
        left += 1
        right -= 1

    print("Reversed Array:", arr)


reverse_in_place(arr)
