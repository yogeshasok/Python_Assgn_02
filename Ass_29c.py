print "using alpha()"
msg = "make of the year"
print "String ",msg ,"is alphanumeric", msg.isalpha()
msg = "makeoftheyear"
print "String ",msg ,"is alphanumeric", msg.isalpha()

print "Using isdigit(),islower(),isspace()"
msg = raw_input("Enter String to check")
if(msg.isdigit()):
    print "Yes it is digit"
elif(msg.islower()):
    print "String is in lowercase"

elif(msg.isspace()):
    print "Only white space avail"


print "Using isnumeric()"
num = u"1233"

if(num.isnumeric()):
    print "It is numeric"
