/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func goodNodes(root *TreeNode) int {
    res := 0

	helper(root,root.Val, &res)

	return res
}

func helper(root *TreeNode, max int, res *int) {
	if root == nil {
		return 
	}

	if root.Val >= max {
		max = root.Val
		*res += 1
	}

	helper(root.Left, max, res)
	helper(root.Right, max, res)
}