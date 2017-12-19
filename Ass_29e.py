from string import maketrans
msg = raw_input("Enter the Sample String wiht leading space : ")
print "Convert to lowercase ", msg.lower()
print "To remove leading white space",msg.lstrip()
print "Maximum character in string is ", max(msg)
print "Minimum character in string is ", min(msg)

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print str.translate(trantab)
