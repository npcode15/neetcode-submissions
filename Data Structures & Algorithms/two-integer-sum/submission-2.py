class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for index, val in enumerate(nums):
            diff = target-val
            if diff in counter:
                return [counter.get(diff), index]
            
            counter[val] = index

        return []