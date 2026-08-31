class Solution:
    def trap(self, height: List[int]) -> int:
        pointer_l = 0
        pointer_r = len(height) - 1
        current_index = 0

        max_l = 0
        max_r = 0

        res = 0

        while pointer_r > pointer_l:      
            if (current_index > 0):
                water_trapped = min(max_l, max_r) - height[current_index]

                if water_trapped > 0:
                    res += water_trapped

            max_l = max(max_l, height[pointer_l])
            max_r = max(max_r, height[pointer_r])

            if max_r > max_l:
                pointer_l += 1
                current_index = pointer_l
            else:
                pointer_r -= 1
                current_index = pointer_r

        return res

                



            

            


            

            
            
            
            

            