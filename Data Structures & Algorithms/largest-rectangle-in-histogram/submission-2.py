class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        index_stack = []
        height_stack = []
        max_area = 0
        final_index = 0

        for index,height in enumerate(heights):
            if not index_stack:
                index_stack.append(index)

            current_index = index

            while height_stack and height < height_stack[-1]:
                current_height = height_stack.pop()
                current_index = index_stack.pop()

                max_area = max(max_area,(index - current_index) * current_height)
            else:
                index_stack.append(current_index)

            height_stack.append(height)
            final_index += 1
        
        while height_stack and index_stack:
            max_area = max(max_area,(final_index - index_stack.pop()) * height_stack.pop())

        return max_area