# Includes spaces in the program.
'''
    Function: reverse
    Input: string
    result: reversed version of string
    Input a string of any characters and recieve the reversed version.
'''

def reverse(string):
    temp = string[::-1];
    print(temp)
    return temp

print("TEST CASES")
# With numbers
reverse("123Hello")
# With spaces
reverse(" abc abc abc ")
# With grammar
reverse("hello, my name is Jimmy")
