class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        start = []
        for c in s:
            start.append(c)
        for d in t:
            if(d not in start):
                return False
            else:
                start.remove(d)
        return True
