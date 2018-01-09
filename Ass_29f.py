print "Using replace()"
initial = "Hello how are you mark ?        "
sub = "Hi"
print "Before Replace :" ,initial
res = initial.replace("Hello",sub)
print "After replacing hello with hi :", res 
print "Using rfind()"
print "Place of 'o' in sentence ", initial.rfind('o')
print "Using rindex()"
print "Index of 'a' in sentence , ", initial.rindex('a')
print "Using rjust()"
print initial.rjust(100,"@")
print "Using rstrip()"
print "String before strip :", initial , "With spaces in right"
print "String after strip  :", initial.rstrip() , "without spaces in right"
