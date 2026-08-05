func findMin(nums []int) int {
	var left int = 0
	var right int = len(nums) - 1

	
	for left < right {
		var mid int = (left + right) / 2

		if nums[mid] > nums[right] {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return nums[left]
}
