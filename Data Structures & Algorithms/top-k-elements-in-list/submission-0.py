class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        emp = {}

        for num in nums:
            emp[num] = emp.get(num, 0) + 1
        sort = sorted(emp.items(), key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sort[i][0])
        return res
    