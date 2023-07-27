from math import ceil


class Solution:
    def min_speed_on_time(self, dist: list[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        if len(dist) == 1:
            return ceil(round(dist[0] / hour, 2))

        hour_for_last = round(hour - len(dist) + 1, 2)
        max_speed = min_speed = ceil(dist[-1] / hour_for_last)
        if round(hour % 1, 2):
            max_speed = ceil(dist[-1] / round(hour % 1, 2))
        result = max_speed = max(max_speed, max(dist))

        if hour_for_last <= 1:
            return max_speed

        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            hours_count = 0

            for i in range(len(dist) - 1):
                hours_count += ceil(dist[i] / mid_speed)
            hours_count += dist[-1] / mid_speed

            if 0 <= round(hour - hours_count, 2):
                result = min(result, mid_speed)

            if round(hour - hours_count, 2) > 0:
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1

        return result
