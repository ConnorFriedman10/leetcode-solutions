class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        nums = list(set(nums))
        nums.sort()
        conslist = []
        currlist = [nums[0]]
        for num in nums[1:]:
            if num - currlist[-1] == 1:
                currlist.append(num)
            else:
                conslist.append(currlist)
                currlist = [num]
        conslist.append(currlist)
        return max([len(x) for x in conslist])
            

            
        