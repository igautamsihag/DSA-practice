# Problem: Second Largest Element | Difficulty: Easy
# Approach:
#   Brute force : sort array and iterate backwards to find second unique element — O(n log n)
#   Better      : iterate twice — first pass finds largest, second pass finds largest excluding first — O(n)
#   Optimal     : single pass using if/else to track first and second largest simultaneously — O(n)

from typing import List


class Solution:
    def secondLargest(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return None

        first_largest = float('-inf')
        second_largest = float('-inf')

        for x in nums:
            if x > first_largest:
                second_largest = first_largest
                first_largest = x 
            elif x > second_largest and x != first_largest:
                second_largest = x 

        return second_largest


# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.secondLargest([1, 2, 3, 4, 5]) == 4
    assert s.secondLargest([5, 5, 4]) == 4
    assert s.secondLargest([1]) is None          # only one element
    print("All tests passed")
