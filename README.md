# DSA Practice in Python

A collection of Data Structures & Algorithms problems solved in Python. Each solution is written as a **self-contained tutorial** — covering problem statement, multiple approaches from brute force to optimal, time complexity, and test cases.

Use this repo to learn how to think through a problem step by step, not just memorize solutions.

---

## How to Read a Solution File

Every file follows the same structure:

```python
# Problem: <name> | Difficulty: <Easy/Medium/Hard>
# Approach:
#   Brute force : <explanation> — O(?)
#   Better      : <explanation> — O(?)
#   Optimal     : <explanation> — O(?)

class Solution:
    def bruteForce(self, nums): ...
    def better(self, nums): ...
    def optimal(self, nums): ...

# --- Tests ---
```

**Start by reading the approaches** at the top before looking at the code. Try to implement it yourself first, then compare with the solution.

## How to Run a Solution

```bash
python arrays/01_second_largest_element.py
```

If all test cases pass, you'll see:
```
All tests passed
```

---

## Problems

### Arrays

| # | Problem | Difficulty | Approaches |
|---|---------|------------|------------|
| 01 | [Second Largest Element](arrays/01_second_largest_element.py) | Easy | Brute force → Optimal |
| 02 | [Check Array Sorted](arrays/02_check_array_sorted.py) | Easy | Brute force → Optimal |
| 03 | [Left Rotate by One](arrays/03_left_rotate_by_one.py) | Easy | Optimal |
| 04 | [Left Rotate by K](arrays/04_left_rotate_by_k.py) | Easy | Brute force → Better → Optimal |
| 05 | [Right Rotate by K](arrays/05_right_rotate_by_k.py) | Easy | Brute force → Better → Optimal |
| 06 | [Remove Duplicates from Sorted Array](arrays/06_remove_duplicates_sorted_array.py) | Easy | Brute force → Optimal |
| 07 | [Move Zeroes to End](arrays/07_move_zeroes_to_end.py) | Easy | Brute force → Optimal |
| 08 | [Find Missing Number](arrays/08_missing_number.py) | Easy | Brute force → Sum → Hash → Diff → XOR |

---

## How to Use This Repo to Learn

1. **Pick a problem** from the table above
2. **Read the approaches** section at the top of the file
3. **Try to code it yourself** before reading the solution
4. **Run the tests** to verify — `python arrays/<filename>.py`
5. **Compare your solution** with the implementations in the file

---

## Topics Covered

- [Arrays](arrays/)
- Strings *(coming soon)*
- Linked List *(coming soon)*
- Trees *(coming soon)*
- Dynamic Programming *(coming soon)*
