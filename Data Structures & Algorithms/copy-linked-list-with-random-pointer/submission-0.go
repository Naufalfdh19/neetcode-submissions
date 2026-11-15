/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    dummy := &Node{}

	hashmap := make(map[*Node]*Node)

	curr := head
	for curr != nil {
		newNode := &Node{Val: curr.Val}
		hashmap[curr] = newNode
		curr = curr.Next
	}

	curr = head
	newCurr := dummy 
	for curr != nil {
		newNode := hashmap[curr]
		newNodeNext := hashmap[curr.Next]
		newNodeRandom := hashmap[curr.Random]

		newNode.Next = newNodeNext
		newNode.Random = newNodeRandom

		newCurr.Next = newNode

		newCurr = newCurr.Next
		curr = curr.Next
	}

	return dummy.Next
}
