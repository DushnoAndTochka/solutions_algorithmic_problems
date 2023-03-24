# FindMinimumInRotatedSortedArray Problem

## Описание:
Имеется некий отсортированный массив размеров N. 

Массив несколько раз сдвинули, те у каждого элемента индекс увеличился на 1, а у последнего стал равен нулю

Пример:
```python
array = [1, 2, 3, 4, 5]
# first rotate
array # => [5, 1, 2, 3, 4]
...
```
Таким образом получили массив у которого есть неизвестный сдвиг, но он все также отсортирован относительно этого сдвига.

На вход в функцию подается:
-  `nums` - массив с сдвигом, как описано выше

Необходимо сказать какой в нем `MIN` элемент.

## Пример
```python
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

```python
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

---
<a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/">Задача на LeetCode</a>