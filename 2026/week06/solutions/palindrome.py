def isPalindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True
    return text[0] == text[len(text) - 1] and isPalindrome(text[1:len(text) - 1])

print(isPalindrome("abba"))
print(isPalindrome("ata"))
print(isPalindrome("abca"))
