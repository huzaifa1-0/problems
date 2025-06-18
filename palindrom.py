def palindrome(s: str) -> bool:
    return s == s[::-1]

print(palindrome('madam')