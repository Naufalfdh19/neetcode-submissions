/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
    linkedListLength := 0

	curr := head

	for curr != nil {
		linkedListLength += 1
		curr = curr.Next
	}

	target := linkedListLength-n

	prev := &ListNode{}
	prev.Next = head
	dummy := prev

	for i := 0; i < target; i++ {
		prev = prev.Next
	}

	prev.Next = prev.Next.Next

	return dummy.Next

}
