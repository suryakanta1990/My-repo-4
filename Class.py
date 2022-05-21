# Example-1
# class MyClass:
#     def Myfun(self):
#         return
#     print("this is class")
# mc=MyClass()

# Example-2
'''class myclass:
    def func(self):
        pass
    def display(self,name):
        print(name)
mc=myclass()
mc.display("john")

# Ex-3 static method & instance method
class Myclass:
    def myfun1(self):
        print("this is instance method...")
    @staticmethod
    def myfun2(self,num):
        print("this is static method:",self,num)
m1=Myclass()
m1.myfun1()
m1.myfun2(100,200)

class Myclass:
    def m1(self):
        print("hi")
    @staticmethod
    def m2(num):
        print(num)
mc=Myclass()
mc.m1()
mc.m2(100)'''
# ------------------------------------------
# class variable.
# -----------------
# Ex-1
# class Myclass:
#     a,b=10,20
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# Myclass().add()
# Myclass().mul()

# Ex-2

# i,j=15,25   #global variable
# class m1:
#     a,b=10,20   # class variable
#     def display(self,x,y):
#         print(self.a+self.b)    #local variable
#         print(i+j)
#         print(x+y)
# m1().display(30,40)

#Ex-3
# a,b=100,200
# class myclass:
#     a,b=300,400
#     def c1(self,a,b):
#         print(a+b)  #access local variable
#         print(self.a+self.b)    #access class variable
#         print(globals()['a']+globals()['b'])    #access global variable
# mc=myclass()
# mc.c1(500,600)





