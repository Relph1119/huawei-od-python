#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 180_statistical_monitoring.py
@time: 2023/8/8 23:48
@project: huawei-od-python
@desc: 180 统计监控
"""


def solve_method(m,n,nums):
    count = 0
    # 查找出所有停车位位置，先count+1安上监控
    cars = []
    for i in range(m):
        for j in range(n):
            if nums[i][j]==1:
                count+=1
                cars.append((i,j))
    # 对每个汽车周围进行一次广度优先遍历，安上监控
    while cars:
        i, j = cars.pop()
        for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0<=x<m and 0<=y<n and nums[x][y]==0:
                count+=1
                nums[x][y]=1
    return count


if __name__ == '__main__':
    assert solve_method(3,3,[[0, 0, 0],[0, 1, 0],[0, 0, 0]]) == 5
    assert solve_method(3,3,[[1, 0, 0],[0, 1, 0],[0, 0, 0]]) == 6
