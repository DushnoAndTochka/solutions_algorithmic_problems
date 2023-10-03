class Solution:
    def winner_of_game(self, colors: str) -> bool:
        a_cnt = b_cnt = res_a = res_b = 0

        for color in colors:
            if color == "A":
                a_cnt += 1
                if b_cnt > 2:
                    res_b += b_cnt - 2
                b_cnt = 0
            else:
                b_cnt += 1
                if a_cnt > 2:
                    res_a += a_cnt - 2
                a_cnt = 0

        if b_cnt > 2:
            res_b += b_cnt - 2
        if a_cnt > 2:
            res_a += a_cnt - 2

        return res_a > res_b
