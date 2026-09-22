class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] not in res:
                res.append(nums[i])
        return len(res) != len(nums)