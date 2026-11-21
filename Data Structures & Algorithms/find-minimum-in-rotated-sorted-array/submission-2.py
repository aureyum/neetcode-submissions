class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min = float('inf')

        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if nums[mid] < min :
                min = nums[mid]
            if nums[mid] < nums[right] :
                right = mid
            else:
                left = mid+1

        return min

                
