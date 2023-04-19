# TopKFrequentElements Solution

## Описание

### Начнем с простого решения.

Нам необходимо посчитать сколько у нас всего повторений у каждого элемента, для этого отлично подойдет `dict`, либо уже готовый `Counter` из пакета `collections`. После надо отсортировать кол-во повторений и взять `k` самых часто встречаемый.

> Очень топорное, но крайне понятное решение.

```python
def solution(nums: list(int), k: int) -> list(int):
    counter = dict()

    for n in nums:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1

    # Все выше записанное можно заменить на counter = Counter(nums)

    sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)

    return [item[0] for item in sorted_counter[:k]]
```

Есть более короткая запись данного решения 

```python
from collections import Counter

def solution(nums: list(int), k: int) -> list(int):
    return [i[0] for i in Counter(nums).most_common(k)]
```

Всего две строки, оптимизация многого из под коробки, но суть почти таже.

Теперь давайте подумаем о сложности. Одна только сортировка подарит нам `O(n log(n))`... А по заданию надо достичь более приемлемых показателей.

### А что если использовать кучу ?

Решение с сортировкой кучей и правда выглядит гораздо лучше

> Про ф-цию `nlargest` можно почитать [тут](https://docs-python.ru/standart-library/modul-heapq-python/funktsija-nlargest-modulja-heapq/).
```python
def solution(nums: list[int], k: int) -> list[int]: 
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get) 
```

Уже получше. Сложность данного алгоритма будет `O(n log(k))`. Но на больших числах сортировка из первого пункта, будет работать шустрее. Тяжело сказать о причинах, но это факт и в доке по `nlargest` это так же прописано.

Выходит что решение уже нас устраивает и оно выполняет все требования. Это правда, но есть еще один пример того, как можно решить эту проблему. О ней вы можете почитать у [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/editorial/).


