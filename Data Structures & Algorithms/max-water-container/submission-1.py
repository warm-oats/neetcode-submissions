class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_stored = 0
        pointer_start = 0
        pointer_end = len(heights) - 1

        while pointer_end > pointer_start:
            current_water_stored = min(heights[pointer_start],heights[pointer_end]) * (pointer_end - pointer_start)
            max_water_stored = max(max_water_stored,current_water_stored)

            if heights[pointer_end] < heights[pointer_start]:
                pointer_end -= 1
            else:
                pointer_start += 1

        return max_water_stored 