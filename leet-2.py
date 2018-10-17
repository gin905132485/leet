'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only
store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.
'''
import random

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
        x = str(x)
        j = str(len(x)) #转化为字符串长度
        sr = ''
        for i in range(int(j)): #获取索引
            r = int(j)
            i = r - i - 1 #索引取反             
            sr = sr + str(x[i])
        return int(sr)

    elif x < 0:
        x = str(x)
        j = str(len(x)) # 转化为字符串长度
        sr = '-'
        for i in range(int(j)-1): # 获取索引
            r = int(j)
            i = r - i - 1 # 索引取反
            sr = sr + str(x[i])
        return int(sr)

    elif x == 0:
        return 0

N = random.randint(-2**31,2**31 - 1)
print(N)
print(reverse(N))