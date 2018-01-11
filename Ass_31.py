limit = int(input("Enter the limit \n"))
lis = []

for i in range (limit):
    lis.append(int(input()))
lis.sort()

flag = 0
num = int(input("Enter number to check  :"))
left = 0
right = len(lis)-1
while(left<=right):
    mid = left+(right-left)/2

    if(lis[mid]==num):
        flag = 1
        break
    elif(lis[mid]<num):
        left = mid+1
    else:
        right = mid-1
if(flag == 0):
    print "Unsuccessful "
else :
    print "Success"
