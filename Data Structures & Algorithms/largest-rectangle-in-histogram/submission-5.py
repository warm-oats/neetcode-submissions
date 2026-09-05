class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hist_stack = []
        max_area = 0
        INDEX = 0
        HEIGHT = 1

        for i in range(len(heights)):
            cur_i = i

            while hist_stack and heights[i] < hist_stack[-1][HEIGHT]:
                prev_height = hist_stack.pop()
                cur_i = prev_height[INDEX]
                max_area = max(max_area, prev_height[HEIGHT] * (i - prev_height[INDEX]))
            
            hist_stack.append([cur_i, heights[i]])

        for height in hist_stack:
            max_area = max(max_area, (len(heights) - height[INDEX]) * height[HEIGHT])

        return max_area

