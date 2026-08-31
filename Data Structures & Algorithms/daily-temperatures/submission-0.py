class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for temp in range(len(temperatures))]
        temp_stack = []

        for index, temp in enumerate(temperatures):
            while temp_stack and temperatures[index] > temp_stack[-1][0]:
                res[temp_stack[-1][1]] = index - temp_stack[-1][1]

                temp_stack.pop()

            temp_stack.append([temp,index])
        
        return res