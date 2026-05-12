# Problem: Remove Duplicates from Sorted Array | Difficulty: Easy
# Approach:
#   Brute force : use a set to store unique elements, copy back to array — O(n) time, O(n) space
#   Optimal     : two pointers, one slow and one fast — O(n) time, O(1) space

from typing import List


class Solution:

    def removeDuplicatesBrute(self, nums: List[int]) -> int:

        s = set()

        for i in range(len(nums)):
            s.add(nums[i])

        return len(s)

    def removeDuplicates(self, nums: List[int]) -> int:
        
        j = 0 

        for i in range(1, len(nums)):

            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]

        return j+1


# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.removeDuplicatesBrute([1, 1, 2]) == 2
    assert s.removeDuplicatesBrute([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert s.removeDuplicatesBrute([1]) == 1                                # single element
    assert s.removeDuplicatesBrute([1, 2, 3]) == 3                         # no duplicates
    print("All tests passed")
