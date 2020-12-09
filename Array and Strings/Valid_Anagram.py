class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s)==collections.Counter(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	return sorted(s)==sorted(t)