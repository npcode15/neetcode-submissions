class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for index, val in enumerate(nums):
            counter[val] = index

        for index, val in enumerate(nums):
            diff = target-val
            if diff in counter and counter.get(diff) != index:
                return [index, counter.get(diff)]

        return []