func groupAnagrams(strs []string) [][]string {
	seen := make(map[string][]string)

	for _, v := range strs {
		// sort the string
		r := []rune(v)
		sort.Slice(r, func(i, j int) bool {
			return r[i] < r[j]
		})
		key := string(r)

		seen[key] = append(seen[key], v)
	}

	var result [][]string
	for _, group := range seen {
		result = append(result, group)
	}

	return result
}
