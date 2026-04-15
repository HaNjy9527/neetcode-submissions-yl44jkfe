class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)   # 虛擬頭
        curr = dummy          # 用來建新 list

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1   # 接上 list1
                list1 = list1.next  # list1 前進
            else:
                curr.next = list2   # 接上 list2
                list2 = list2.next  # list2 前進
            
            curr = curr.next        # curr 前進

        # 處理剩下的
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next