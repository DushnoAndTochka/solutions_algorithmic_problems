# Non-overlapping Intervals Solution

## Описание

Очень не простая задача, хоть и отмечена как `medium`.

Давайте подумаем как бы мы вообще могли решить данную задачу. Начнем как всегда с рисунков.

Предположим мы имеем вот такие входные данные:

```python
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

Сами по себе интервалы мало о чем говорят и решение с ними не найти, так что давайте попробуем отобразить их на прямой:

```
  0  1  2  3  4  5
--|--|--|--|--|--|-->
    1--2
        2--3
           3--4
    1------3       
```

Это выглядело бы приблизительно вот так. Стоит помнить, что если два интервала берут начало в одной точке, то это не считается пересечением и является "ОК".

Что же теперь ? Наш массив никак не отсортирован... Поэтому пройтись в лоб сложно. Первая идея, это хранить данные в hash_map(dict) и как то крутить потом их. Но это очень дорого... С точки зрения сложности, мы получим что-то около квадратичной сложности, что бы пройтись и понять кто с кем, и где пересекается... Так что выглядит как плохой вариант...

Следующая мысль, которая приходит в голову, смотря уже на рисунок такая. Бывает всего два типа пересечений:

- простое пересечение
    ```
      0  1  2  3  4  5
    --|--|--|--|--|--|-->
      0-----2
         1-----3
    ```
    В данном случае нам не важно какой из этих интервалов вообще выбирать. Они равноценны.

- вложенное пересечение
```
  0  1  2  3  4  5
--|--|--|--|--|--|-->
    1--2
        2--3
    1------3      
```
У нас есть два "хороших" интервала, которые лежат внутри третьего("плохого") интервала.

Если в случае с "простым пересечение" нам безразницы какой брать, так как все они равноценны и будут перекрывать друг друга, а итогом выйдет только один нормальный. То вот второй уже интересней. Второй заключает внутри одного интервала, много потенциально хороших интервалов... и нам надо как-то найчиться это обрабатывать...

Если взять первый законченный интервал, то есть интервал конец которого самый "левый", то не будет ни одного интервала вложенного в него самого. То есть мы избавляемся от проблемы второго типа, вложенных интервалов, ведь вложенный интервал гарантированно закончится раньше, чем тот что мы взяли. Но если мы уверены, что интервал заканчивается самым первым, то он точно не содержит другие интервалы и не несет рисков для нас. Он потенциально может оказаться интервалом первого типа, НО мы этого не бимся от слова совсем, ведь там не принципиально кого выбирать.

Что из этого следует ??? То что мы можем отсортировать интервалы по их концу, после чего считать, что самый первый интервал - "нормальный". Если последующий интервал берет свое начало на конце первого интервала или правее, значит он также "нормальный", а вот если его начало находится левее конца первого, значит он либо содержит в себе первый, либо пересекается с ним...

ЭТО и есть по сути вся идея решения

```python
class Solution:
    def erase_overlap_intervals(self, intervals: list[list[int]]) -> int:
        # сортируем по концу
        intervals.sort(key=lambda interval: interval[1])

        # первый считаем "нормальным"
        prev_interval_i = 0
        # счетчик на 1, так как первый "нормальный"
        count = 1

        for i in range(1, len(intervals)):
            # если начало интервала лежит 
            # на конце или правее,
            # то он тоже нормальный
            if intervals[i][0] >= intervals[prev_interval_i][1]:
                # теперь будем искать относительно него
                prev_interval_i = i
                # увеличиваем счетчик нормальных
                count += 1
        # в ответе требуется число интервалов,
        # которые надо удалить, то есть тех
        # что не "нормальные"
        return len(intervals) - count

```