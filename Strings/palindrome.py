def isPalindrome(s):
    s = s.lower()
    st = ""
    print(s)
    for i in s:
        x = ord(i)
        if (x>96 and x<123) or (x>47 and x<58):
            st= st+(i)
    print(st)
    if st == st[::-1]: return True
    return False
#steps: lowercase, remove punctuation, check for palindrome

s = "Hello, My Name is anthony gonsalvis.!"
isPalindrome(s)
isPalindrome("0P")