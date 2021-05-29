def checkPalindrome(inputString):
    copy = inputString[::-1] # Don;t need to make a copy of a string. [::-1] reverses it
    if copy == inputString: # palindromes match if reversed
        return True
    else:
        return False