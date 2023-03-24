# SearchA2dMatrix Solution

## Описание

Задача может ввести в ступор и показаться сложной. Но на самом деле тут очень важно прочитать условия, а именно одно правило данной матрицы:

- Первое число любой строки больше чем число предыдущей.

Что это значит ? 

Значит нам надо для начала найти строку в которой потенциально будет наше число. Такая строка должна удовлетворять следующему правилу 
```python
row[0] <= target <= row[-1]
```
То есть таргет должен быть зажат между первым и последним числом строки, тогда есть смысл в ней искать.

Дальше надо вспомнить, что все строки отсортированны, а значит мы можем просто применить уже знакомый `binary search` и быстро найти или не найти таргет.