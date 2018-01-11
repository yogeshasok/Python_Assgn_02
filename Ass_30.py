ran = int(input("Enter the number of elements\n"))
lis = []
for i in range(ran):
    num = int(input())
    lis.append(num)
print lis
sort = []
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if(lis[i]>lis[j]):
            temp = lis[j]
            lis[j] = lis[i]
            lis[i] = temp
print lis
