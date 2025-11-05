class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[1]*len(nums)
        prod=1
        n=len(nums)
        for i in range(1,n):
            arr[i]=arr[i-1]*nums[i-1]
        right=1
        for i in range(n-1,-1,-1):
            arr[i]=arr[i]*right
            right=right*nums[i]
        return arr
            