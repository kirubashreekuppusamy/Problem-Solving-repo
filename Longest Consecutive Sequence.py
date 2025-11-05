class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset=set(nums)
        longest=0
        for num in nums:
            if num-1 not in nset:
                current=num
                count=1
                while current+1 in nset:
                    current=current+1
                    count+=1
                longest=max(longest,count)
        return longest