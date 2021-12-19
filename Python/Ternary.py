# class P:
#     def m1(self):
#         print("Parent class method")
# class C(P):
#     def m1(self):
#         super().m1()
#         print("Child class method")
# c = C()
# c.m1()

# s = "shrikrushna"
# i = len(s)-1
# r = ""
# while i>=0:
#     r = r+s[i]
#     i = i-1
# print(r)

#
# l = [1,2,3,4,5,6,78,99,0,1]
# max = l[0]
# max1 = []
#
# for i in range(1,len(l)):
#     if l[i]>max:
#         max1 = max
#         max = l[i]
# print(max1)

#Operator overloading
# class Book:
#
#     def __init__(self,page):
#         self.page = page
#
#     def __add__(self, other):
#         result  = self.page + other.page
#         rbook = Book(result)
#         return rbook
#     def __str__(self):
#         return str(self.page)
# #
# b1 = Book(10)
# b2 = Book(20)
# print(b1+b2)

#Method overloading
# class AA:
#     def m1(self,arg1):
#         print("This is m1 method")
#     def m1(self,arg1,arg2):
#         print("This is m1 method with arg1")
#     def m1(self,arg1,arg2,arg3):
#         print("This is m1 method with arg1,arg2 & arg3")
# a = AA()
# a.m1(1,2,3)


# Abstraction
# from abc import *
# class Vehical(ABC):
#     @abstractmethod
#     def getNoofWheel(self):
#         pass
# class Bus(Vehical):
#     def getNoofWheel(self):
#         return 6
#
# b = Bus()
# print(b.getNoofWheel())


# a  =3,4,5
# print(a)
#
# b1,b2,b3 = a
# print(b1,b2,b3 )






# class Parent1:
#     def __init__(self,a):
#         self.a = a
#     def m1(self):
#         print("Parent1 class m1 method")
#
#
# class Parent2:
#     def __init__(self,b):
#         self.b = b
#     def m2(self):
#
#         print("Parent2 class m2 method")
#
# class Child(Parent1,Parent2):
#     def __init__(self,e):
#         self.e = e
#
#     def m3(self):
#         super().__init__(20)
#
#         print("Child class m3 method")
#         print(self.e)
#         print(self.b)
#
#
#
# c = Child(10)
# c.m1()
# c.m2()
# c.m3()
# print(c.a)

n1 = input("Enter strng:")
if n1 == n1[ : :-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# n1 = input("Enter string:")
#
# result = lambda n1: n1 == n1[::-1]
#
# print("Palindrome")







# n1 = input("Enter strng:")
# r1 = reversed(n1)
# print(r1)
# rev = "".join(r1)
# if n1 == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# class Parent:
#     def __init__(self):
#         self.__a1 = 10
#
#
#     def __m1(self):
#         print("This is Private method")
#
#     def m2(self):
#         print(self.__a1)
#         print(self.__m1())
#         self._d = 30
#
# class Child(Parent):
#     def m3(self):
#         print(self._d)
#
#
# p = Parent()
# p.m2()
# print(p._d)
# # print(p.__a1)
# # Parent(p.__m1())















