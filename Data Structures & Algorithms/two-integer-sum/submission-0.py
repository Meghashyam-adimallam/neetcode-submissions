class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        emp = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in emp:
                return[emp[diff], i]
            else:
                emp[n] = i