'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''
class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sr = ''
        if strs != []:               #输入非空列表时
            l1 = min(len(i) for i in strs)
            for i in range(l1):      #操作次数
                lst = []
                for j in strs:       #提取出每个字符串的第i项
                    lst.append(j[i]) #添加到列表
                lst = list(set(lst)) #列表去重
                if len(lst) == 1 and lst[0].islower():    #当对应字符相同时添加至sr
                    sr = sr+(lst[0])
                else:                #当出现不同字符时终止循环
                    break
            print(sr)
            return sr
        elif strs == []:
            return sr

a = Solution()
a.longestCommonPrefix(['a1aca','a1ba'])