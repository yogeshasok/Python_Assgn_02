print "Using split()"
init = "       Hi How Are You ? bro \n how do you do it?           "
arr = init.split(" ")
print arr
print "Using splitlines() "
print init.splitlines()
print "USing startswith() "
print "Whether string starts with 'hi' :",init.startswith('Hi')
print "Using strip()"
print "Before using strip ", init ,"with spaces both side"
print "After using strip()", init.strip() ,"Without any spaces "
print "USing swapcase() "
print init.swapcase()
