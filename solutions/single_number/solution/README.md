# SingleNumber Solution

## Описание
Вся идея решения построена на `XOR`.

---
### Немного теории по `XOR`

>XOR — это логический оператор, работающий с битами. Давайте обозначим его `^`. Если два получаемых им на входе бита одинаковы, то результат будет равен `0`, в противном случае `1`.

`XOR` складывает именно побитов. Те каждый бит одного числа, с каждым битом другого. Работает как `ИЛИ`. Если оба бита равны, то получится `0`, если разные, то `1`.

```
0011 ^ 0101 = 0110
```

Если посмотреть на сложение побитово:
```
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```

### Что же с этим делать ?
На самом деле необходимо понять несколько свойств `XOR`.
- `x ^ 0 = x`. Так как у `0`, все биты равны `0`, то он не может поменять изначального числа, пример: 
    ```
    0 ^ 0 = 0
    0 ^ 0 = 0
    1 ^ 0 = 1
    1 ^ 0 = 1
    ```
- `x ^ x = 0`. Это просто. Так как оба числа имеют одинаковые битовое представление, то и из сумма занулится.
- `x ^ y = y ^ x`. Последовательность не играет никакого значения.

Из этих двух свойств следует очень интересный вывод. Не важно в какой последовательности вы будете складывать числа через `XOR`, результат будет равн. Если во время сложения будут встречаться одинаковые числа, то они сами себя занулят.

```
  a ^ b ^ c ^ a ^ b     
= a ^ a ^ b ^ b ^ c     # Using x ^ x = 0
= 0 ^ 0 ^ c             # Using x ^ 0 = x
= c
```
---
Вщозвращаемся к решению. Думаю после прочтения теории по `XOR` решение приходит в голову само. Нам необходимо проссумировать все чила в изначальном списке через `XOR`. Итогом мы получим то самое число, которое не имеет пары, ведь все остальные попарно занулят друг друга.

## Полезно почитать:
[Ссылка на Habr](https://habr.com/ru/company/vdsina/blog/538298/). Очень понравилось то как там расписана теория, примеры взял именно от туда. Советую почитать оригинал.