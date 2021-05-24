#dubesar on binarysearch
class Solution:
    def solve(self, nums):
        eve = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                eve.append(nums[i])
            else:
                odd.append(nums[i])
        eve = sorted(eve)
        odd = sorted(odd)
        odd.reverse()
        eve_i = 0
        odd_i = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = eve[eve_i]
                eve_i += 1
            else:
                nums[i] = odd[odd_i]
                odd_i += 1
        return nums
        