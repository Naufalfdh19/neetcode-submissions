/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
    arr := make([]int,0)

	curr := head
	for curr != nil {
		arr = append(arr, curr.Val)

		curr = curr.Next
	}

	curr = head
	l, r := 0, len(arr)-1
	count := 1
	for curr != nil {
		if count % 2 != 0 {
			curr.Val = arr[l]
			l += 1
		} else {
			curr.Val = arr[r]
			r -= 1
		}

		curr = curr.Next
		count += 1
	}
}
