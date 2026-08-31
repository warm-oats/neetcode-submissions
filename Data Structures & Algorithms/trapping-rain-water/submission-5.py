class Solution:
    def trap(self, height: List[int]) -> int:
        pointer_left = 0
        pointer_right = len(height) - 1
        current_block_index = 0
        max_left = height[pointer_left]
        max_right = height[pointer_right]
        max_area_water_trapped = 0 

        while pointer_right > pointer_left:
            max_left = max(max_left,height[pointer_left])
            max_right = max(max_right,height[pointer_right])
            water_trapped = min(max_left,max_right) - height[current_block_index]

            if water_trapped > 0:
                max_area_water_trapped += water_trapped

            if max_right > max_left:
                pointer_left += 1
                current_block_index = pointer_left
            else:
                pointer_right -= 1
                current_block_index = pointer_right

        return max_area_water_trapped

            
