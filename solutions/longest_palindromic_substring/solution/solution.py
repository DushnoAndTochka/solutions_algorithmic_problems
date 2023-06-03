class Solution:
    def longest_palindrome(self, s: str) -> str:
        result_start_pos = 0
        result_stop_pos = 1

        for i in range(len(s)):
            for right in [1, 2]:
                left = i
                right += i

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                if (right - left - 1) > (result_stop_pos - result_start_pos):
                    result_start_pos = left + 1
                    result_stop_pos = right

        return s[result_start_pos:result_stop_pos]
