def palindrome(text):
    if len(text) <= 1:
        print('palindrome')
    else:
        if text[0] == text[-1]:
            palindrome(text[1:-1])
        else: 
            print('not a palindrome')

palindrome("abba")