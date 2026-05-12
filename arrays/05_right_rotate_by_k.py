# Problem: Right Rotate Array by K Places | Difficulty: Easy
# Approach:
#   Brute force : rotate right by one, k times — O(n*k)
#   Better      : store last k elements in new array, then append remaining — O(n) time, O(n) space
#   Optimal     : reverse entire array, reverse first k, reverse remaining — O(n) time, O(1) space

from typing import List


class Solution:
    def rightRotateByK(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums 
        
        k = k % len(nums)

        for x in range(k):

            z = nums[len(nums)-1]

            for y in range(len(nums)-1, 0, -1):
                nums[y] = nums[y-1]

            nums[0] = z 

        return nums

    def rightRotateByKBetter(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums 
        
        k = k % len(nums)

        results = []

        for i in range(len(nums)-k, len(nums)):
            results.append(nums[i])

        for i in range(0, len(nums)-k):
            results.append(nums[i])

        return results
        

    def rightRotateByKOptimal(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums 
        
        k = k % len(nums)
        
        def swap(nums: List[int], left: int, right: int) -> List[int]:

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1

            return nums 
        
       
        swap(nums, 0, len(nums)-1)
        swap(nums, 0, k-1)
        result = swap(nums, k, len(nums)-1)

        return result

        


# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.rightRotateByKOptimal([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert s.rightRotateByKOptimal([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
    assert s.rightRotateByKOptimal([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]   # full rotation
    assert s.rightRotateByKOptimal([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]   # k > len
    print("All tests passed")
