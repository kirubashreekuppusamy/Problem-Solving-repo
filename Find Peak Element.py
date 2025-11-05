class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        stack=[]
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i]>nums[i-1]:
                    stack.pop()
                    stack.append(nums[i])
        peak_ele=stack[0]
        return nums.index(peak_ele)
            




            
            
        