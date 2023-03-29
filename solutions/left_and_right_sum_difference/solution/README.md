# Left and Right Sum Differences



- ### Наивное решение
    Для каждого элемента можно посчитать сумму справа и сумму слева
    
  ```python
  def left_rigth_difference(nums: list[int]) -> list[int]:
      
      r = []
      
      for i in range(len(nums)):
          left = sum(nums[0:i])
          right = sum(nums[i+1:])
          r.append(abs(left - right))
      return r
  ```
    
    **Плюсы**
    - Решение очень короткое и понятное.

    **Минусы**
    - Решение используем линейную дополнительную память (nums[0:i] - создаёт список, который не используется в результате)
    - Решение работает за квадратичное время O(n^2)

- ### Решение с сохранением суммы справа и слева
    
    Можно найти сумма справа и когда мы итерируемся по элементам, отнимать каждый элемент
    А для нахождения суммы слева инициализируем её нулём и добавляем каждый элемент
     
    ```python
    def left_rigth_difference(nums: list[int]) -> list[int]:
        right = sum(nums)
        left = 0
        r = []
        for num in nums:
            right -= num
            r.append(abs(right-left))
            left += num
        return r
    ```

    **Плюсы**
    - Решение понятное.
    - Работает за линейное время - O(n)
    - Не использует линейную дополнительную память - O(1)
