class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tupleset = set()

        def recur(idx, twice):     
            if idx >= len(nums):
                twice = sorted(twice)
                if tuple(twice) not in tupleset:
                    res.append(twice)
                    tupleset.add(tuple(twice))
                return

            recur(idx+1, twice)
            recur(idx+1, twice + [nums[idx]])

        recur(0, [])
        return res