class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = i+1
        max_count = 0 
        for x in dict:
            count = 0
            while x in dict:
                count+=1
                x+=1
            max_count = max(max_count, count)

        return max_count