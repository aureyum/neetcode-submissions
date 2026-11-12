class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(heights) - 1

        while i < j :
            width = j - i
            height = min(heights[j], heights[i])
            area = width * height
            maxArea = max(area, maxArea)

            if heights[i] > heights[j] :
                j -= 1
            else: i += 1

        return maxArea
        