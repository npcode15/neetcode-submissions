class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
                continue
            elif counter > maxCount:
                maxCount = counter

            counter = 0

        if counter > maxCount:
            maxCount = counter
        return maxCount