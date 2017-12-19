msg = raw_input("enter the string to count vowels ")
msg = msg.lower()
count = 0
dic = {'a':0,'e':0,'i':0,'o':0,'u':0}
for char in msg :
    if(char == 'a'):
        dic['a']=dic['a']+1
        count = count+1
    elif(char == 'e'):
        dic['e']=dic['e']+1
        count = count+1
    elif(char == 'i'):
        dic['i']=dic['i']+1
        count = count+1
    elif(char == 'o'):
        dic['o']=dic['o']+1
        count = count+1
    elif(char == 'u'):
        dic['u']=dic['u']+1
        count = count+1
print "total vowels in string is ",count
print "Each count is ",dic
