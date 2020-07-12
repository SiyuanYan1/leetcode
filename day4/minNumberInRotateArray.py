# -*- coding:utf-8 -*-
"""题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。"""


#naive:从前往后扫描，找到第一个比上一个元素小的元素，即为最小元素
class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        for i in range(len(rotateArray)):
            if rotateArray[i]<rotateArray[i-1]:
                return rotateArray[i]
        return rotateArray[0]

    """因为前后两部分都为有序，可以考虑使用二分查找"""# -*- coding:utf-8 -*-


# -*- coding:utf-8 -*-
class Solution2:
    def minNumberInRotateArray(self, rotateArray):

        if len(rotateArray) == 0:
            return 0
        head = 0
        rear = len(rotateArray) - 1
        if rotateArray[head] < rotateArray[rear]:
            return rotateArray[0]
        while head != rear - 1:
            mid = (head + rear) // 2
            if rotateArray[head] <= rotateArray[mid]:
                head = mid

            else:
                rear = mid

        return rotateArray[rear]

    # write code here

    # write code here
if __name__ == '__main__':
    s2=Solution2()
    res=s2.minNumberInRotateArray([3,4,5,1,2])
    print(res)





