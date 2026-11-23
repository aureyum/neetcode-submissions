class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}

        left = 0
        result = 0
        max_freq = 0

        for right in range(len(s)) :
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            max_freq = max(max_freq, frequency[s[right]])

            if (right-left+1) - max_freq > k :
                frequency[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result