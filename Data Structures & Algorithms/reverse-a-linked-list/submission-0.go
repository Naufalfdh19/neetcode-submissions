/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    arr := []int{}

	curr := head
	for curr != nil {
		arr = append(arr, curr.Val)
		curr = curr.Next
	}

	curr = head
	for i := len(arr)-1; i >= 0; i-- {
		curr.Val = arr[i]
		curr = curr.Next
	}

	return head
	

}
