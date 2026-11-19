/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
    res := []int{}

	helper(root,&res)

	idx := 0
	for i := 0; i < k-1; i++ {
		idx += 1
	}

	return res[idx]
}

func helper(root *TreeNode, res *[]int) {
	if root == nil {
		return 
	}

	helper(root.Left,res)
	*res = append(*res,root.Val)
	helper(root.Right,res)
}
