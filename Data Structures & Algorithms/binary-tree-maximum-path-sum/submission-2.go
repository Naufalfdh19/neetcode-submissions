/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxPathSum(root *TreeNode) int {
	res := math.MinInt

	helper(root,&res)

	return res
}

func helper(root *TreeNode, result *int) int {
	if root == nil {
		return 0
	}

	res := root.Val

	left := helper(root.Left,result)
	right := helper(root.Right,result)

	if *result < res+left+right {
		*result = res+left+right
	}

	res += max(0,left,right)

	if *result < res {
		*result = res
	}

	return res
}
