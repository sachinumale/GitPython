
# 1. Ternary operator
# a = int(input("Enter 1st No"))
# b = int(input("Enter 2nd No"))
# c = int(input("Enter 3rd No"))
# minimum = a if a<b and b<c else  b if b<c else c
# print(minimum)
#--------------------------------------------------------------

# 2. Product of two number
# a,b,c = [int(x) for x in input("Enter 3 number: ").split()]
# print("Product of 3 number:",a*b*c)

#--------------------------------------------------------------

# n = int(input("Enter number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*i)

#--------------------------------------------------------------

# cart = [10,20,40,500,700,1,2,7,40]
# for x in cart:
#     if x<500:
#         print(x)
#         continue
#     print("not in range",x)

#--------------------------------------------------------------
#Substring program:-

# s = "babjbfjasufhjndfvasopdababananaabab"
# sub = "ab"
# pos = s.find(sub)
# c = 0
# while pos != -1:
#     c = c + 1
#     print("Substring occur at:", pos)
#     pos = s.find(sub,pos+len(sub),len(s))
#
# print('The Number of occurrences:',c)


# s='abcdefabghijkabjkhlm'
# subs='ab'
# c= s.count(subs)
# print('The Number of occurrences:',c)

#
# s=input('Enter Any String to reverse:')
# r=reversed(s)
# output = "".join(r)
# print(output)
# print(s[::-1])

# input: Learning Python is very easy
# output: easy very is Python Learning

#-----------------------------------------------------
# def fact(n):
#     result = 1
#     if n == 1:
#         return result
#     while n > 1:
#         result = result * n
#         n = n-1
#     return result
# n = int(input("Enter number: "))
# print(f"Factorial of number {n} is: ",fact(n))

# def fact(n):
#     result = 1
#     if n == 0:
#         return result
#     else:
#         result = n * fact(n-1)
#     return result

#---------------------------------------------------------
d1 = {100:'durga',200:'ravi',300:'shiva',400:'pavan'}
d2 = {500:'sunny',600:'bunny',700:'chinny'}

# for k,v in d2.items():
# 	d1[k]=v
#
# #d1.update(d2)
#
# print(d1)

#----------------------------------------------------------

from random import *
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits='0123456789'
print(choice(alphabets+digits)+choice(alphabets+digits)+choice(alphabets+digits)+choice(alphabets+digits))

from random import *
otp=''
for i in range(6):
	otp=otp+str(randint(0,9))
print(otp)


from random import *
alphanumeric='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
for i in range(10):
	pwd=''
	for i in range(6):
		pwd=pwd+choice(alphanumeric)
	print(pwd)