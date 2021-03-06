
def calculateCircleArea(radius):
    print(radius)
    return radius



calculateCircleArea(10)


def test_calculateCircleArea():
    calculateCircleArea(10)



#
# 1. 题目介绍
# 根据圆的半径，计算圆的面积。有圆面积计算公式可知：面积 = PI * r * r。

# 2. 题目思路，我是如何解答这个问题的
# 构建一个函数来完成这个事情。输入参数：radius代表圆的半径，通过公式可以计算出一个面积的值，返回该值完成该题目。
#
# 3. 题目的关键知识点是什么？
# 函数，基本运算，

# 4. 题目容易出错的地方是什么？
# 对于圆的半径没有进行判断，可能输入的是一个字符串，也可能什么也没有输入，也可能输入的是一个负数

# 5. 通过这道题目我学习到了什么？
# 一道完整的题目包含如下几个步骤
# * 有完整的解题思路
# * 通过代码对思路进行实现
# * 考虑一些异常的case
# * 通过单元测试来保证逻辑的正确性