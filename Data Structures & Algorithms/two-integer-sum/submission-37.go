func twoSum(nums []int, target int) []int {
    seenVals := make(map[int] int)

    for i, v := range nums {
        seenVals[v] = i
    }

    for i, v := range nums {
        var dif int = target - v

        val, exists := seenVals[dif]

        if !exists || val == i  {
            continue
        }

        return []int {i, val}
    }
    
    return []int {}
}
