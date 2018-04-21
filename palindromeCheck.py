import re
def palindromeCheck(string):
    remSpace = string.replace(" ", "")
    if(remSpace[::-1] == remSpace):
        print("The string is a palindrome:", string)
    else:
        print("The string you have entered is not a palindrome:",string)
    return remSpace

palindromeCheck("ta t")
