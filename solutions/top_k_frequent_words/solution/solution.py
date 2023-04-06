from collections import Counter


class Solution:
    def top_k_frequent(self, words: list[str], k: int) -> list[str]:
        word_counter = Counter(words)
        return sorted(word_counter, key=lambda w: (-word_counter[w], w))[:k]
