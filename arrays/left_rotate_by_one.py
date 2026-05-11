# Problem: Left Rotate Array by One | Difficulty: Easy
# Approach:
#   Optimal : store first element, shift all elements left by one, place stored element at end — O(n)

from typing import List


class Solution:
    def leftRotateByOne(self, nums: List[int]) -> List[int]:

        z = nums[0]

        for x in range(len(nums)-1):
            nums[x] = nums[x+1]
        
        nums[len(nums)-1] = z

        return nums



# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.leftRotateByOne([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]
    assert s.leftRotateByOne([3]) == [3]            # single element
    assert s.leftRotateByOne([1, 2]) == [2, 1]
    print("All tests passed")
