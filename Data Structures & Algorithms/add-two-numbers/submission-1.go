/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}

	curr := dummy
	left := 0
	for l1 != nil && l2 != nil {
		sum := l1.Val+l2.Val
		remain := (sum+left)%10
		node := &ListNode{Val: remain}	
		left = (sum+left)/10

		curr.Next = node
		curr = curr.Next
		l1 = l1.Next
		l2 = l2.Next
	}

	for l1 != nil {
		remain := (l1.Val+left)%10
		node := &ListNode{Val: remain}	
		left = (l1.Val+left)/10

		curr.Next = node
		curr = curr.Next
		l1 = l1.Next
	}

	for l2 != nil {
		remain := (l2.Val+left)%10
		node := &ListNode{Val: remain}	
		left = (l2.Val+left)/10

		curr.Next = node
		curr = curr.Next
		l2 = l2.Next
	}

	if left != 0 {
		node := &ListNode{Val: 1}	
		curr.Next = node
	}

	return dummy.Next
}
