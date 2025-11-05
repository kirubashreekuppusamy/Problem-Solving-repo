class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val=0
        cur_val=0
        for num in nums:
            cur_val+=num
            min_val=min(min_val,cur_val)
        return 1-min_val
        