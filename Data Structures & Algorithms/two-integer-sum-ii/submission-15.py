class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_i = 0
        end_i = len(numbers) - 1

        while start_i < end_i:
            res = numbers[start_i] + numbers[end_i]

            if res == target:
                return [start_i+1,end_i+1]
            
            if res > target:
                end_i -= 1
            else:
                start_i += 1


            