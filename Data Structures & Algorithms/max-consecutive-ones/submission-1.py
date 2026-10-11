class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        counter = 0
        for num in nums:
            if num:
                counter += 1
            else:
                counter = 0

            if counter > maxCount:
                maxCount = counter

        if counter > maxCount:
            maxCount = counter
        return maxCount