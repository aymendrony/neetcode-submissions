class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height)-1
        tall = 0
        while i < j:
            if height[i] <= height[j]:
                tall = max(tall,height[i])
                res+= max(tall - height[i+1], 0)
                i+=1

            else:
                tall = max(tall,height[j])
                res+= max(tall - height[j-1], 0)
                j-=1
        return res 
