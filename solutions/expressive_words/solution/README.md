# Expressive Words

Для решения задачи нам нужно будет несколько вспомогательных функций и один вспомогательный класс.

Класс Streak - содержит буквы и сколько раз она идёт подряд

```python
import dataclasses


@dataclasses.dataclass
class Streak:
    letter: str
    count: int
```

Так же можно добавить метод в этому классу, который показывает можно ли данный streak привести из work streak.  

```python
import dataclasses


@dataclasses.dataclass
class Streak:
    letter: str
    count: int
    
    def is_expressed(self, other: 'Streak') -> bool:
        # Если буквы не совпадают, то нельзя
        if self.letter != other.letter:
            return False
        # Если количество букв одинаково, то можно
        if self.count == other.count:
            return True
        # Если количество в word больше, то возвращаем False
        if self.count < other.count:
            return False
        # Иначе возвращаем имеет ли количество больше трёх
        return self.count >= 3
```

Этот класс решает нашу задачу, остальное просто привести каждое слово к списку этих классов и сравнить их

```python

class Streak: ...

# Функция, которая приводит слово к списку Streak

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

# Функция, которая сравнивает s_streaks c word_streaks
def check(self, word_streaks: list[Streak], s_streaks: list[Streak]):
    # Если длина не равна, то возвращаем False
    if len(s_streaks) != len(word_streaks):
        return False
    
    for s_streak, word_streak in zip(s_streaks, word_streaks):
        if not s_streak.is_expressed(word_streak):
            return False
    return True
```


А после этого можно написать уже окончательную функцию

```python

def expressive_words(self, s: str, words: list[str]) -> int:
    s_streaks = self.get_streaks(s)
    return sum(self.check(self.get_streaks(word), s_streaks) for word in words)
```

То есть задача на то что просто разбить по функциям и аккуратно всё написать.
