class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        flen=len(num) - k
        for c in num:
            while stack and k and stack[-1]>c:
                stack.pop()
                k=k-1
            stack.append(c)
        return ''.join(stack[:flen]).lstrip('0') or '0'