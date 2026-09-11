class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nset = set()
        for num in nums:
            if num not in nset:
                nset.add(num)
            else:
                return num