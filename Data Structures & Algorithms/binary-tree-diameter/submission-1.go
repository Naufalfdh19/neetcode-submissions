/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diameterOfBinaryTree(root *TreeNode) int {
    maxDiameter := 0
	
	helper(root, &maxDiameter)

	return maxDiameter
}

func helper(root *TreeNode, maxDiameter *int) int {
	if root == nil {
		return 0
	}

	left := helper(root.Left, maxDiameter)
	right := helper(root.Right, maxDiameter)

	*maxDiameter = max(*maxDiameter, left+right)

	return max(left,right)+1
}
