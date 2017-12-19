test = raw_input("Enter string to check whether it is palindrome ")
test = test.lower()
if(test==test[::-1]):
    print "It is palindrome"
else:
    print "It is not a palindrome"
