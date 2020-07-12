
"""题目描述：在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序
，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断
数组中是否含有该整数。"""

class Solution1:
    """看作n行有序数组，用binary search,时间复杂度O(mlogn)"""
    def Find(self, target, array):
        if target is None or len(array)==0:
            return False
        for i in range(len(array)):
            lo = 0
            hi = len(array[i]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if target > array[i][mid]:
                    lo = mid + 1
                elif target < array[i][mid]:
                    hi = mid - 1
                else:
                    return True
        return False



class Solution2:
    def Find(self, target, array):
        """解法:从某⼀个⻆开始查找，然后指针向两个⽅向移动。如果从左上⻆开始，由于current <target时，向右向下都更⼤，会有歧义（从右下⻆开始同理），
        如果从左下⻆开始，当current <target 时，说明应当向右移动⼀格，当current>target时，说明应当向上移动⼀格，没有歧义。（从右上⻆开 始同理）"""
        if target is None or len(array) == 0:
            return False
        row = 0
        col = len(array[0]) - 1
        while row < len(array) and col >= 0:
            current = array[row][col]
            if target > current:
                row += 1
            elif target < current:
                col -= 1
            else:
                return True
        return False

