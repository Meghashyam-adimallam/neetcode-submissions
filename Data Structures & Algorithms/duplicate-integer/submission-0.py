class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        emp = []

        for i in nums:
            if i in emp:
                return True
            else:
                emp.append(i)
        return False