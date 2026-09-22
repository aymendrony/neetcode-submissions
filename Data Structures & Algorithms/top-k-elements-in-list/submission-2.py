class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = Counter(nums)  
        sorted_items = sorted(dict_nums.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]