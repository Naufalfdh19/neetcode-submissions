/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{}
	dummy := head

	for list1 != nil && list2 != nil{
		if list1.Val <= list2.Val {
			head.Next = list1
			list1 = list1.Next
		} else {
			head.Next = list2
			list2 = list2.Next
		}
		head = head.Next
	}

	for list1 != nil {
		head.Next = list1
		list1 = list1.Next
		head = head.Next
	}

	for list2 != nil {
		head.Next = list2
		list2 = list2.Next
		head = head.Next
	}

	return dummy.Next

}
