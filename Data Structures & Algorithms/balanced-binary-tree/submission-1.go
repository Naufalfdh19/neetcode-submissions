/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isBalanced(root *TreeNode) bool {
	isBalance, _ := helper(root)

	return isBalance
}

func helper(root *TreeNode) (bool, int) {
	if root == nil {
		return true, 0
	}

	isRight,left := helper(root.Left)
	isLeft, right := helper(root.Right)

	if int(math.Abs(float64(left)-float64(right))) > 1 {
		return false, max(left,right)+1
	}

	return isLeft && isRight, max(left,right)+1 
}

