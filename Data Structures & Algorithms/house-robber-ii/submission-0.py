class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        nums_1 = nums[:len(nums)-1]
        nums_2 = nums[1:]
        res_1 = [0]*(len(nums)-1)
        res_1[0] = nums_1[0]
        res_1[1] = max(nums_1[0], nums_1[1])
        res_2 = [0]*(len(nums)-1)
        res_2[0] = nums_2[0]
        res_2[1] = max(nums_2[0], nums_2[1])
        for i in range(2, len(nums)-1):
            res_1[i] = max(res_1[i-1], res_1[i-2] + nums_1[i])
            res_2[i] = max(res_2[i-1], res_2[i-2] + nums_2[i])
        return max(res_1[len(nums)-2], res_2[len(nums)-2])