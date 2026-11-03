class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = []
        if len(s) == len(t):
            for i in range(len(s)):
                list.append(s[i])
            for j in range(len(t)):
                if (t[j] in list):
                    list.remove(t[j])
            if not list:
                return True
            return False
        return False
        