# Data Structures and Algorithms (DSA) Learning Journey

A comprehensive 9-day DSA learning program covering fundamental algorithms, array manipulation, and problem-solving techniques.

---

## 📋 Table of Contents

1. [Day 1: Max-Min in Array](#day-1-max-min-in-array)
2. [Day 2: Array Reversal](#day-2-array-reversal)
3. [Day 3: Duplicate Detection & Removal](#day-3-duplicate-detection--removal)
4. [Day 4: Chocolate Distribution Problem](#day-4-chocolate-distribution-problem)
5. [Day 5: Count Digits](#day-5-count-digits)
6. [Day 6: Palindrome Check](#day-6-palindrome-check)
7. [Day 7: Armstrong Number](#day-7-armstrong-number)
8. [Day 8: Frequency Counting](#day-8-frequency-counting)
9. [Day 9: Advanced Frequency Mapping](#day-9-advanced-frequency-mapping)
10. [Day 10: Basic Recursion](#day-10-basic-recursion)
11. [Day 11: Recursion Patterns](#day-11-recursion-patterns)
12. [Day 12: Factorial using Recursion](#day-12-factorial-using-recursion)
13. [Day 13: Recursive List Reversal](#day-13-recursive-list-reversal)
14. [Day 14: Selection Sort](#day-14-selection-sort)
15. [Day 15: Bubble Sort](#day-15-bubble-sort)
16. [Day 16: Insertion Sort](#day-16-insertion-sort)
17. [Day 17: Merge Sort](#day-17-merge-sort)
18. [Day 18: Quick Sort](#day-18-quick-sort)
19. [Day 19: Duplicate Elements in List](#day-19-duplicate-elements-in-list)
20. [Day 20: Right Rotate Array by 1](#day-20-right-rotate-array-by-1)
21. [Day 21: Rotate Array by K](#day-21-rotate-array-by-k)

---

## Day 1: Max-Min in Array

**File:** `day1/MaxMin.py`

**Concept:** Finding the maximum and minimum values in an array using a single loop iteration.

**Key Points:**

- Iterate through the array starting from index 1
- Maintain two variables: `max_val` and `min_val`
- Compare each element and update accordingly
- Time Complexity: O(n) | Space Complexity: O(1)

**Example:**

```
Input: [12, 3, 4, 16, 2]
Output: Max: 16, Min: 2
```

---

## Day 2: Array Reversal

**Files:** `day2/Reverse.py`, `day2/TwoPointer.py`

**Concept:** Reversing an array using two different approaches.

### Approach 1: Using Auxiliary Array

- Create a new list and append elements in reverse order
- Time Complexity: O(n) | Space Complexity: O(n)

### Approach 2: Two-Pointer Technique (In-Place)

- Use left and right pointers
- Swap elements and move pointers towards center
- Time Complexity: O(n) | Space Complexity: O(1)
- **Recommended:** More efficient as it modifies array in-place

**Example:**

```
Input: [2, 1, 4, 5]
Output: [5, 4, 1, 2]
```

---

## Day 3: Duplicate Detection & Removal

**Files:** `day3/ContainDuplicate.py`, `day3/RemoveDuplicate.py`

**Concept:** Detecting and removing duplicate elements from an array.

### Duplicate Detection

- Use a set to track seen elements
- Return True on first duplicate found
- Time Complexity: O(n) | Space Complexity: O(n)

### Duplicate Removal

- Convert array to set to remove duplicates
- Automatically handles duplicate elimination
- Time Complexity: O(n) | Space Complexity: O(n)

**Example:**

```
Input: [1, 2, 3, 4, 1, 5, 2]
Duplicates Found: True
Unique Elements: {1, 2, 3, 4, 5}
```

---

## Day 4: Chocolate Distribution Problem

**File:** `day4/ChocolateD.py`

**Concept:** Distributing chocolates to students while minimizing the difference between maximum and minimum packets.

**Algorithm:**

1. Sort the array
2. Use sliding window of size m
3. Find the window with minimum difference (last - first element)

**Approach:**

- Sorting ensures consecutive elements have minimal difference
- Sliding window technique: O(n - m + 1)
- Time Complexity: O(n log n) | Space Complexity: O(1)

**Example:**

```
Input: arr = [2, 4, 15, 1, 3, 8], m = 3
Output: Minimum Difference = 2
Explanation: Choose [1, 2, 3] or [3, 4, 5]
```

---

## Day 5: Count Digits

**File:** `day5/Count.py`

**Concept:** Counting the total number of digits in an integer.

**Algorithm:**

1. Handle edge case: if number is 0, count = 1
2. Use integer division by 10 repeatedly
3. Increment counter each iteration

**Time Complexity:** O(log n) | Space Complexity: O(1)

**Example:**

```
Input: 4555
Output: 4 digits
```

---

## Day 6: Palindrome Check

**File:** `day6/palindorme.py`

**Concept:** Checking if a number is a palindrome (reads same forwards and backwards).

**Algorithm:**

1. Extract last digit using modulo (%)
2. Build reversed number by appending digits
3. Compare original with reversed number

**Time Complexity:** O(log n) | Space Complexity: O(1)

**Example:**

```
Input: 121
Output: Palindrome

Input: 123
Output: Not a Palindrome
```

---

## Day 7: Armstrong Number

**File:** `day7/Almstrong.py`

**Concept:** Identifying Armstrong numbers (narcissistic numbers where sum of digits raised to power of digit count equals the number).

**Definition:**

- An n-digit number is Armstrong if: digit₁^n + digit₂^n + ... + digitₙ^n = original number

**Examples:**

- 153 is Armstrong: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
- 9474 is Armstrong: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474

**Time Complexity:** O(log n) | Space Complexity: O(1)

---

## Day 8: Frequency Counting

**File:** `day8/frequerncy.py`

**Concept:** Counting the frequency of each element in an array using a dictionary.

**Algorithm:**

1. Create an empty dictionary
2. Iterate through array
3. If element exists, increment count; else initialize to 1
4. Return frequency map

**Time Complexity:** O(n) | Space Complexity: O(k) where k is unique elements

**Example:**

```
Input: [1,2,3,4,5,5,5,6,6,7]
Output: {1:1, 2:1, 3:1, 4:1, 5:3, 6:2, 7:1}
```

---

## Day 9: Advanced Frequency Mapping

**File:** `day9/frequercymap.py`

**Concept:** Using array-based hash mapping for efficient frequency queries.

**Algorithm:**

1. Create hash array of size (max_element + 1)
2. Store frequency count at each index
3. Query frequency in O(1) time

**Advantages:**

- Constant time lookups O(1)
- Better performance for range queries
- Suitable when element range is known and bounded

**Time Complexity:**

- Setup: O(n)
- Queries: O(1)
- Space Complexity: O(max_element)

**Example:**

```
Input Array: [1, 3, 2, 4, 5, 5, 1, 6]
Hash Map: [0, 2, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0]
Query 5: Output = 2
```

---

## Day 10: Basic Recursion

**File:** `day10/recursion.py`

**Concept:** Introduction to recursion by printing numbers from 1 to N.

**Key Points:**

- Base case: `if i > n: return`
- Recursive step: `func(i + 1, n)`
- Understanding stack calls and termination conditions.

---

## Day 11: Recursion Patterns

**Files:** `day11/ParaRecursion.py`, `day11/FunctionalRecursion.py`

**Concept:** Comparing Parameterized and Functional recursion styles.

### Parameterized Recursion

- Passing results as parameters (e.g., passing `sum` to the next call).
- Useful for tail-recursion-like patterns.

### Functional Recursion

- Function returns a value that is used by the caller.
- Example: `return n + func(n-1)`

---

## Day 12: Factorial using Recursion

**File:** `day12/Factorial.py`

**Concept:** Calculating the factorial of a number using the functional recursion pattern.

**Formula:** `n! = n * (n-1)!`

**Complexity:**

- Time Complexity: O(n)
- Space Complexity: O(n) (Recursion stack)

---

## Day 13: Recursive List Reversal

**File:** `day13/Reverse_an_list_by_recursion.py`

**Concept:** Reversing an array using recursion instead of iterative loops.

**Approach:**

- Use two pointers (left, right).
- Swap elements at `num[left]` and `num[right]`.
- Recursively call for `left+1` and `right-1`.
- Base case: `left >= right`.

---

## Day 14: Selection Sort

**File:** `day14/Selection_sort.py`

**Concept:** A comparison-based sorting algorithm that repeatedly selects the minimum element from the unsorted part and puts it at the beginning.

**Algorithm:**

1. Find the minimum element in the unsorted array.
2. Swap it with the first element of the unsorted part.
3. Move the boundary between sorted and unsorted parts.

**Complexity:**

- Time Complexity: O(n²)
- Space Complexity: O(1)

---

## Day 15: Bubble Sort

**File:** `day15/Bubble_Sort.py`

**Concept:** A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

**Algorithm:**

1. Compare adjacent elements.
2. If the first is greater than the second, swap them.
3. Repeat for all elements in the array.
4. Continue until the array is sorted.

**Complexity:**

- Time Complexity: O(n²)
- Space Complexity: O(1)

---

## Day 16: Insertion Sort

**File:** `day16/insertion_sort.py`

**Concept:** A straightforward sorting algorithm that builds the final sorted array one element at a time, moving each element to its correct position within the already sorted part of the array.

**Algorithm:**

1. Iterate from the second element (index 1) to the end of the array.
2. Compare the current element (key) to its predecessors.
3. Shift all elements greater than the key one position to the right to make space.
4. Insert the key into its correct position.

**Complexity:**

- Time Complexity: O(n²) worst and average case; O(n) best case
- Space Complexity: O(1)

---

## Day 17: Merge Sort

**Files:** `day17/merge_sort.py`, `day17/merge_two_array.py`

**Concept:** A divide-and-conquer sorting algorithm that divides the array into halves, sorts them recursively, and then merges the sorted halves.

**Algorithm:**

1. **Divide:** Find the middle point to divide the array into two halves.
2. **Conquer:** Recursively sort both halves using Merge Sort.
3. **Combine:** Merge the two sorted halves into a single sorted array using a helper function.

**Helper Function (`merge_two_array.py`):**

- Uses two pointers to compare elements from both arrays and builds a sorted result.

**Complexity:**

- Time Complexity: O(n log n) in all cases (best, average, worst).
- Space Complexity: O(n) due to auxiliary space used for merging.

---

## Day 18: Quick Sort

**File:** `day18/Quick_sort.py`

**Concept:** A highly efficient divide-and-conquer sorting algorithm that picks an element as 'pivot' and partitions the given array around the picked pivot.

**Algorithm:**

1. Pick an element (pivot) from the array.
2. Partitioning: Reorder the array so that all elements with values less than the pivot come before the pivot, and all elements with values greater than the pivot come after it.
3. Recursively apply the above steps to the sub-arrays of elements with smaller and larger values.

**Complexity:**

- Time Complexity: O(n log n) average; O(n²) worst case.
- Space Complexity: O(log n) for recursive stack.

---

## Day 19: Duplicate Elements in List

**File:** `day19/Find_dulplicate_element _in_list.py`

**Concept:** Identifying duplicate elements in a list using a frequency map (dictionary) for optimal performance.

**Algorithm:**

1. Initialize an empty dictionary for frequency counting.
2. Iterate through the list, updating the count for each element in the dictionary.
3. Iterate through the dictionary and identify keys with a value greater than 1.

**Complexity:**

- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Day 20: Right Rotate Array by 1

**File:** `day20/Right_Rotate_Array_by_1.py`

**Concept:** Rotating an array to the right by one position, where the last element moves to the first position.

**Algorithm:**

1. Store the last element of the array.
2. Iterate from the end to the beginning (backwards), shifting each element one position to the right.
3. Place the stored last element at the first position (index 0).

**Complexity:**

- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Day 21: Rotate Array by K

**File:** `day21/k_place.py`

**Concept:** Rotating an array to the right by `k` positions using an efficient in-place algorithm.

**Algorithm:**

1.  Reverse the entire array.
2.  Reverse the first `k` elements.
3.  Reverse the remaining `n-k` elements.

**Why this works:** It achieves O(1) space complexity by performing in-place reversals. Reversing the whole array moves the last `k` elements to the front (though in reverse order), and then reversing the sub-segments corrects their orientation.

**Complexity:**

- Time Complexity: O(n)
- Space Complexity: O(1)

---

## 📊 Learning Progress Summary

| Day | Topic                  | Difficulty  | Concepts Covered            |
| --- | ---------------------- | ----------- | --------------------------- |
| 1   | Max-Min                | ⭐ Easy     | Linear Iteration            |
| 2   | Array Reversal         | ⭐ Easy     | Two-Pointer, In-place swap  |
| 3   | Duplicates             | ⭐⭐ Medium | Set, Hash Set, Logic        |
| 4   | Chocolate Distribution | ⭐⭐ Medium | Sorting, Sliding Window     |
| 5   | Count Digits           | ⭐ Easy     | Mathematical Operations     |
| 6   | Palindrome             | ⭐⭐ Medium | Number Manipulation         |
| 7   | Armstrong Number       | ⭐⭐ Medium | Power Operations            |
| 8   | Frequency Counting     | ⭐⭐ Medium | Dictionary/HashMap          |
| 9   | Frequency Mapping      | ⭐⭐⭐ Hard | Array Hashing, Optimization |
| 10  | Basic Recursion        | ⭐ Easy     | Recursion Basics            |
| 11  | Recursion Patterns     | ⭐⭐ Medium | Parameterized vs Functional |
| 12  | Factorial              | ⭐ Easy     | Recursive Math              |
| 13  | Recursive Reversal     | ⭐⭐ Medium | Pointer manipulation        |
| 14  | Selection Sort         | ⭐⭐ Medium | Sorting Algorithms          |
| 15  | Bubble Sort            | ⭐⭐ Medium | Sorting Algorithms          |
| 16  | Insertion Sort         | ⭐⭐ Medium | Sorting Algorithms          |
| 17  | Merge Sort             | ⭐⭐⭐ Hard | Divide and Conquer, Sorting |
| 18  | Quick Sort             | ⭐⭐⭐ Hard | Divide and Conquer, Pivot   |
| 19  | Duplicate Elements     | ⭐⭐ Medium | Frequency Counting, Map     |
| 20  | Right Rotate Array     | ⭐⭐ Medium | Array Manipulation, Shifting |
| 21  | Rotate Array by K      | ⭐⭐ Medium | Array Reversal, In-place     |

---

## 🎯 Key Concepts Learned

### Data Structures

- Arrays
- Dictionaries/HashMaps
- Sets
- Hash Arrays

### Algorithms & Techniques

- Linear Iteration
- Two-Pointer Technique
- Sliding Window
- Sorting
- Hashing
- Frequency Counting

### Computational Complexity

- Time Complexity Analysis (O(n), O(log n), O(1))
- Space Complexity Optimization
- Trade-offs between speed and memory

---

## 🚀 How to Use This Repository

### Prerequisites

- Python 3.6+
- Basic understanding of arrays and loops

### Running the Programs

```bash
# Navigate to specific day folder
cd day1

# Run the Python script
python MaxMin.py
```

### Structure

```
DDSA/
├── day1/
│   └── MaxMin.py
├── day2/
│   ├── Reverse.py
│   └── TwoPointer.py
├── day3/
│   ├── ContainDuplicate.py
│   └── RemoveDuplicate.py
├── day4/
│   └── ChocolateD.py
├── day5/
│   └── Count.py
├── day6/
│   └── palindorme.py
├── day7/
│   └── Almstrong.py
├── day8/
│   └── frequerncy.py
├── day9/
│   └── frequercymap.py
├── day10/
│   └── recursion.py
├── day11/
│   ├── FunctionalRecursion.py
│   └── ParaRecursion.py
├── day12/
│   └── Factorial.py
├── day13/
│   └── Reverse_an_list_by_recursion.py
├── day14/
│   ├── Selection_sort.py
│   └── test_selection_sort.py
├── day15/
│   └── Bubble_Sort.py
├── day16/
│   └── insertion_sort.py
├── day17/
│   ├── merge_sort.py
│   └── merge_two_array.py
├── day18/
│   └── Quick_sort.py
├── day19/
│   └── Find_dulplicate_element _in_list.py
├── day20/
│   └── Right_Rotate_Array_by_1.py
├── day21/
│   └── k_place.py
└── README.md (This file)
```

---

## 💡 Tips for Further Learning

1. **Practice:** Try solving variations of each problem
2. **Optimize:** Attempt to improve time/space complexity
3. **Document:** Add comments explaining your logic
4. **Test:** Create test cases with edge cases
5. **Review:** Compare your solutions with others

---

## 📚 Related Topics to Explore

- Advanced Sorting Algorithms (Merge Sort, Quick Sort)
- Searching Techniques (Binary Search)
- Dynamic Programming
- Graph Algorithms
- Tree Traversals

---

## 📝 License

This learning material is created for educational purposes.

---

## 🤝 Contribution

Feel free to add improvements, optimizations, or additional problems to enhance this DSA learning resource.

---

**Last Updated:** March 24, 2026

**Status:** ✅ Complete - 21 Days DSA Journey Tracked
