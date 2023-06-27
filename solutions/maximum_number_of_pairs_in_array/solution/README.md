# Maximum Number of Pairs in Array Solution

## Описание

Начнем с простого и понятного решениея.

### Решение через сортировку.

Мы можем отсортировать входящий массив данных. После этого будет легко найти все пары. Если текущее и предыдущее равны, значит у нас пара. Если не равны, значит найдено новое число. Или же мы можем просто посчитать эти числа и если получим 
- четное число. Значит все числа имеют пары
- нечетное число. Значит одно число не имеет пары

```python
class Solution:
    def number_of_pairs(self, nums: list[int]) -> list[int]:
         nums.sort()

        counter = 0
        curent_num = nums[0]
        res = [0, 0]

        print(nums)
        for num in nums:
            if num == curent_num:
                counter += 1
            else:
                res[0] += counter // 2
                res[1] += 1 if counter % 2 != 0 else 0
                curent_num = num
                counter = 1

        res[0] += counter // 2
        res[1] += 1 if counter % 2 != 0 else 0
        
        return res
```

итогом получаем вот такого монстра. Давайте подумаем какая тут будет сложность ? `O(n * log(n))` так как в решении есть сортировка.

### Решение через Counter

В предыдущем решении можно было заметить, что мы считаем кол-во каждого числа и потом что-то с этим делаем. Тогда зачем нам вообще сортировка ? Мы можем просто посчитать каждое число и потом получить ответ их этих данных.

```python
class Solution:
    def number_of_pairs(self, nums: list[int]) -> list[int]:
        counted_nums = Counter(nums)

        res = [0, 0]

        for _, v in counted_nums.items():
            ceil = v // 2
            res[0] += ceil
            
            if v % 2 != 0:
                res[1] += 1

        return res
```

Что же тут у нас с сложностью ? Все гораздо лучше. Она стала линейной `O(n)`. 

### Решение через dict

Предыдущее решение мне не нравится только тем, что мы два раза гуляем по данным и в этом нет большого смысла. 

```python
class Solution:
    def number_of_pairs(self, nums: list[int]) -> list[int]:
        encountered_nums = dict()
        res = [0, 0]

        for num in nums:
            if encountered_nums.get(num):
                encountered_nums[num] -= 1
                res[0] += 1
                res[1] -= 1
            else:
                encountered_nums[num] = 1
                res[1] += 1

        return res
```

Сложность так же линейная. Но теперь мы расчитываем ответ прям во время первой проходки. Мы не используем деление, а это тоже не большой плюсик.