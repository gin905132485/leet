'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true

示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
'''

class Solution:

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x > 0:
            x = str(x)
            j = str(len(x)) #转化为字符串长度
            sr = ''
            for i in range(int(j)): #获取索引
                r = int(j)
                i = r - i - 1 #索引取反
                sr = sr + str(x[i])
            if sr == x:
                print(sr)
                print(x)
                return True
            else:
                print(sr)
                print(x)
                return False
        else:
            print('请输入整数')

a = Solution()
a.isPalindrome(121211)