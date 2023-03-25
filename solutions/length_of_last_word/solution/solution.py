class Solution(object):

    def length_of_last_word(self, s: str) -> int:
        len_last_word = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if len_last_word == 0:
                    # Если наш счетчик равен нулю,
                    # значит мы еще не встречали буквы и
                    # эти проблемы для нас не показательны.
                    continue

                # Если наш счетчик не равен нулю,
                # значит мы уже встречали буквы и
                # прошли все слово целиком.
                return len_last_word
            len_last_word += 1

        return len_last_word
