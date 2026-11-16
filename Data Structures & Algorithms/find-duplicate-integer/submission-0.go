import ("slices")

func findDuplicate(nums []int) int {
    slices.Sort(nums)

	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			return nums[i]
		}
	}

	return -1
}
