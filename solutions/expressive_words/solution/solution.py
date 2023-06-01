import dataclasses


@dataclasses.dataclass
class Streak:
    letter: str
    count: int

    def is_expressed(self, other: 'Streak') -> bool:
        if self.letter != other.letter:
            return False
        if self.count == other.count:
            return True
        if self.count < other.count:
            return False
        return self.count >= 3


class Solution:
    def expressive_words(self, s: str, words: list[str]) -> int:
        s_streaks = self.get_streaks(s)
        return sum(
            self.check(self.get_streaks(word), s_streaks)
            for word in words
        )

    def check(self, word_streaks: list[Streak], s_streaks: list[Streak]):
        if len(s_streaks) != len(word_streaks):
            return False
        for s_streak, word_streak in zip(s_streaks, word_streaks):
            if not s_streak.is_expressed(word_streak):
                return False
        return True

    def get_streaks(self, word: str) -> list[Streak]:
        work_it = iter(word)
        streak_letter = next(work_it)
        streak_len = 1
        streaks = []
        for letter in work_it:
            if letter == streak_letter:
                streak_len += 1
            else:
                streaks.append(Streak(streak_letter, streak_len))
                streak_letter = letter
                streak_len = 1

        streaks.append(Streak(streak_letter, streak_len))
        return streaks
