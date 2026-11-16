class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = [1] * len(nums)
        right_prefix = [1] * len(nums)

        i=1

        while i < len(nums) :
            left_prefix[i] = left_prefix[i-1] * nums[i-1] 
            i += 1
        
        i= i-2
        while i > -1:
            right_prefix[i] = right_prefix[i+1] * nums[i+1]
            i -= 1

        return [left_prefix[j] * right_prefix[j] for j in range(len(nums))]

