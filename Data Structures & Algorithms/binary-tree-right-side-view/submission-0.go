/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rightSideView(root *TreeNode) []int {
	temp := [][]int{}

	helper(root,0,&temp)

	res := []int{}

	for _, arr := range temp {
		res = append(res, arr[len(arr)-1])
	}

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
