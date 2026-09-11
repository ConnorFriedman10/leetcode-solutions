class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(idx, twice):     
            if idx >= len(nums):
                res.append(twice) 
                return
            recur(idx+1, twice)
            recur(idx+1, twice + [nums[idx]])

        recur(0, [])
        return res