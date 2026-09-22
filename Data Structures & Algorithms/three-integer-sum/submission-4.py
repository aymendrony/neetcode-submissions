class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for k in range(len(nums)):
            target = -nums[k]
            i = 0
            j = len(nums)-1
            while i<j :
                somme = nums[i] +nums[j]
                if somme == target and i!=k and j!=k and sorted([nums[i], nums[j],nums[k]]) not in res:
                    res.append(sorted([nums[i], nums[j],nums[k]]))
                if somme < target:
                    i+=1
                else:
                    j-=1
        return res 


