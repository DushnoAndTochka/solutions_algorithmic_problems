from collections import defaultdict


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        available_symbols = defaultdict(int)

        left_pointer = right_pointer = max_size = window_size = 0

        while right_pointer < len(s):
            if available_symbols[s[right_pointer]] < 1:
                available_symbols[s[right_pointer]] += 1
                right_pointer += 1
                window_size += 1
                max_size = max(max_size, window_size)
            else:
                available_symbols[s[left_pointer]] -= 1
                left_pointer += 1
                window_size -= 1

        return max_size
