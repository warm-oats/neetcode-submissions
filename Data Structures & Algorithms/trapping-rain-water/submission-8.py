class Solution:
    def trap(self, height: List[int]) -> int:
        left_i = 0
        right_i = len(height) - 1
        left_max = height[left_i]
        right_max = height[right_i]
        area = 0

        while left_i < right_i:
            if height[left_i] < height[right_i]:
                left_i += 1

                if height[left_i] > left_max:
                    left_max = height[left_i]
                else:
                    area += max(0, min(left_max, right_max) - height[left_i])
            else:
                right_i -= 1

                if height[right_i] > right_max:
                    right_max = height[right_i]
                else:
                    area += max(0, min(left_max, right_max) - height[right_i])
        
        return area
