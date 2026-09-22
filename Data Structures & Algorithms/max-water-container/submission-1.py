class Solution:
    def maxArea(self, heights: List[int]) -> int:
        air_max = 0
        i = 0
        j = len(heights)-1
        while i < j:
            air_current = (j-i)* min(heights[i],heights[j])
            air_max = max(air_max,air_current)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return air_max