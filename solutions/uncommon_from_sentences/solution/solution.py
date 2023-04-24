import collections


class Solution:
    def uncommon_from_sentences(self, s1: str, s2: str) -> list[str]:
        words = collections.Counter(s1.split())
        words.update(s2.split())
        return [
            word for word, count in words.items()
            if count == 1
        ]
