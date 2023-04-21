# ImplementMagicDictionary Problem

Решение можно описать следующим образом:

- Создаём словарь в котором будут содержаться все замены
- В методе build_dict добавляем все замены каждого слова в наш словарь
- При поиске для каждой замены слова проверяем, есть ли отличное слово в нашем словаре от текущего слова

Разобъем все решение по объяснению каждого из методов.

```python
class MagicDictionary:
    ...
    def build_dict(self, words: list[str]) -> None:
        # Добавляем каждый элемент в наш словарь
        for word in words:
            self._insert(word)
    ...
```

А теперь разберем метод _insert

```python
class MagicDictionary:
    # Нужна определенная константа
    _HAS_MORE_ONE_WORD = '*'
    
    def __init__(self):
        # При инициализации создаём пустой словарь
        self._words_by_replaced = {}
    
    def _insert(self, word: str):
        # Проходимся по каждой букве
        for i in range(len(word)):
            # Заменяем букву на *
            replaced = self._make_replaced(word, i)
            
            # Если слово уже есть с такой замены
            if replaced in self._words_by_replaced and replaced != word:
                # Значит не обязательно нам хранить все слова, а можно просто записать константу
                # Так как если два элемента в словаре, то слово точно не будет равно одному из них
                self._words_by_replaced[replaced] = self._HAS_MORE_ONE_WORD
            else:
                # Добавляем слово в словарь
                self._words_by_replaced[replaced] = word
    
    # Этот метод нам нужен для того что бы заменять один символ в слове 
    def _make_replaced(self, word: str, i: int):
        return word[:i] + '*' + word[i + 1:]
```

Теперь мы научились создавать наш словарь, теперь научимся провереть есть ли слово в нашем словаре

И этот метод довольно простой.

```python

class MagicDictionary:
    
    def __init__(self):
        # При инициализации создаём пустой словарь
        self._words_by_replaced = {}
    
    def search(self, search_word: str) -> bool:
        # Проходимся по каждой букве слова
        for i in range(len(search_word)):
            # Получаем слово с заменой 
            replaced = self._make_replaced(search_word, i)
            # Если оно есть в нашем словаре
            if replaced in self._words_by_replaced:
                word = self._words_by_replaced[replaced]
                # Если у нас больше двух слов с данной заменой, то возвращаем True
                if word == self._HAS_MORE_ONE_WORD:
                    return True
                # Если наше слово не равно тому что в словаре, то так же возвращаем True
                if search_word != word:
                    return True
                # Иначе переходим к следующей итерации
        return False

```