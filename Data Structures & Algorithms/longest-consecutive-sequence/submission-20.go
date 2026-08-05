func longestConsecutive(nums []int) int {
    longestCount := 0

	numList := make(map[int]bool)

	for _, v := range nums {
		numList[v] = true
	}

	for num := range numList {
		currentNum, curLongest := num, 1
		for numList[currentNum + 1] {
			curLongest++
			currentNum += 1
		}
		longestCount = max(curLongest, longestCount)
	}

	return longestCount
}