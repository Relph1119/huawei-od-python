# 195 跳房子（2）

## 题目描述

跳房子，也叫跳飞机，是一种世界性的儿童游戏。游戏参与者需要分多个回合按顺序跳到第1格直到房子的最后一格，然后获得一次选房子的机会，直到所有房子被选完，房子最多的人获胜。在跳房子的过程中，如果有踩线等违规行为会结束当前回合，甚至可能倒退几步。

假设房子的总格数是`count`，小红每回合可能连续跳的步数都放在数组`steps`中，请问数组中是否有一种步数的组合，可以让小红三个回合跳到最后一格？如果有，请输出索引和最小的步数组合（数据保证索引和最小的步数组合是唯一的）。

注意：数组中的步数可以重复，但数组中的元素不能重复使用。

## 输入描述

第一行输入为房子总格数`count`，取值范围是 count <= 10000。

第二行输入为每回合可能连续跳的步数`steps`，数组长度的取值范围是3 <= steps.length <= 10000，每个步数的取值范围是 -100000 <= steps[i] <= 100000。

## 输出描述

返回索引和最小的满足要求的步数组合（顺序保持`steps`中原有顺序）。

## 示例描述

### 示例一

**输入：**

```text
9
[1,4,5,2,0,2]
```

**输出：**

```text
[4,5,0]
```


### 示例二

**输入：**

```text
9
[1,5,2,0,2,4]
```

**输出：**

```text
[5,2,2]
```

### 示例三

**输入：**

```text
12
[-1,2,4,9]
```

**输出：**

```text
[-1,4,9]
```

## 解题思路

1. `def dfs(nums, remaining, combination, indices, index):`: 这是深度优先搜索函数的定义，它接受五个参数：`nums` 表示数字列表，`remaining` 表示还需要选择几个数字，`combination` 是当前已选择的数字组合，`indices` 是当前已选择数字的索引组合，`index` 表示当前遍历的索引。
2. `global minIndexSum, targetCount, result`: 声明要在函数内部使用的全局变量。
3. `if remaining == 0:`: 如果需要选择的数字个数为 0，即已经选择了 3 个数字。
   - 在这个条件下，计算当前数字组合的和 `total` 和索引之和 `indexSumTemp`。
   - 如果数字组合的和等于给定的目标值 `targetCount`，并且索引之和小于当前最小索引之和 `minIndexSum`，则更新 `minIndexSum` 和 `result`。
4. `else:`: 否则，还需要选择更多的数字。
   - 进入一个循环，遍历从当前索引 `index` 开始到数字列表的末尾。
     - `combination.append(nums[i])`: 将当前数字添加到组合中。
     - `indices.append(i)`: 将当前数字的索引添加到索引列表中。
     - 递归调用 `dfs` 函数，同时更新剩余需要选择的数字数量为 `remaining - 1`，当前组合，当前索引列表，以及递增的索引 `i + 1`。
     - `combination.pop()`: 回溯，移除刚添加的数字。
     - `indices.pop()`: 回溯，移除刚添加的索引。
5. `minIndexSum = float('inf')`: 初始化最小索引之和为正无穷大。
6. `targetCount = int(input())`: 从标准输入读取目标和的值。
7. `nums = list(map(int, input().strip(' [\] ').split(',')))`: 从标准输入读取包含数字的字符串，将其处理为数字列表。
8. `result = []`: 初始化结果列表为空。
9. `dfs(nums, 3, [], [], 0)`: 调用深度优先搜索函数，开始寻找满足条件的数字组合。

## 解题代码

```python
def dfs(nums, remaining, combination, indices, index):
    global minIndexSum, targetCount, result

    if remaining == 0:
        total = 0
        indexSumTemp = 0
        for i in range(3):
            total += combination[i]
            indexSumTemp += indices[i]
        if total == targetCount and indexSumTemp < minIndexSum:
            minIndexSum = indexSumTemp
            result = combination[:]
    else:
        for i in range(index, len(nums)):
            combination.append(nums[i])
            indices.append(i)
            dfs(nums, remaining - 1, combination, indices, i + 1)
            combination.pop()
            indices.pop()


minIndexSum = float('inf')
targetCount = int(input())
nums = list(map(int, input().strip(' [\] ').split(',')))
result = []
dfs(nums, 3, [], [], 0)
output = '[' + ', '.join(map(str, result)) + '] '
print(output)
```
