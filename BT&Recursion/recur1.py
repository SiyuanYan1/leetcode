# class linkedList:#O(N)
#     def __init__(self):
#         self.head=None
#
#     def __len__(self):
#         current=self.head
#         count=0
#         while not current:
#             count+=1
#             current=current.next
#         return count
class linkedList:
    def __init__(self,x):
        self.head=None
        self.val=x
        self.next=None

    def _length(self,current):
        if current==None:
            return 0
        else:
            return 1+self._length(current.next)

    def __len__(self):
        return self._length(self.head)

    # def __contains__(self, item):
    #     current=self.head
    #     while not current:
    #         if current.val==item:
    #             return True
    #         else:
    #             current=current.next
    #     return False
    def __contains__(self, item):
        return self.contain_aux(self.head,item)
    def contain_aux(self,current,item):
        if current==None:
            return False
        elif current.val==item:
            return True
        else:
            return self.contain_aux(current.next,item)
    # def copy(self):
    #     new_list=list()
    #     for item in self:
    #         new_list.insert(len(new_list),item)
    #     return new_list

    def __copy__(self):


    def copy_aux(self,current,new_list):
        if current is not None:
            self.copy_aux()



