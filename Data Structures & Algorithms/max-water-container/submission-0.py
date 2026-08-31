class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_pointer = 0
        r_pointer = len(heights) - 1
        max_water = 0

        while r_pointer > l_pointer:
            water_amount = (r_pointer - l_pointer) * min(heights[l_pointer], heights[r_pointer])
            max_water = max(water_amount, max_water)

            if heights[l_pointer] < heights[r_pointer]:
                l_pointer += 1
            else:
                r_pointer -= 1
        
        return max_water
