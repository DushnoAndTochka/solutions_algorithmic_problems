# GuessNumberHigherOrLower Problem
## Описание проблемы:

Это игра в угадай число, которое загадал. Один игрок загадывает число в диапахоне от 1 до n. Второй игрок угадывает это число. Каждый раз, когда второй игрок делает предположение, первый говорит "много", если загаданное число меньше или "мало", если загаданное число больше.

Задача заключается в том, что код является вторым игроком и пытается угадать число. Код первого игрока имеет ф-цию `guess` и возвращает следующее:
- Если предполагаемое число оказалось больше загаданного, то вернет -1
- Если меньше, то вернет 1
- Если угадали, то вернет 0

Ф-ция должна вернуть число, которое было задагадано

## Пример
```
Input: n = 10, pick = 6
Output: 6
```

---
<a href="https://leetcode.com/problems/guess-number-higher-or-lower/">Задача на LeetCode</a>