# ValidParentheses Problem

## Описание
На вход подается строка, которая содержит следующие символы `'('`, `')'`, `'{'`, `'}'`, `'['` и `']'`. Необходимо сказать, является ли входящая строка валидной последовательностью скобок.

Валидной последовательностью скобок считается та последовательность, в которой выполняются следующие правила:

- Все открытые скобки, должны быть закрыты скобками того же вида.
- Скобки должны быть закрыты в правильном порядке.
- Каждая закрывающая скобка. закрывает скобку того же вида.

## Пример

```
Input: s = "()"
Output: true
```
---
```
Input: s = "()[]{}"
Output: true
```
---
```
Input: s = "(]"
Output: false
```

---
<a href="https://leetcode.com/problems/valid-parentheses/">Задача на LeetCode</a>