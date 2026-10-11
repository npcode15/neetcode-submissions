class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxArr = [0]*len(arr)
        maxArr[len(arr) - 1] = -1

        rightMax = arr[len(arr) - 1]
        for index in range(len(arr) - 2, -1, -1):
            maxArr[index] = rightMax

            if arr[index] > rightMax:
                rightMax = arr[index]

        return maxArr