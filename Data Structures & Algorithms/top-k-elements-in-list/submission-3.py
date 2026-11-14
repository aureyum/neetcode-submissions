class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in range(len(nums)) :
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1

        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_frequency[:k]]