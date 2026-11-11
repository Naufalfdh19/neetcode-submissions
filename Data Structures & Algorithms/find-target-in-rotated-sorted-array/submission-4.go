func search(nums []int, target int) int {
	idx := findMin(nums)

	if target == nums[idx] {
		return idx
	} 

	left := binarySearch(nums,target,0,max(0,idx))
	right := binarySearch(nums,target,idx,len(nums))
	fmt.Println(left,right)
	return max(left,right)
}

func binarySearch(nums []int, target, l, r int) int {
	if nums[l] == target {
		return l
	} 

	for l < r {
		mid := l+(r-l)/2
	
		if nums[mid] < target {
			l = mid+1
		} else if nums[mid] > target {
			r = mid
		} else {
			return mid
		}
	}

	return -1
}

func findMin(nums []int) int {
	l, r := 0, len(nums)-1
	
	for l < r {
		mid := l+(r-l)/2
		if nums[mid] > nums[r] {
			l = mid+1
		} else {
			r = mid
		} 
	}

	return l
}
