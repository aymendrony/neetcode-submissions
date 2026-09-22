class Solution:
    def climbStairs(self, n: int) -> int:
        results = [1,2]
        for i in range(n-1):
            results.append(int(results[i]+results[i+1]))
        return results[n-1]