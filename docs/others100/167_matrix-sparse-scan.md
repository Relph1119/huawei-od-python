# 167 矩形稀疏扫描

## 题目描述

如果矩阵中的许多系数都为零，那么该矩阵就是稀疏的。对稀疏现象有兴趣是因为它的开发可以带来巨大的计算节省，并且在许多大的实践中都会出现矩阵稀疏的问题。

给定一个矩阵，现在需要逐行和逐列地扫描矩阵，如果某一行或者某一列内，存在连续出现的0的个数超过了行宽或者列宽的一半(`W/2`)，则认为该行或者该列是稀疏的。

扫描给定的矩阵，输出稀疏的行数和列数。

## 输入描述

第一行输入为`M`和`N`，表示矩阵的大小`M*N`，取值范围是0 < M,N <= 100。

接下来`M`行输入为矩阵的成员，每行`N`个成员，矩阵成员都是有符号整数，取值范围是[-32768,32767]。

## 输出描述

输出两行，第一行表示稀疏行的个数，第二行表示稀疏列的个数。

## 示例描述

### 示例一

**输入：**

```text
3 3
1 0 0
0 1 0
0 0 1
```

**输出：**
```text
3
3
```

**说明：**

给定的3x3矩阵里，每一行和每一列内都存在2个0，行宽3，列宽3，由于超过了(3/2=1)行宽或列宽的一半，因此稀疏行有3个，稀疏列有3个。

### 示例二

**输入：**

```text
5 3
-1 0 1
0 0 0
-1 0 0
0 -1 0
0 0 0
10
```

**输出：**

```text
5
3
```

**说明：**

给定的5x3矩阵，每行里面0的个数大于等于1表示稀疏行，每列里面0的个数大于等于2表示稀疏行，所以有5个稀疏行，3个稀疏列。

## 解题思路

1. 按行遍历矩阵：
    - 计算每行里面0的个数。
    - 如果大于等于行宽的一半，则统计稀疏行的个数。
2. 按列遍历矩阵：
    - 计算每列里面0的个数。
    - 如果大于等于列宽的一半，则统计稀疏列的个数。    
3. 返回稀疏行个数和稀疏列个数。

## 解题代码

```python
def solve_method1(row, col, matrix):
    count_row = 0
    required_zeros = col // 2
    for i in range(row):
        cnt = matrix[i].count(0)
        if cnt >= required_zeros:
            count_row += 1

    count_col = 0
    required_zeros = row // 2
    for i in range(col):
        tmp = []
        for j in range(row):
            tmp.append(matrix[j][i])
        cnt = tmp.count(0)
        if cnt >= required_zeros:
            count_col += 1
    return count_row, count_col


if __name__ == '__main__':
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert solve_method1(3, 3, matrix) == (3, 3)
    matrix = [[-1, 0, 1], [0, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 0]]
    assert solve_method1(5, 3, matrix) == (5, 3)
```


