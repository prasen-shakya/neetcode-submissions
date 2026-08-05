func isAnagram(s string, t string) bool {
    seen := make(map[rune] int);

    if len(s) != len(t) {
        return false;
    }

    for _, c := range s {
        val, exists := seen[c];

        if exists {
            seen[c] = val + 1;
        } else {
            seen[c] = 1;
        }
    }

    for _, c := range t {
        val, exists := seen[c];

        if !exists {
            return false;
        }

        if val == 0 {
            return false; 
        }

        seen[c] = val - 1;
    }

    return true;
}
