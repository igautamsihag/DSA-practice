# Problem: Move Zeroes to End | Difficulty: Easy
# Approach:
#   Brute force : collect non-zero elements in new array, fill remaining with zeroes — O(n) time, O(n) space
#   Optimal     : two pointers, swap non-zero elements to front — O(n) time, O(1) space

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        
        non_zero = []

        for i in range(len(nums)):
            if nums[i]!=0:
                non_zero.append(nums[i])
        
        for i in range(len(non_zero), len(nums)):
            non_zero.append(0)

        return non_zero
    
    def moveZeroesOptimal(self, nums: List[int]) -> List[int]:

        i = 0 

        for j in range(len(nums)):

            if nums[j]!=0:
                nums[i],  nums[j] = nums[j], nums[i]
                i+=1

        return nums


# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.moveZeroesOptimal([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert s.moveZeroesOptimal([0, 0, 1]) == [1, 0, 0]
    assert s.moveZeroesOptimal([1, 2, 3]) == [1, 2, 3]       # no zeroes
    assert s.moveZeroesOptimal([0, 0, 0]) == [0, 0, 0]       # all zeroes
    assert s.moveZeroesOptimal([1]) == [1]                    # single element
    print("All tests passed")
