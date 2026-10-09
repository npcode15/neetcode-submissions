class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCounter = {}
        for num in nums:
            if numCounter.get(num, False):
                return True
            else:
               numCounter[num] = 1
        
        return False