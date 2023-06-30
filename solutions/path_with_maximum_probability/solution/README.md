# Path with Maximum Probability Solution

## Теория

Начнем с небольшой теории по графам. НО не будем уходить глубоко, так как это может занять очень много времени.

> Граф (иногда называемый неориентированным графом, чтобы отличать его от ориентированного графа, или простым графом, чтобы отличать его от мультиграфа)[4][5] представляет собой пару G = (V, E), где V - множество, элементы которого называются вершинами (единственное число: вершина), а E - множество парных вершин, элементы которых называются ребрами (иногда связями или строки).
>
> Взвешенный граф или сеть[9][10] - это граф, в котором каждому ребру присвоено определенное число (вес).[11] Такие веса могут представлять, например, затраты, длины или мощности, в зависимости от решаемой задачи. 
>
>Источник: [wiki.](https://translated.turbopages.org/proxy_u/en-ru.ru.7b220fed-649d72ea-361539a5-74722d776562/https/en.wikipedia.org/wiki/Graph_(discrete_mathematics))

Понимаю что может быть малопонятно, поэтому давайте коротко проговорим тоже самое.

Граф - это множество вершин, которые соединены ребрами.
Взвешенный граф - это когда ребра имеют числовой вес.

```
         0
      /  |  \
     1   2   3
     |  / \  | 
      4     5  
      |     |
      |     6
       \   /
         7
```

Вот как пример какой-то граф, который не взвешен. Дайте каждому переходу из вершины в вершину(ребру) какое-то число, полчите взвешенный. Это очень грубое определение и конечно стоит почитать более подробно про графы, но пока что нам этого достаточно, для данной задачи.


## Описание

У нас есть некий взвешенный граф. Необходимо определить максимально успешный путь из точки старта, до точки конца. Назовем его `оптимальный путь`

Первое что надо понять, что старт и конец не являются самой маленькой или самой большой нодой, то есть они могут находиться где-то в середине графа. При этом оптимальный путь может пролегать через начальную ноду или как-то еще.

```
         0
      /  |  \
    end   2   3
     |  / \  | 
      4   start  
      |     |
      |     6
       \   /
         7
```

Если мы будем смотреть на граф таким образом, то будет крайне не удобно с ним работать, так как совершенно не понятно куда двигаться.(сейчас речь именно о решении на листке) Поэтому предлагаю всегда располагать граф таким образом, что бы начало было сверху, а конец как можно ниже. и как бы послойно. те сначала идет старт, потом все то что является дочерним(соседним) к старту, потом их дети и так далее. То есть мы как бы удаляемся от старта в сторону конца.

```
           start
         /   |   \
        2    3    6
      /   \ /      |
     4     0       7
      \   /        |
       end         4
                   |
                  end
```

Прибилительно вот так это бы выглядело. Я позволил себе разорвать некоторые связи, что бы было легче отобразить, но надо понимать, что 7 и 2 указывают на одну и ту-же ноду 4.

А вот теперь, если пригледеться, то можно вспомнить, что мы решали что-то очень похожее на данную задачу. У нас есть вершина сверху, есть вершина снизу и надо сказать какой путь будет самым дорогим(дешевым). Не вспоминаете ? Подсказываю [пирамида](/solutions/triangle/solution/). 

Понимаю что вы в легком недоумении, но идея такая же. нам надо спускаться от вершины вниз и запоминать самую оптимальную стоимость попадания в ту или иную вершину. После продолжать спускаться до самого низа, пока не пройдемся по всем ребрам. Итогом мы получим значение самого оптимального пути к каждой из вершин, включая конечную вершину.

Хорошо, скажете вы, но как же нам построить такие данные ? Одна только подготовка может отнять кучу ресурсов. А я вам отвечу, что не надо подгатавливать данные как на рисунке. Рисунок нужен только для правильного восприятия самой задачи. Поэтому полезно рисовать на листочке или где то еще и пытаться разными способами крутить имеющиеся данные, пока не сложится картина.


Перейдем к суте самого решения. Нам необходимо знать все возможные переходы из каждой вершины в соседнюю, эти данные прийдется подготовить. Нам нужно знать `цену` перехода от старта к каждой из вершин, эти данные будем формировать по ходу. Цена перехода в точку старт всегда 1, ведь из нее мы начинаем. Имея эти данные мы можем приступить к решению

```python
from collections import defaultdict, deque


class Solution:
    def max_probability(
        self,
        n: int,
        edges: list[list[int]],
        succ_prob: list[float],
        start: int,
        end: int,
    ) -> float:
        # Создаем множество в котором будем хранить
        # оптимальную(максимальную) стоимость перехода
        # в любую вершины из точки старт
        succ_prob_node = [0] * n
        # стоимость перехода в старт равна 1
        succ_prob_node[start] = 1
        
        # теперь начинаем подгатавливать данные,
        # которые позволят хранить всех соседей
        # для каждой из вершин.
        node_paths = defaultdict(list)

        for i, [node, another_node] in enumerate(edges):
            # Если у вершины А есть сосед Б,
            # значит это справедливо и наоборот.
            # Так же необходимо запомнить их порядковый
            # номер, таким образом мы сможем узнать вес
            # их ребра или другими словами, стоимость
            # перехода из одной вершины в другую.
            node_paths[node].append((another_node, i))
            node_paths[another_node].append((node, i))
        
        # Путешествие в тысячу миль начинается с одного шага ©
        # Запомним start как первый шаг и начнем "гулять" по графу
        paths = deque()
        # deque позволяет не хранить лишние данные,
        # а забирать их на каждом шагу
        paths.append(start)

        # пока есть куда идти дальше, идем
        while paths:
            # берем вершину, которая есть в нашем пути.
            node = paths.popleft()

            # достаем всех соседей этой ноды.
            for next_node, succ_prob_i in node_paths[node]:
                # нам нет смысла двигаться в обратном направлении
                if next_node == node:
                    continue
                # считаем стоимость перехода в новую ноду
                new_v = succ_prob_node[node] * succ_prob[succ_prob_i]
                # возможно мы уже знаем путь в новую ноду
                # и он более оптимальный. Тогда не надо ничего делать
                if new_v > succ_prob_node[next_node]:
                    # Мы нашли оптимальный путь к следующей ноде
                    # Необходимо запомнить его стоимость
                    succ_prob_node[next_node] = new_v
                    # Необходимо добавить следующую ноду,
                    # что бы прогуляться по этому пути
                    # Это место можно оптимизировать!!!
                    paths.append(next_node)
        
        # После того как мы прошлись по всем путям, мы знаем ответ
        return succ_prob_node[end]
```

Признаюсь честно, это далеко не самое оптимальное решение. Оно сокрее показывает саму суть.
Даже в этом решении есть несколько мест, которые можно оптимизировать. 

Так что у вас есть все шансы сделать куда круче.