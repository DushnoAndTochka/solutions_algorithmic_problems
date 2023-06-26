
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield ''.join(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield ''.join(pool[i] for i in indices)


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
