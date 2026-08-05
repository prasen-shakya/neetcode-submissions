func twoSum(nums []int, target int) []int {
    seenVals := make(map[int]int) // parentheses should be square brackets

    for i, v := range nums {
        seenVals[v] = i
    }

    for i, v := range nums {
        dif := target - v
        val, exists := seenVals[dif] // use := to declare new variables

        // Make sure we don't use the same element twice
        if exists && val != i {
            return []int{i, val} // correct slice literal syntax
        }
    }

    return nil // in case no solution is found
}