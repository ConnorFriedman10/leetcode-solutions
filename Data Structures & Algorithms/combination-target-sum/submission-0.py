class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #for each number, we have 3 options: include it an repeat, include it an go forward, or ignore it and go forward
        res = []

        def dfs(idx, currlist, currsum):
            if currsum == target:
                res.append(currlist)
                return
            
            if idx >= len(nums) or currsum > target:
                return
            
            # include nums[idx], allow repeating it (stay at idx)
            dfs(idx, currlist + [nums[idx]], currsum + nums[idx])

            # skip nums[idx] entirely, move forward
            dfs(idx+1, currlist, currsum)
            

        dfs(0, [], 0)
        return res


            