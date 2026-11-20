/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func buildTree(preorder []int, inorder []int) *TreeNode {
    return helper(preorder, inorder)
}

func helper(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}

	root := TreeNode{Val: preorder[0]}

	inorderIdx := 0
	for i, num := range inorder {
		if num == preorder[0] {
			inorderIdx = i
			break
		}
	}

	// fmt.Println(preorder, inorder, inorderIdx)

	inorderLeft := inorder[:inorderIdx]
	inorderRight := inorder[inorderIdx+1:]

	preorderIdx := len(inorderLeft)+1
	var preorderLeft []int
	if preorderIdx >= 1 {
		preorderLeft = preorder[1:preorderIdx]
	}
	var preorderRight []int
	if preorderIdx <= len(preorder) {
		preorderRight = preorder[preorderIdx:]
	}
	

	left := helper(preorderLeft, inorderLeft)
	right := helper(preorderRight, inorderRight)
	
	root.Left = left
	root.Right = right

	return &root
}