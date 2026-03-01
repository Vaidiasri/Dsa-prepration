from Selection_sort import SelectionSort

def test_selection_sort():
    test_cases = [
        ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([5], [5]),
        ([5, 2, 5, 1], [1, 2, 5, 5])
    ]
    
    for arr, expected in test_cases:
        sorter = SelectionSort(list(arr)) # Use a copy since SelectionSort sorts in-place
        result = sorter.selection_sort()
        assert result == expected, f"Failed for {arr}: expected {expected}, got {result}"
        print(f"Passed: {arr} -> {result}")

if __name__ == "__main__":
    test_selection_sort()
