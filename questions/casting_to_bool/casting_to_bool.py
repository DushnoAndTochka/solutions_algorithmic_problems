class Class:

    def __repr__(self):
        return 'Class'


class HasBool:

    def __init__(self, result: bool):
        self._result = result

    def __bool__(self):
        return self._result

    def __repr__(self):
        return f'HasBool({self._result})'


class HasLen:

    def __init__(self, n: int):
        self._n = n

    def __len__(self):
        return self._n

    def __repr__(self):
        return f'HasLen({self._n})'


def main():

    items = [
        Class(),
        HasBool(True),
        HasBool(False),
        HasLen(0),
        HasLen(1),
    ]

    true_items = []
    false_items = []

    for item in items:
        if item:
            true_items.append(item)
        else:
            false_items.append(item)

    print('true_items:', true_items)


if __name__ == '__main__':
    # Что выведется при выполнении этого скрипта?
    main()
