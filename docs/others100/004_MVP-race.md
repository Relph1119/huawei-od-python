# 004-MVP争夺战

## 题目描述

在星球争霸篮球赛对抗赛中，强大的宇宙战队，希望每个人都能拿到MVP。
MVP的条件是，单场最高分得分获得者，可以并列，所以宇宙战队决定在比赛中，
尽可能让更多的队员上场，且让所有有得分的队员得分都相同。
然而比赛过程中的每一分钟的得分都只能由某一个人包揽。

## 输入描述

输入第一行为一个数字t,表示有得分的分钟数(1<=t<=50),第二行为t个数字，代表每一分钟的得分p(1<=p<=50)

## 输出描述

输出有得分的队员都是MVP时最少的MVP得分。

## 示例描述

### 示例一

**输入：**
```
9
5 2 1 5 2 1 5 2 1
```

**输出：**
```
6
```

**说明：**  
样例分析：一共4人得分，分别都为6分
5 + 1
5 + 1
5 + 1
2 + 2 + 2

## 解题思路

这是一个分配MVP得分的问题，其中给出了一组选手得分，要求将得分平均分配给一定数量的MVP,使得每个MVP的得分相等，
并且能够得到所有选手的得分。
具体实现思路如下：
1.首先读入选手得分，并计算出选手总得分。然后对得分数组进行排序，求出最高得分作为MVP得分的下限，以及选手总得分的一半
作为MVP得分的上限。**（平均每个人和两个人平分）**
2.从下限到上限遍历所有可能的MVP得分，如果当前得分能够**整除**选手总得分，则将其作为平均分。从选手得分数组的最后一位开
始，递归地进行得分分配，直到所有得分都被分配完毕或者得分无法再分配。如果成功平分所有得分，则保存当前平均分，跳出循
环。
3.最后输出总得分或者平均分，具体输出哪一个取决于是否成功平分得分。

在递归函数中，我们采用回溯法来逐步分配得分。具体实现如下：
1.如果分配的得分小于等于平均分，则分配结束。
2.从得分数组的最后一位开始遍历，如果当前得分为0，则跳过该得分。否则，将该得分加入已分配得分的集合中，并递归调用函数，
将剩余的得分分配给剩下的MVP。
3.如果递归调用成功分配了剩余的得分，则继续在原有得分集合中分配当前平均分的得分，重复步骤2。
4.如果分配失败或者得分已经全部分配完毕，则将已分配得分集合中的得分清零并返回Tu,表示分配成功。
5.如果分配成功，则检查是否还有剩余得分，以及剩余得分是否能够被平分。如果满足条件，则继续分配平均分的得分，重复步骤2。
6.如果分配失败，则将已分配得分集合中的得分弹出，并返回Fse,表示分配失败。

## 解题代码

```python
import sys

score =0
#         整数数组 分数 空列表 数组最后的位置
def combine(ints,n,lst,index):
    global score
    # 排除分数小于零且为0时，将0存入对应位置（索引即得分）
    if n <=0:
        # 这里只会执行一次(的吧)，专门处理为0情况的
        if n ==0:
            for i in range(len(lst)):
                ints[lst[i]]=0
            return True
    # 从数组末尾开始往前遍历
    for i in range(index,-1,-1):
        # 非法情况直接跳出循环
        if n <0 or sum(ints)==0:
            break
        x = ints[i]
        if x ==0:
            continue
        lst.append(i)
        # 递归
        if combine(ints,n-x,lst,i-1):
            count = sum(ints)
            if count ==0 or count % score !=0:
                break
            combine(ints,score,[],len(ints)-1)
        lst.pop()
    return sum(ints)==0

if __name__ == "__main__":
    t = int(input())
    p = input().split()
    # 取出整形分数
    ints = [int( p[i] ) for i in range(t)]

    # 计算总分
    count = sum(ints)
    # 排序该数组
    ints.sort()
    # 将最大的单个分数置为下限
    min_score = ints[t -1]

    res =0
    # 从下限到上限遍历所有可能分数
    for i in range(min_score,count //2):
        # 当可以整除时
        if count % i==0:
            score = i
            if combine(ints,score,[],t-1):
                res = score
                break
    print(count if res ==0 else res)
```
