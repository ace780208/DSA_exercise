# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
def swap(head: ListNode, left: int, right: int) -> ListNode:
    # swap the left-th node and the right-th node (1-index)
    if left == right:
        return head
    i = 1
    dummy = head
    prev_left = None
    node_left = None
    prev_right = None
    node_right = None
    while dummy and i <= right:
        if i == left - 1:
            prev_left = dummy
        
        if i == left:
            node_left = dummy
        
        if i == right - 1:
            prev_right = dummy
        
        if i == right:
            node_right = dummy
            
        i+=1
        dummy = dummy.next
        
    if not prev_left:
        head = node_right
    else:
        prev_left.next = node_right
    prev_right.next = node_left
    tmp = node_left.next
    node_left.next = node_right.next
    node_right.next = tmp

    return head


def reverse(head: ListNode) -> ListNode:
    # reverse linked list
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev


def partial_reverse(head: ListNode, left: int, right: int) -> ListNode:
    # reverse the left-th node to the right-th node (1-index)
    # e.g. 1->2->3->4->5->6->7->8->9 to 1->2->6->5->4->3->7->8->9
    if left == right:
        return head
    i = 1
    dummy = head
    unchange_head = None
    unchange_tail = None
    change_head = None
    change_tail = None
    while i <= right:
        if i == left - 1:
            unchange_head = dummy
        if i == left:
            change_head = dummy
        if i == right:
            change_tail = dummy
            unchange_tail = dummy.next
            change_tail.next = None
            
        i += 1
        dummy = dummy.next

    reverse_head = reverse(change_head)
    
    if unchange_head:
        unchange_head.next = reverse_head
    if unchange_tail:
        change_head.next = unchange_tail
    return head


def main():
    intlist = list(range(1, 10))
    head = None
    dummy = None
    for i in intlist:
        tmp_node = ListNode(i)
        if not head:
            head = tmp_node
            dummy = head
        else:
            dummy.next = tmp_node            
            dummy = dummy.next
            
    head = swap(head, 1, 2)
    head = partial_reverse(head, 2, 6)
    node_string = []
    while head:
        node_string.append(str(head.val))
        head = head.next
    print('->'.join(node_string))

if __name__ == '__main__':
    main()