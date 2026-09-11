class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums[::-1]
        
        forward = [1]
        backward = [1]
        for idx, num in enumerate(nums):
            if idx != 0:
                forward.append(nums[idx-1] * forward[-1])
                backward.append(nums[idx*-1] * backward[-1])

        exself = []
        for num1, num2 in zip(forward, backward[::-1]):
            exself.append(num1 * num2)
        
        return(exself)
        