func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix[0]), len(matrix)
	check := []int{}

	for	i := 1; i < n; i++ {
		if matrix[i][0] > target && matrix[i-1][0] < target {
			check = []int{i,i-1}
			break
		} else if matrix[i][0] == target {
			check = []int{i}
			break
		} else if matrix[i-1][0] == target {
			check = []int{i-1}
			break
		}
	}

	if len(check) == 0 {
		check = []int{n-1}
	}

	for _, idx := range check {
		for i := 0; i < m; i++ {
			if matrix[idx][i] == target {
				return true
			}
		}	
	}

	return false
}
