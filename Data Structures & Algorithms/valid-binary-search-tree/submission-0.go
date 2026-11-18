/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
    bstArr := []int{}

	inorder(root,&bstArr)

	for i := 1; i < len(bstArr); i++ {
		if bstArr[i] <= bstArr[i-1] {
			return false
		}
	}	

	return true
}

func inorder(root *TreeNode, bstArr *[]int) {
	if root == nil {
		return
	}

	inorder(root.Left,bstArr)
	*bstArr = append(*bstArr, root.Val)
	inorder(root.Right,bstArr)
}

