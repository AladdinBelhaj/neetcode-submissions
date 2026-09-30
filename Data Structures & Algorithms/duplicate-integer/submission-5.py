class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        if len(nums) != len(setNums):
            return True
        else:
            return False


        