
s = "TACOCAT" 

#if s == s[::-1]:
#    print("Palindrome")
#else: 
#    print("No Palindrome")


def check_palindrome(s):
    stack = []
    for i in range(len(s)//2): 
        stack.append(s[i])

    if len(s) % 2 == 0:
        j = len(s) // 2
    else: 
        j = len(s) // 2 + 1

    for i in range(j, len(s)): 
        if s[i] != stack.pop():
            print("Not a palindrome")
            return -1 
    
    if stack == []:
        print("Palindrome")
        return 1
    else: 
        print("Not a palindrome")
        return -1 

check_palindrome("TACOCAT")