class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while r >= l:
            middle = math.floor((r + l) / 2)

            if target == nums[middle]:
                return middle

            if nums[l] < nums[r]:
                if target > nums[middle]:
                    l = middle + 1
                else:
                    r = middle - 1
            elif target > nums[middle]:
                if nums[l] <= nums[middle] and nums[r] <= nums[middle]:
                    if target > nums[l]:
                        l = middle + 1
                    else:
                        r = middle - 1
                elif nums[l] >= nums[middle]:
                    if target > nums[r]:
                        r = middle - 1
                    else:
                        l = middle + 1

            elif target < nums[middle]:
                if nums[r] >= nums[middle] and nums[l] >= nums[middle]:
                    if target < nums[r]:
                        r = middle - 1
                    else:
                        l = middle + 1
                elif nums[l] <= nums[middle]:
                    if target < nums[l]:
                        l = middle + 1
                    else:
                        r = middle - 1
            
        return -1


        
        