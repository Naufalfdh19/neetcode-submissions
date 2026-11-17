/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	var startNodes []*TreeNode
	startNodes = searchTheNode(root, subRoot, startNodes)

	if len(startNodes) == 0 {
		return false
	}

	for _, startNode := range startNodes {
		if helper(startNode, subRoot) {
			return true
		}
	}

	return false
}

func helper(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil && subRoot == nil {
		return true
	}

	if root != nil && subRoot == nil {
		return false
	} else if root == nil && subRoot != nil {
		return false
	} else if root != nil && subRoot != nil {
		if root.Val != subRoot.Val {
			return false
		}
	}

	left := helper(root.Left, subRoot.Left)
	right := helper(root.Right, subRoot.Right)

	return left && right
}

func searchTheNode(root *TreeNode, subRoot *TreeNode, startNodes []*TreeNode) []*TreeNode {
	if root == nil {
		return startNodes
	}

	startNodes = searchTheNode(root.Left, subRoot, startNodes)
	startNodes = searchTheNode(root.Right, subRoot, startNodes)

	if root.Val == subRoot.Val {
		startNodes = append(startNodes, root)
	}
	return startNodes
}
