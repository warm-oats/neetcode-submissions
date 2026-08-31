class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for temp in range(len(temperatures))]
        temp_stack = []
        TEMP_VALUE = 0
        TEMP_INDEX = 1

        for index, temp in enumerate(temperatures):
            while temp_stack and temperatures[index] > temp_stack[-1][TEMP_VALUE]:
                res[temp_stack[-1][TEMP_INDEX]] = index - temp_stack[-1][TEMP_INDEX]

                temp_stack.pop()

            temp_stack.append([temp,index])
        
        return res