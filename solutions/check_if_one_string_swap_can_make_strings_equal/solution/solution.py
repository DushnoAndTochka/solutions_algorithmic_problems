class Solution:
    def are_almost_equal(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        diff_letters = None
        has_diff = False

        for i1, i2 in zip(s1, s2):
            if i1 == i2:
                continue

            if has_diff:
                return False

            if diff_letters is None:
                diff_letters = (i1, i2)
            elif diff_letters == (i2, i1):
                diff_letters = None
                has_diff = True
            else:
                return False

        return diff_letters is None
