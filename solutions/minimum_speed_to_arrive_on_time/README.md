# Minimum Speed to Arrive on Time Problem

## Описание

Вам дается число `hour`, которое обозначает кол-во часов через которое вы должны оказаться в офисе. Так же на вход подается массив `dist`, в нем хранятся расстояния поездов на которых вам необходимо проехать. `dist[i]` это расстояние `i`-го поезда, которое он проедет.

Необходимо посчитать, с какой средней скоростью должны ехать поезда, что бы вы успели на работу. Если же не возможно успеть, то необходимо вернуть `-1`

**ВАЖНО** Поезда отправляются каждый час и если вы прийдете на платформу раньше или позже, то вам прийдется ждать следующего поезда.

Пример:

```
dist = [1, 2, 3]
hour = 6

result = 1
```
Если средняя скорость каждого всех поездов будет 1 км/ч, то вы успеете вовремя. Время пересадки не учитывается. При данной скорости вы будете оказываться на пероне пересадки ровно в `**:00` каждого часа, поэтому вы не будете ждать седующего поезда.

---
<a href="https://leetcode.com/problems/minimum-speed-to-arrive-on-time/">Задача на LeetCode</a>