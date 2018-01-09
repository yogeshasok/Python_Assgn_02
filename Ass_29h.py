from string import maketrans
init = "hi how are you ?"
print "Using title()"
print "Before using title() :",init
print "After using title() :", init.title()
print "using translate()"
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

print init.translate(trantab)
print "Using upper()"
print init.upper()
print "Using Zfill()"
print init.zfill(100)
str = u"this2009";
print "Using isdecimal()"
print str
print str.isdecimal()
print str
str = u"23443434";
print str.isdecimal()
