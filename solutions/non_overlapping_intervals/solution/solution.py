class Solution:
    def erase_overlap_intervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        prev_interval_i = 0
        count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev_interval_i][1]:
                prev_interval_i = i
                count += 1

        return len(intervals) - count
