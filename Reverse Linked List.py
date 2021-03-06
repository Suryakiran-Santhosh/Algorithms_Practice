"""
Question: Reverse a Linked List
By: Suryakiran Santhosh

Prompt:
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # ListNode


def reverseList(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head

    llremaining = head.next
    rev = head
    rev.next = None

    while llremaining != None:
        temp = llremaining
        llremaining = llremaining.next
        temp.next = rev
        rev = temp

    return rev


def main():
    inputLL = list([1, 2, 3, 4, 5])
    linkedlist = ListNode()

    reverseList(linkedlist)  # Output 5->4->3->2->1->NULL


if __name__ == "__main__":
    main()
