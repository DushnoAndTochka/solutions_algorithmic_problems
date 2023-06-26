import itertools


def combinations(characters: str, length: int):
    for item in itertools.combinations(characters, length):
        yield ''.join(item)


class CombinationIterator:

    def __init__(self, characters: str, length: int):
        self._it = combinations(characters, length)
        self._next = None

    def next(self) -> str:
        if self._next is not None:
            result = self._next
            self._next = None
            return result  # noqa: R504
        return next(self._it)

    def has_next(self) -> bool:
        if self._next is not None:
            return True
        try:
            self._next = next(self._it)
        except StopIteration:
            return False
        return True
