func findMin(nums []int) int {
	var left int = 0
	var right int = len(nums) - 1

	var currentMin int = 9999
	
	for left <= right {
		var mid int = (left + right) / 2

		currentMin = min(nums[mid], currentMin)

		if nums[left] <= nums[right] {
			currentMin = min(nums[left], currentMin)
		}

		if nums[mid] >= nums[left] {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return currentMin
}
