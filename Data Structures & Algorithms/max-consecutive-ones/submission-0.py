class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maximum = 0
        for val in nums:
            if val == 1:
                current += 1
                if current > maximum:
                    maximum = current
            else:
                current = 0
        return maximum