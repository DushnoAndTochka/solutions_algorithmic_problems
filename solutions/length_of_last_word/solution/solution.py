class Solution(object):

    def length_of_last_word(self, s: str) -> int:
        counter = 0

        for i in range(len(s) - 1, -1, -1):
            if counter == 0 and s[i] == ' ':
                continue
            elif counter != 0 and s[i] == ' ':
                return counter
            elif s[i] != ' ':
                counter += 1

        return counter