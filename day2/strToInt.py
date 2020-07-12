class Solution1:
    def StrToInt(self, s):
        # write code here
        minus = 1
        number = 0
        if not s:
            return number
        if s[0] == '+':
            if len(s) > 1:
                s = s[1:]
            else:
                return 0
        elif s[0] == '-':
            minus = -1
            if len(s) > 1:
                s = s[1:]
            else:
                return 0
        for i in range(0, len(s)):
            if '0' <= s[i] <= '9':
                number = number * 10 + ord(s[i]) - ord('0')
            else:
                return 0
        return number * minus


class Solution2:
    def StrToInt(self, s):
        # write code here
        numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        if s == '':
            return 0
        label = 1
        sum = 0
        for c in s:
            if c in numList:
                if c == '+':
                    label = 1
                    continue
                elif c == '-':
                    label = -1
                    continue
                else:
                    sum = sum * 10 + numList.index(c)
            else:
                sum = 0
                break
        return sum * label

