
#题目描述：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）如图，第二棵树为第一棵树的子树。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return False
        res=False
        if pRoot1.val==pRoot2.val:
            res=self.isSubTree(pRoot1,pRoot2)
        if res==False:
            res=self.HasSubtree(pRoot1.left,pRoot2)
        if res==False:
            res=self.HasSubtree(pRoot1.right,pRoot2)
        return res

    def isSubTree(self,pRoot1,pRoot2):
        if  pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val!=pRoot2.val:
            return False
        return self.isSubTree(pRoot1.left,pRoot2.left) and self.isSubTree(pRoot1.right,pRoot2.right)



        

