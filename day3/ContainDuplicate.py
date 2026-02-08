arr = [1, 2, 3, 4, 1, 5, 2]


def has_duplicate(nums):
    my_set = set()

    for num in nums:
        if num in my_set:
            return True  # Jaise hi pehla duplicate mila, true return kardo
        my_set.add(num)

    return False  # Poora loop khatam hone par bhi kuch nahi mila


print(has_duplicate(arr))  # Output: True
