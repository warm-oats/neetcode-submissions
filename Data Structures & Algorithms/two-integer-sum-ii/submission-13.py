class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_start = 0
        pointer_end = len(numbers) - 1

        while pointer_end > pointer_start:
            current_sum = numbers[pointer_start] + numbers[pointer_end]

            if current_sum > target:
                pointer_end -= 1
            elif current_sum < target:
                pointer_start += 1
            else:
                return [pointer_start+1,pointer_end+1]
            

        

            
