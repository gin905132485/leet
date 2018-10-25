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
store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
For the purpose of this problem, assume that your function
returns 0 when the reversed integer overflows.
'''
import random

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if -2**31 < x < 2**31 -1:
        if x > 0:
            x = str(x)
            j = str(len(x)) #转化为字符串长度
            sr = ''
            for i in range(int(j)): #获取索引
                r = int(j)
                i = r - i - 1 #索引取反
                sr = sr + str(x[i])
            if -2**31 < int(sr) < 2**31 -1:
                return int(sr)
            else:
                return 0

        elif x < 0:
            x = str(x)
            j = str(len(x)) # 转化为字符串长度
            sr = '-'
            for i in range(int(j)-1): # 获取索引
                r = int(j)
                i = r - i - 1 # 索引取反
                sr = sr + str(x[i])
            if -2**31 < int(sr) < 2**31 -1:
                return int(sr)
            else:
                return 0

        elif x == 0:
            return 0
    else:
        return 0



print(reverse(2147483647))