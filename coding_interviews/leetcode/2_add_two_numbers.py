# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dfs to concat into string
        
        str_num1 = ''
        str_num2 = ''
        
        str_num1 = self.dfs(l1,str_num1)
        str_num2 = self.dfs(l2,str_num2)
#         print(str_num1)
#         print(str_num2)
        
        num1 = int(str_num1)
        num2 = int(str_num2)
        
        new_num = num1 + num2 
        # print(new_num)
        new_list_node = self.num_link_list(new_num)
        # print(self.dfs(new_list_node,''),)
        
        return new_list_node
        
        
    def dfs(self, node,num_str):
        if not node:
            return ''
        
        result = self.dfs(node.next, num_str)
        
        num_str = result + str(node.val)
        
        
        return num_str
        
    
    def num_link_list(self, num):
        
        str_num = str(num)
        # print(str_num)
        head = ListNode(int(str_num[-1]))
        node = head 
     
        for i in range(len(str_num)-2,-1, -1):
            node.next = ListNode(int(str_num[i]))
            node = node.next 
        
        return head 