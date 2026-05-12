# Problem: Find Single Missing Number in Array | Difficulty: Easy
# Given an array of n-1 integers in range [1, n], find the missing number.
# Approach:
#   Brute force : for each number 1 to n, check if it exists in array — O(n^2)
#   Better      : sort the array, check where sequence breaks — O(n log n)
#   Optimal     : use sum formula n*(n+1)/2, subtract array sum — O(n) time, O(1) space

from typing import List


class Solution:

    def missingNumberBrute(self, nums: List[int]) -> int:
        
        for i in range(len(nums)+1):
            found = False
            for j in range(len(nums)):
                if i+1 == nums[j]:
                    found = True
                    break 

            if not found:
                return i+1
            
    def missingNumberSum(self, nums: List[int]) -> int:

        n = len(nums)+1 
        summation = n*(n+1)/2
        sum = 0

        for i in range(len(nums)):
            sum+=nums[i]

        return summation-sum

    def missingNumberHash(self, nums: List[int]) -> int:

        hash = [0]*(len(nums)+2)

        for i in range(len(nums)):
            hash[nums[i]] = 1

        for i in range(1, len(hash)):
            if hash[i]!=1:
                return i 
            
        return -1 

    def missingNumberDiff(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            if nums[i] != i+1:
                return i+1 
            
        return len(nums)+1

    def missingNumberXor(self, nums: List[int]) -> int:

        xor1 = 0
        xor2 = 0 

        for i in range(len(nums)):
            xor1^=nums[i]
            xor2^=i+1 
        
        xor2 = xor2^len(nums)+1 

        return xor1^xor2




# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.missingNumberXor([1, 2, 4, 5]) == 3
    assert s.missingNumberXor([2, 3, 4, 5]) == 1       # missing first
    assert s.missingNumberXor([1, 2, 3, 4]) == 5       # missing last
    assert s.missingNumberXor([1]) == 2                # single element
    print("All tests passed")
