import collections


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
