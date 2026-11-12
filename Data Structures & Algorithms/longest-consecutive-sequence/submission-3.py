class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        sorted_nums = sorted(nums)
        unique_nums = list(dict.fromkeys(sorted_nums))
        longest = 1
        current = 1
        for i in range(0, len(unique_nums)-1):
            if unique_nums[i] + 1 == unique_nums[i+1] :
                current += 1
            else: current = 1
            longest = max(current, longest)
        return longest