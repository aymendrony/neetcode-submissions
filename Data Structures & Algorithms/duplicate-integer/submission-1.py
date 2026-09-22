class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        res = {}
        for i in range(n):
            if nums[i] not in res.keys():
                res[nums[i]] = 1
            else:
                return True
        return False