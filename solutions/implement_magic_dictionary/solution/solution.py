class MagicDictionary:
    _HAS_MORE_ONE_WORD = '*'

    def __init__(self):
        self._words_by_replaced = {}

    def build_dict(self, words: list[str]) -> None:
        for word in words:
            self._insert(word)

    def search(self, search_word: str) -> bool:
        for i in range(len(search_word)):
            replaced = self._make_replaced(search_word, i)
            if replaced in self._words_by_replaced:
                word = self._words_by_replaced[replaced]
                if word == self._HAS_MORE_ONE_WORD or search_word != word:
                    return True
        return False

    def _insert(self, word: str):
        for i in range(len(word)):
            replaced = self._make_replaced(word, i)
            if replaced in self._words_by_replaced:
                self._words_by_replaced[replaced] = self._HAS_MORE_ONE_WORD
            else:
                self._words_by_replaced[replaced] = word

    def _make_replaced(self, word: str, i: int):
        return word[:i] + '*' + word[i + 1:]
