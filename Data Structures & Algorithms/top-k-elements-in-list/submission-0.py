class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1

        sorted_freq = sorted(frequency.items(), key = lambda x : x[1], reverse = True)

        output = []


        for i in range(k) :
            output.append(sorted_freq[i][0])

        return output



