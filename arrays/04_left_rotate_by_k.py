# Problem: Left Rotate Array by K Places | Difficulty: Easy
# Approach:
#   Brute force : rotate by one, k times — O(n*k)
#   Better      : store elements from index k onwards in new array, then append first k elements — O(n) time, O(n) space
#   Optimal     : reverse first k, reverse remaining, reverse entire array — O(n) time, O(1) space

from typing import List


class Solution:
    def leftRotateByK(self, nums: List[int], k: int) -> List[int]:

        k = k % len(nums)
        
        for x in range(k):
            z = nums[0]
            for y in range(len(nums)-1):
                nums[y] = nums[y+1]
            
            nums[len(nums)-1] = z

        return nums
    
    def leftRotateByKBetter(self,  nums: List[int], k: int) -> List[int]:

        if len(nums) == k:
            return nums
        
        k = k % len(nums)

        result = []

        for i in range(k, len(nums)):
            result.append(nums[i])

        for i in range(0, k):
            result.append(nums[i])

        return result


    def leftRotateByKOptimal(self, nums: List[int], k: int) -> List[int]:

        k = k % len(nums)

        def swap(nums: List[int], left: int, right: int):

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            
            return nums 
        
        swap(nums, 0, k-1)
        swap(nums, k, len(nums)-1)
        result = swap(nums, 0, len(nums)-1)

        return result


# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.leftRotateByKBetter([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert s.leftRotateByKBetter([1, 2, 3, 4, 5], 1) == [2, 3, 4, 5, 1]
    assert s.leftRotateByKBetter([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]   # full rotation
    assert s.leftRotateByKBetter([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]   # k > len
    print("All tests passed")
