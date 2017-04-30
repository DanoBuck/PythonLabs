def isPalindromeIterative(word):
    removeSpacesHolder = word.replace(" ", "")
    reversedWord = reverse(removeSpacesHolder)

    if reversedWord.upper() == removeSpacesHolder.upper():
        print(word.upper(), "reversed is", word.upper(), "- palindrome")
        return True
    print(word.upper(), "reversed is", reversedWord.upper(), "- not a palindrome")
    return False


def reverse(word):
    backward = ""

    for i in reversed(range(len(word))):
        backward += word[i]

    return backward


print("**********Iteratively Checking Palindromes**********\n")
isPalindromeIterative("HELLO")
isPalindromeIterative("Hannah")
isPalindromeIterative("121")
isPalindromeIterative("Al lets Della call Ed Stella")
isPalindromeIterative("No lemon, no melon")

def isPalindromeRecursive(word):
    if word.find(" "):
        word = word.replace(" ", "")
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0].upper() == word[len(word)-1].upper():
        return isPalindromeRecursive(word[1:-1])
    else:
        return False

print("\n*********Recursively Checking Palindromes**********\n")
print("Is Hello a palindrome:", isPalindromeRecursive("HELLO"))
print("Is Hannah a palindrome:", isPalindromeRecursive("Hannah"))
print("Is 121 a palindrome:", isPalindromeRecursive("121"))
print("Is Al lets Della call Ed Stella a palidrome:", isPalindromeRecursive("Al lets Della call Ed Stella"))
print("Is No lemon, no melon a palindrome:", isPalindromeRecursive("No lemon, no melon"))

