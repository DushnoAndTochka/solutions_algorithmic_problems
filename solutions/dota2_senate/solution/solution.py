from collections import deque


class Solution:
    def predict_party_victory(self, senate: str) -> str:
        voting_queue = deque(senate)

        d_senator_count = voting_queue.count("D")
        r_senator_count = len(senate) - d_senator_count

        kill_d = kill_r = 0

        while r_senator_count and d_senator_count:
            voting_senator = voting_queue.popleft()
            if voting_senator == "R":
                if kill_r == 0:
                    voting_queue.append(voting_senator)
                    kill_d += 1
                else:
                    kill_r -= 1
                    r_senator_count -= 1
            else:
                if kill_d == 0:
                    voting_queue.append(voting_senator)
                    kill_r += 1
                else:
                    kill_d -= 1
                    d_senator_count -= 1

        return "Dire" if d_senator_count else "Radiant"
