# print 1 to n using recursion
def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)  # Increment i instead of decrementing n

func(1, 15)  # Now it works correctly