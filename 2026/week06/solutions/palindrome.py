def isPalindrome(a):
    if len(a) == 0 or len(a) == 1:
        return True
    return a[0] == a[len(a) - 1] and isPalindrome(a[1:len(a) - 1])

print(isPalindrome("ata"))
print(isPalindrome("abba"))
print(isPalindrome("abca"))