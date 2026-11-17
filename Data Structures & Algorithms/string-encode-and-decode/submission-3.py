class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for i in range(len(strs)) :
            encoded_string += str(len(strs[i])) + "#" + strs[i]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        left = 0
        words = []

        while left < len(s):
            right = left
            while s[right] != "#" :
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            words.append(s[left:right])
            left = right
        return words