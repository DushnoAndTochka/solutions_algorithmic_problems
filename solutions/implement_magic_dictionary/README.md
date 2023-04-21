# ImplementMagicDictionary Problem

## Описание

Необходимо реализовать класс `MagicDictionary`, в который при инициализации подается множество слов. Класс должен иметь ф-цию, которая принимает слово, и отвечает `boool`:
- Если в этом слове можно поменять ровно один символ и получить любое слово из списка, который подавался на ините, то `True`
- Иначе `False`

```python
class MagicDictionary:

    def __init__(self):
        """Инициализирует все необходимое в пустом состоянии."""
        pass

    def buildDict(self, dictionary: List[str]) -> None:
        """Принимает список слов к которым будем пытаться приводить другие слова."""
        pass

    def search(self, searchWord: str) -> bool:
        """
        Получает слово и пытается заменить ровно 1 символ, что бы слово стало одни из списка dictionary.
        См. предыдущую ф-цию. dictionary - ее аргумент.
        """
        pass
```

## Пример
```python
magic_dictionary = MagicDictionary()
# Заливаем список слов, к которым будем пытаться привести другие слова.
magicDictionary.buildDict(["hello", "leetcode"])

# ну и начинаем проверять слова.
magicDictionary.search("hello") # return False
magicDictionary.search("hhllo") # return True.
magicDictionary.search("hell") # return False
magicDictionary.search("leetcoded") # return False
```

Почему такие ответы ?
- `'hello'` -> False. Нет возможности поменять ровно один символ и получить слово из входного списка. Так как слово равно одному их таких слов.
- `'hhllo'` -> True. Меняем вторую `h` на `e` и получаем `'hello'`.
- `'hell'` и `'leetcoded'` -> False. Могло показаться, что можно удалить/добавить букву и все хорого, НО по условию задачи необходимо именно поменять одну букву на другую. По-этому эти слова не подходят.

---
<a href="https://leetcode.com/problems/implement-magic-dictionary/">Задача на LeetCode</a>