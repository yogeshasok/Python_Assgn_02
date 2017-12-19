print "Using Capitalize "
st = "yogesh waran"
print "Before Capitalize ", st
print "After Capitalize ", st.capitalize()


print "Using center ()"
sam = "Welcome To the Shop"
print sam.center(100,'*')


print "Using count() "
sub = "I do not like to repeat success , I like to go on other things"
print "Count of like in string is", sub.count('like')


print "Using Encode and decode"
msg = "Hi How r u?"
en = msg.encode('base64','strict')
print "Message befor Encoding ", msg
print "Message After encoded ", en
dec = en.decode('base64','strict')
print "Message after applying decode ", dec
