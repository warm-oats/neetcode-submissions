class Solution:
    def trap(self, height: List[int]) -> int:
        max_heights_arr = []

        # Get prefix and suffix array
        for i in range(len(height)):
            l_pointer = 0 
            r_pointer = len(height) - 1

            prefix_max = 0
            suffix_max = 0

            while i > l_pointer:
                prefix_max = max(height[l_pointer], prefix_max)
                l_pointer += 1
            
            while i < r_pointer:
                suffix_max = max(height[r_pointer], suffix_max)
                r_pointer -= 1

            max_heights_arr.append(min(prefix_max, suffix_max) - height[i])

        max_area = 0

        for area in max_heights_arr:
            if area > 0:
                max_area += area
            
        return max_area

            

            
            
            
            

            