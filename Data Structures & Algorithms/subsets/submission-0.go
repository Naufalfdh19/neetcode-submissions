import ("slices")

func subsets(nums []int) [][]int {
	buckets := [][]int{}
	helper(nums, []int{}, &buckets, -1)

	return buckets
}


func helper(nums []int, bucket []int, buckets *[][]int, idx int) {
	*buckets = append(*buckets, slices.Clone(bucket)) 

	for i := idx+1; i < len(nums); i++ {
		bucket = append(bucket, nums[i])
		helper(nums, bucket, buckets, i)
		bucket = bucket[:len(bucket)-1]  
	}
}