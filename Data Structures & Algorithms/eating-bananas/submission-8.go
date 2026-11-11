import ("slices")

func minEatingSpeed(piles []int, h int) int {
		l, r := 1, slices.Max(piles)+1
		minimumRate := math.MaxInt
		for l < r {
			mid := l+(r-l)/2

			if calculate(piles,mid) <= h {
				r = mid
				if minimumRate > mid {
					minimumRate = mid
				}
			} else {
				l = mid+1
			} 
		}	

        return minimumRate
}

func calculate(piles []int, divider int) int {
	tempH := 0
	for i := 0; i < len(piles); i++ {
		numerator := piles[i]
		tempH += int(math.Ceil(float64(numerator) / float64(divider)))
	}

	return tempH
}

