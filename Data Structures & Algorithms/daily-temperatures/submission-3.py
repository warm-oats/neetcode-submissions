class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []

        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                res.append(0)
            else:
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                
                if stack:
                    res.append(stack[-1] - i)
                else:
                    res.append(0)
            
            stack.append(i)
        
        return res[::-1]