func isPalindrome(s string) bool {
	newS := []rune{}

	for _, letter := range s {
		if isAlnum(letter) {
			newS = append(newS, letter)
		}
	}
	
	cleanedS := strings.ToLower(string(newS))

	l, r := 0, len(cleanedS)-1

	for l < r {
		if cleanedS[l] != cleanedS[r] {
			return false
		}

		l+=1
		r-=1
	} 

	return true
}

func isAlnum(r rune) bool {
    return unicode.IsLetter(r) || unicode.IsDigit(r)
}

