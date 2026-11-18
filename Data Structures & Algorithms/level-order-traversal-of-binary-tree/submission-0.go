/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
	res := [][]int{}

	helper(root,0,&res)

	return res
}

func helper(root *TreeNode, level int, res *[][]int) {
	if root == nil {
		return
	}

	if len(*res) <= level {
		*res = append(*res, []int{})
	} 

	(*res)[level] = append((*res)[level],root.Val)

	helper(root.Left, level+1, res)
	helper(root.Right, level+1, res)
}
