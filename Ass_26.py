msg = "Hi How r u?"
en = msg.encode('base64','strict')
print "Message befor Encoding ", msg
print "Message After encoded ", en
dec = en.decode('base64','strict')
print "Message after applying decode ", dec
