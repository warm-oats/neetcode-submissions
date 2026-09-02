class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start_i = 0
        end_i = len(heights) - 1
        area = 0

        while start_i < end_i:
            area = max(area, (end_i - start_i) * min(heights[start_i], heights[end_i]))

            if heights[start_i] < heights[end_i]:
                start_i += 1
            else:
                end_i -= 1
        
        return area