import math
import random
n = 0.543
print "Round of ",n ,"is " ,round(n)


num = 25
print "Square root of number ", num ,"is ",math.sqrt(num)

print "Random number between 0 and 9 is ",random.randrange(0,9)


print "Random number between 10 and 500 using uniform ",random.uniform(10,500)

ab = -20
print "Absolute value of ", ab , "is ", abs(ab)

fl = 10.6
print "Ceil and Floor value of ", fl , "is ", math.ceil(fl), math.floor(fl)

print "Comparing two vlaues using cmp(x,y) cmp(80,100) ", cmp(80,100)

print "Using Exponential math.exp(100.12) ", math.exp(100.12)

print "Using pow(x,y) pow(2,3)",math.pow(2,3)

print "Using log10 function log10(100) ",math.log10(100)

print "Using min and max in (10,23,45,56,2,35,87) ", min(10,23,45,56,2,35,87) , max(10,23,45,56,2,35,87)


lis = [10,24,43,52,37,87]
print "Using Choice in random [10,24,43,52,37,87] ", random.choice(lis)

print "Using random() function ", random.random()

print "Using Seed function set 10"
random.seed(10)
print "After Seed() Value of random() is ", random.random()

print "Before Applying shuffle,  list is ", lis
random.shuffle(lis)
print "After Shuffle() ", lis
