# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        rl = ListNode(0)
        root = rl
        rl.val = l1.val + l2.val + carry
        carry = int(rl.val/10)

        if rl.val > 9:
            rl.val = rl.val % 10        


        #traverse the nodes
        while (not ((l1.next == None) and (l2.next == None))) or carry :
            rl.next = ListNode(0)
            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = 0
                
            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = 0


            rl = rl.next
            rl.val = l1.val + l2.val + carry
            carry = int(rl.val/10)

            if rl.val > 9:
                rl.val = rl.val % 10
            

        rl.next = None

        return root

def printNode(a):
    sol_str = ""
    while True:
        
        sol_str += str(a.val)
        
        
        if a.next == None:
            break;
        
        a = a.next
        sol_str += '->'

    print(sol_str)

def parseStr2Node(str_node):
    val_list = str_node.split('->')

    root = ListNode(0)
    curr = root
    for i, item in enumerate(val_list):
        if i != 0:
            curr = curr.next
        curr.val = int(item)
        curr.next = ListNode(0)

    curr.next = None
    return root
        
    
if __name__ == '__main__':
    sol = Solution()

    n0 = parseStr2Node("8->8->8->1")
    m0 = parseStr2Node("9->4->9->1")
    printNode(n0)
    printNode(m0)
    
    a = sol.addTwoNumbers(n0,m0)
    printNode(a)
