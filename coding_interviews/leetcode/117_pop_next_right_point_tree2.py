class Solution:
    def connect(self, root: 'Node') -> 'Node':
        first = root
        while first:
            head = tail = Node(None)
            cur = first
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next 
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next 
                
                cur = cur.next 
            
            first = head.next 
        
        return root 
        