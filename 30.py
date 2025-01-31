import numpy as np
npp=np.nan
print(type(npp))


#TUPLE
#tuple is immutable(unhashable)
#the values of tuple will be in ()
t=('nit',0)
print(type(t))

t1=1,2,3,4,5,6      #by default it goes to tuple
print(type(t1))

print(t1.count(7))
print(t1.count(5))

print(t1.index(4))
# print(t1.index(7))       #it show the error of value not in the tuple

print(t1*3)        #it prints the values 3 times

print(t1[:])
print(t1[:3])
print(t1[3:])
print(t1[::-1])
print(t1[::])
print(t1[:100])

for i in t1:
    print(i)

for i in enumerate(t1):
    print(i)

print(t[0][0])
print(t[0][1])
print(t[0][2])
# print(t[0][3])

print(~21)
print(~22)
print(~99)

print(12 & 13)
print(12 and 13)
print(12 | 13)
print(12 or 13)
print(12^13)
print(99^100)
print(101^102)
print(10<<1)     #10*(2**1)
print(10<<2)     #10*(2**2)
print(10>>2)     #10/(2**2)
print(10>>1)     #10/(2**1)

import math               #package:collection of modules
x=math.sqrt(25)           #module:collection of functions
print(x)                  #function

x1=math.sqrt(15)
print(x1)

print(math.floor(3.567))
print(math.ceil(3.567))



#PRACTICE
t2=() #empty tuple
t3=(2,3,4,5) #tuple of int
t4=('hehe','hehehe') #tuple of str
t5=(2.3,3.4,5.5,6.5) #tuple of float
t6=((23,34,45),(45,56,67)) #nested tuple
t7=(2,3.4,'hehe',(67,78,89)) #tuple of mixed data types
print(len(t7)) #prints length of the tuple

#Indexing and Slicing
print(t3[0])
print(t4[0:]) #prints the values from first to last
print(t5[:3]) #prints the values from first to 3rd element
print(t3[-1]) #prints last value

print(t5[0:4]) #prints from 1st element to 3rd element
print(t5[:-1]) #prints from 1st to last but one element
print(t5[::]) #prints all the elements
print(t5[::-1]) #prints all the elements in reverse
print(t5[::-2]) #prints elements ini reverse with step index 2

#Removing and Counting
print(t5.count(5.5)) #counts the no.of repetations of 5.5
print(t5.index(5.5)) #prints the index of 5.5

#Loop
for i in t5:
    print(i)
for i in enumerate(t5): #prints the elements of t5 with indexes in its first argument
    print(i)
    
#Tuple Membership
print(5.5 in t5)  #checks if the given value is in the tuple or not

if 5.5 in t5:
    print('true')
else:
    print('false')

if 9.9 in t5:
    print('true')
else:
    print('false')
    
#Sorting
sorted(t5) #sorts the tuple in ascending order
print(t5)

sorted(t5,reverse=True) #sorts the tuple in descending order
print(t5)