# def is_palindrome(word) :
#     reversed_word = word[::-1] 
#     if word == reversed_word :
#         return True
#     else:
#         return False

# def is_palindrome(word) :
#     if word == word[::-1] :
#         return True
#     return False

def is_palindrome(word) :
    return word == word[::-1]

print(is_palindrome("sourav"))
print(is_palindrome("naman"))
