func search(nums []int, target int) int {
	l := 0
	r := len(nums) - 1

	// Find pivot
	for l < r {
		m := (l + r) / 2

		if nums[m] > nums[r] {
			l = m + 1
		} else {
			r = m
		}
	}

	pivot := l

	// Pick correct half
	if pivot == 0 {
		l = 0
		r = len(nums) - 1
	} else if target >= nums[0] && target <= nums[pivot-1] {
		l = 0
		r = pivot - 1
	} else {
		l = pivot
		r = len(nums) - 1
	}

	// Binary search
	for l <= r {
		m := (l + r) / 2

		if nums[m] == target {
			return m
		} else if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	return -1
}