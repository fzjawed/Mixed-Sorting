class Solution:
    def solve(self, nums):
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i] % 2 == 0 and nums[j] % 2 == 0:
                    if nums[i] > nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
                if nums[i] % 2 == 1 and nums[j] % 2 == 1:
                    if nums[i] < nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
        return nums