#  120-最大收益股票收益问题

## 题目描述

假设知道某段连续时间内股票价格，计算通过买入卖出可获得的最大收益。
输入一个大小为n的数price$(p_1,p_2,p_3,p_4....p_n),p_i$是第i天的股要价格$p_i$的格式为股票价格(非负整型)加上货币单位 Y 或者 S，其中 Y 代表人民币，S 代表美元，这里规定 1 美元可以兑换 7 人民币。
$p_i$样例 1: 123Y 代表 123 元人民币
$p_i$样例 2: 123S 代表 123 元美元，可兑换 861 人民币
假设橡皮擦可以在任何一天买入或者卖出胶票，也可以选择放弃交易，请计其在交易周期n天内你能获得的最大收益(以人民币计算) 。

## 输入描述

输入一个包含交易周期内各天股票价格的字符串，以空格分隔。
不考虑异常输入情况。

## 输出描述

输出一个整型数代表在交易周期 n 天内你能获得的最大收益，n < 10000
备注: 股票价格只会用Y人民币或 S 美元进行输入，不考虑其他情况。

## 示例描述

### 示例一

**输入：**

```
2Y 3S 4S 6Y 8S
```

**输出：**

```
76
```

**说明：**  

对应样例，在第 1 天买入，第 3 天卖出，第 4 天买入，第 5 天卖出



## 解题思路



## 解题代码

```python
def calculate_max_profit(input_str):
	# 如果输入字符串为空，则返回0
	if not input_str:
		return 0

	#将输入字符串按空格分割成字符串列表
	price_strings = input_str.split()
	# 初始化价格列表，长度为价格字符串列表的长度，每个元素都为0
	prices = [0] * len(price_strings)

	# 遍历价格字符串列表
	for i in range(len(price_strings)):
		#取出当前价格字符串
		price_string = price_strings[i]
		# 如果价格字符串的最后一个字符不是数字， 则说明输入无效，返回0
		if not price_string[:-1].isdigit():
			return 0
		# 将价格字符串转换为整数
		value = int(price_string[:-1])
		# 取出价格字符串的最后一个字符，判断货币类型
		currency = price_string[-1]
		# 如果货币类型是"S",则将价格乘以7
		if currency == "S":
			value *= 7
		# 将处理后的价格存入价格列表
		prices[i] = value


	#初始化最大利润为0
	max_profit = 0

	#遍历价格列表，计算最大利润
	for i in range(1, len(prices)):
		# 如果当前价格比前一个价格高，则将差值加入最大利润
		if prices[i] > prices[i - 1 ]:
			max_profit += prices[i] - prices[i - 1]


	# 返回最大利润
	return max_profit

# 读取输入字符串，并计算最大利润
input_str = input()
print(calculate_max_profit(input_str))


```

## 代码运行结果

```

```
