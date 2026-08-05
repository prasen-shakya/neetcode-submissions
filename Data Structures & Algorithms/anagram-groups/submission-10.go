func groupAnagrams(strs []string) [][]string {
	m := make(map[[26]int][]string)

	for _, s := range strs {
		var key [26]int

		for _, c := range s {
			key[c-'a']++
		}

		m[key] = append(m[key], s)
	}

	var result [][]string
	for _, group := range m {
		result = append(result, group)
	}

	return result
}
