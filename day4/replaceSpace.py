# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res=''
        for c in s:
            if c!=' ':
                res+=c
            else:
                res+='%20'
        return res