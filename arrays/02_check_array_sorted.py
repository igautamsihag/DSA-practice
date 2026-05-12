# Problem: Check if Array is Sorted | Difficulty: Easy
# Approach:
#   Brute force : compare all pairs using nested loops — O(n^2)
#   Optimal     : single pass, check if any element is less than previous — O(n)

from typing import List


class Solution:
    def isSorted(self, nums: List[int]) -> bool:
        
        for x in range(len(nums)-1):
            if nums[x] > nums[x+1]:
                return False
            
        return True


# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.isSorted([1, 2, 3, 4, 5]) == True
    assert s.isSorted([1, 1, 2, 3]) == True     # duplicates allowed
    assert s.isSorted([5, 3, 4, 1]) == False
    assert s.isSorted([1]) == True               # single element
    print("All tests passed")
