/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {
    var parent *TreeNode

	helper(root, p, q, &parent)

	return parent
}

func helper(root *TreeNode, p *TreeNode, q *TreeNode, parent **TreeNode) bool {
	if root == nil {
		return false
	}

	left := helper(root.Left, p, q, parent)
	right := helper(root.Right, p, q, parent)

	if left && right && *parent == nil {
		*parent = root
	}
	if (left || right) && (root.Val == p.Val || root.Val == q.Val) {
		*parent = root
	}

	if root.Val == p.Val || root.Val == q.Val {
		return true
	}

	return left || right
}


