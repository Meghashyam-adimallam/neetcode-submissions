class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        emp = {}
        lt = []

        for word in strs:
            key = ''.join(sorted(word))
            if key not in emp:
                emp[key] = []
            emp[key].append(word)
        return list(emp.values())