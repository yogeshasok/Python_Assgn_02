print "using endswith() "
str1= "Yogesh Asokan"
print "Main String: ", str1
print "Suffix to search: Asokan"
if(str1.endswith('Asokan')):
    print "You are right person"
else:
    print "You are not authorized"


print "Using expandtabs() "
str1 ="Hi\tHello How are you"
print "Normal tab :",str1
print "Extended tab :" ,str1.expandtabs(10)


print "Using find() "
msg = "This is an example for an find function"
print"From 0th index ", msg.find('func')
print "From 20 th index ", msg.find('func',20)
print "From 34 th index ", msg.find('func',34)

print "Using index()"
print "Index of func in ", msg ,"is ",msg.index('func')

msg = "year2017"
print "String ",msg ,"is alphanumeric", msg.isalnum()
msg = "year 2017"
print "String ",msg ,"is alphanumeric", msg.isalnum()
