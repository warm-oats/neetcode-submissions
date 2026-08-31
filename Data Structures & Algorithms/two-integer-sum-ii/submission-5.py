class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1

        while True:
            while (numbers[pointer1] + numbers[pointer2]) > target:
                pointer2 -= 1
            
            if (numbers[pointer1] + numbers[pointer2]) == target:
                return [(pointer1 + 1), (pointer2 + 1)]
            else:
                pointer1 += 1


            