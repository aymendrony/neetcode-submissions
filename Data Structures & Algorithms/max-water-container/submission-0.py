class Solution:
    def maxArea(self, heights: List[int]) -> int:
        air_max = 0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                air_current = (j-i) * min(heights[i], heights[j])
                air_max = max(air_max, air_current)
        return air_max 