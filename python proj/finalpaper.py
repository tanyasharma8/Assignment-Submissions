# l=[10,2.5,30,45,50,5.5]
# print(sum(l))
# # print(l[-2:-1])
# def lists(l):
#     s=1
#     for i in l:
#         s*=i
#     return s
# print(lists([2,2,3]))

# l= ['abc', 'xyz', 'aba', '1221']
# for i in l:
#     if len(l)>=2 and i[0]==i[-1]:
#         print(l.index(i))

# l= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# l[1].sort()
# print(l)
# def li(a):
#     return a[-1]
# def sort(t):
#     print(sorted(t,key=li))
# print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))



# a = [10,20,30,20,10,50,60,40,80,50,40]
# s=set(a)
# print(s)
# l2=list(s)
# print(l2)

# def comman(l1,l2):
#     retur=False
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 retur=True
#     return retur
# print(comman([1,2,3,4,5], [5,6,7,8,9]))

# l=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # Expected Output : ['Green', 'White', 'Black']
# l.remove('Red')
# l.remove('Pink')
# l.remove('Yellow')
# print(l)

# l=[1,2,3,4,5,6,7,8]
# for i in l:
#     if i%2==0:
#         l.remove(i)
# print(l)

# Write a Python program to generate and p rint a list of firstand last 5 elements where the values are square of numbers between 1 and 30 (both included). 

# l=[x**2 for x in range(1,31)]
# print(l)
# l1=l[1:6]
# l2=l[25:]
# new=l1+l2
# print(new)



# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
# s1=set(list1)
# s2=set(list2)

# print(list(s1.difference(s2))+(list(s2.difference(s1))))


# l=['a','b','c']
# str=''.join(l)
# print(str)

# l=[1,8,2,-1,2,3,-2]
# l.sort()
# print(l[-2])




# def second_largest(numbers):
#   if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()    
#   return  uniq_items[-2]   
# print(second_largest([1,2,3,4,4]))

# from tempfile import tempdir


# l=[10,20,22,90,12,88,32,12,84,30,50,40,60,37,9]
# print(l[::-1])
# def func(l,min,max):
#     c=0
#     for i in l:
#         if min<=i<=max:
#             c+=1
#     return c
# print(func(l,50,100))
# def swap(l):
#     temp=l[0]
#     l[0]=l[-1]
#     l[-1]=temp
#     return l
# print(swap(l))



# tuple
# t=1,2,3,4
# print(type(t))

# t= (1, 2) 
# t2=(2, 3)
# t3=(3, 4)


# # for i in t:
# #     list(i)

# def tuple(l):
#     res=[sum(i) for i in l]
#     return res
# print(tuple(t))

# t=(('Red', 'White'/
    # if'Olive' in i:

# t=('a','b','c')
# str=''.join(t)
# print(str)\

# t=(1,2,3,4,5,6,7,8,9,0,7,5,412,12,34,444444444)
# print(t[3])
# print(t[::-1])

# l= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# def replcae(l):
#     re=[list(i) for i in l]
#     for i in re:
#         i[-1]=100
#     return l
# print(replcae(l))
# tT1 = (1, 2, 3, 4, 5, 6, 7, 8)
# print(tT1[-5:-2])











# a. (2xy-9y/2xy3 )-(4yx2/2y)
# b. log(x)-log(y)

# import math
# x=eval(input())
# y=eval(input())
# res=(2*x*y-9*y/2*x*math.pow(y,3))-(4*y*math.pow(x,2)/2*y)
# print(res)
# re2=math.log(x)-math.log(y)
# print(re2)


# s=input('Enter the string:')
# if len(s)>=10:
#     print(s.upper())
# else:
    # print(s.lower())



# s1=input()
# # s2=input()
# # if len(s1)>len(s2):
# #     print(s1)
# # else:
# #     print(s2)
# if len(s1)>=3:
#     if s1[-3:]=='ing':
#         print(s1+'ly')
#     else:
#         print(s1+'ing')
# else:
#     print(s1)

# for i in range(1,21):
#     if i%3==0 and i%5==0:
#         print('AGC College')
#     elif i%3==0:
#         print('AGC')
#     elif i%5==0:
#         print('College')










# Dictionary

# from ast import While
# from cProfile import label
# from functools import reduce
# from pstats import SortKey
# from re import L
# import string
# from tempfile import tempdir
# from turtle import color

# from pyparsing import col


# di={1:'Tanya',2:'Akshit'}
# d=dict(a=1,b=2,c=3)
# d={k:v for k,v in (('a',1),('b',2))}
# print(d)
# print(type(d))
# d.update({'a':100})
# print(d)


# d={'Name':'Tanya','Age':20,'Class':'CSE'}
# print(d.keys())
# print(d.values())
# print(d.items())
# d['Name']='Akshit'
# d['city']='Amritsar'
# d['marks']=[10,9,8]
# d['marks'].append(5)
# del d['Age']
# d.pop('Class')
# print(d)
# print(len(d))
# d2=d.copy()
# print(d2)

# d.update(di)
# print(d)
# print(di)


# d={'physics','maths','science'}
# d=dict.fromkeys(d,'N')
# print(d)




# d1={1:'Amit',2:'Suman'}
# d2={4:'Tanya',5:'Akshit'}
# d3={}
# for i in (d1,d2):
#     d3.update(i)
# print(d3)

# def check(d,k):
    
#     if k in d.keys():
#         print('Present')
#     else:
#         print('Absent')
# check(d1,1)
# # d1[3]='Tanya'
# # print(d1)

# d1={1:'Amit',2:'Suman',3:'Amit'}
# md={}
# for k,v in d1.items():
#     if v not in md.values():
#         md[k]=v

# print(md)


# d={}
# for i in range(2):
#     id=int(input())
#     bname=input()
#     bprice=int(input())
#     l=[]
#     l.append(bname)
#     l.append(bprice)
#     d[id]=l
# print(d)

# d={}
# s=0
# for i in range(2):
#     rn=int(input("Enter Roll Number:"))
#     nm=input('Enter Name:')
#     marks=int(input("enter Marks"))
#     d1={}
#     d1[nm]=marks
#     d[rn]=d1
    
# print(d)


# for k,v in d.items():
#     for i in v.values():
#         s=s+i
# print(s)






# Sample Dictionary :
# dic1={1:10, :20}
# for k,v in dic1.items():
#     print(f'{k2}={v}')
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in (dic1,dic2,dic3):
#     dic4.update(i)
# print(dic4)

# d={1:{'Name':'John','Age':'27'}
#     ,2:{'Name':'Marie','Age':'22'}
# }

# for i in d.keys():
#     print(i)
# for i in d.values():
#     for j in i.keys():
#         print(j)
# for i in d.values():
#     for k,v in i.items():
#         print(f'{k}={v}')

# a=13
# b=9
# c=12
# print(a|b|c)
# print(a&b&c)
# print(a^b^c)

# print(~a)
# print(a>>3)











# 2. Write a program of guessing game between 1-12. If got 9 → win, less than 9 → Lower than winning number and more than 9 → higher than winning number. 

# import random


# n=random.randint(1,12)
# if n==9:
#     print('win')
# elif n>9:
#     print('more than winning number')

# else:
#     print('less than winning number')


# Write a program to accept three numbers and print all possible combinations from the digits. 

# a=int(input())
# b=int(input())
# c=int(input())
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if i!=j & j!=k & k!=i:
#                 print(d[i],d[j],d[k])






# dataframe
# using list
# import pandas as pd
# d={'Name':['Tanya','Akshit'],'Age':[20,22]}
# # # l=[['name','age'],['Tanya',20],['Akshit',22]]
# df=pd.DataFrame(d,index=['Student1','student2'])
# # print(df)

# # d=pd.read_csv("D:\python proj\detail.csv")

# # d=pd.read_excel("D:\python proj\b2.xlsx")
# print(df.shape)
# print(df.head(1))
# print(df.tail(0))







# import pandas as pd 
# import numpy as np
# d=pd.DataFrame({
#     'One':[100,200,102],
#     'Two':[400,np.nan,250],
#     'Three':[90,150,np.nan],
#     'Born':[pd.NaT,pd.Timestamp("2002-03-08"),pd.NaT]
# })
# # df=pd.DataFrame(d)
# # x={'//t(y)
# # y=df.fillna(method='bfill')
# # print()
# # print(y)
# # print(d)
# for i in d.iteritems():
#     print()
#     print(i)
#     print()






# import pandas as pd
# import matplotlib.pyplot as plt
# d={'Name':['Tanya','Akshit'],'Age':[20,22]}
# df=pd.DataFrame(d)
# print(df)
# df.plot(kind='line',x='Name',y='Age')
# plt.show()
















# functions

# LAMBDA FUNCTIONS

# x=lambda i:i%2==0
# print(x(289))

# l=[1,2,3]
# x=list(map(lambda i:i**2,range(1,21)))
# print(x)

# x=list(filter(lambda a:a%2==0,range(1,11)))
# print(x)


# l=[1,6,3,55,22,0,10]
# x=list(filter(lambda i:i%5==0,l))
# print(x)

# scores=[666,909,686,595,767,606,888,747,818,656]
# x=list(filter(lambda i:i>700,scores))
# print(x)

#
# #
# l=['666','909','559','676','560','888','174','181','165']
# x=list(filter(map(lambda i:i[0]==i[2],l)))
# print(l)





# import sys
# l=['a',0,1]

# for i in l:
#     try:
#         print('The ENtry is:',i)
#         r=1/int(i)
#         break
#     except:
#         print('Oops!',sys.exc_info()[0],'occured')
#         print('Next Entry')
#         print()

#     print('The reciprocal of',i,r)

# while True:

#     try:
#         entry1=int(input('Enter The Value:'))
#         r=1/int(entry1)
#     except ValueError:2

#         print('Oops! ErrorOccured')
#     except ZeroDivisionError:
#         print('Oops! ErrorOccured')
#     else:
#         print('the reciprocal of ',entry1,' is ',r)



# try:
#     age=int(input())
#     if age<0:
#         raise ValueError()
# except:
#     print('-ve value entered')
# else:
#     print(age)

# def avg(marks):
#     assert len(marks) != 0,'length of  marks cant be zero'
#     return sum(marks)/len(marks)
# mark1 = []
# print("Average of mark1:",avg(mark1))


# myfile=open('neha.txt','r')
# print(myfile.read(4))
# # myfile.write('Hi Neha Good to see you')
# myfile.close()
# # print('Successfully done')






# myfile=open('nehap.txt','w')
# myfile.write('hi to line one')
# myfile.write('hi to line two')
# myfile.close()
# print('Successfully written in file')
# myfile2=open('nehap.txt','a')
# myfile2.write('HI THERE')
# myfile2.close()
# # print(myfile2.readline())
# print(myfile2.readline())
# myfile2.close()


# def main():
#     myfile=open('neha12.txt','w')
#     myfile.write("hi hoe are you")
# main()



# filename=input("enter filename:")
# obj=open(filename)
# x=obj.read()
# c=0
# for char in x:
#     if char=='A' or char=='a' or char=='I' or char=='i' or char=='E'or char=='e' or char=='O' or char=='o':
#         c=c+1
#     print(c)


# import csv
# csvData=[['Name','Age'],['Tanya',20],['Akshit',22]]
# csvfile=open('1.csv','w')
# wfile=csv.writer(csvfile)
# wfile.writerows(csvData)
# print('Data wriiten')
# csvfile.close()



   


# import random 

# myfile=open('mst.txt','w')
# for i in range(51):
#     i=random.randint(500,1000)
#     myfile.writelines(str(i)+'\n')
# myfile.close()
# print('succesfully written')

# myfile2=open('mst.txt','r')
# i=myfile2.readlines()
# # print(i)
# for w in i:
#     if int(w)%5==0  and int(w)%3==0:
#         print(w)
# myfile2.close()
 


      

# line graph

# import matplotlib.pyplot as mat

# x=[1,2,3]
# y=[4,1,8]
# mat.plot(x,y,label='First',color='k',marker='D',markerfacecolor='r',ls='-.',lw=3)
# mat.xlabel('Cost')
# mat.ylabel('Speed')
# mat.title('Line Graph')
# mat.legend()
# mat.show()


# views=[534,256,689,401,724,689,350]
# days=range(1,8)
# mat.plot(days,views,label='Youtube Viewership',color='k',marker='D',markerfacecolor='r',ls='-.',lw=3)
# mat.xlabel('Number of days')
# mat.ylabel('Youtube views')
# mat.title('Youtube Views Analysis')
# mat.legend()
# mat.savefig('D:/python.pdf',format='pdf')
# mat.show()


# ploting 2 lines

# x1=[1,3,5]
# y1=[6,9,3]
# x2=[1,3,5]
# y2=[3,7,9]
# mat.plot(x1,y1,label='First',color='r')
# mat.plot(x2,y2,label='Second',color='g')
# mat.xlabel('Cost')
# mat.ylabel('Speed')
# mat.legend()
# mat.show()


# pie graph

# import matplotlib.pyplot as mat

# # x=[12,55,33,77,35]
# # y=['java','c','c++','python','php']
# # color=['orange','blue','purple','cyan','g']
# # # ex=[0,0,0,0,0.2]
# # mat.pie(x,labels=y,colors=color,autopct='%1.1f%%',startangle=90)
# # # mat.legend()
# # mat.show()


# # x1=[1,2,3,4,5]
# # x2=[11,12,13,14,15]
# # y=[5,2,1,3,6]
# # mat.scatter(x1,y,label='cost p',color='cyan')
# # mat.scatter(x2,y,label='selling p',color='r')
# # mat.xlabel('cost')
# # mat.ylabel('sell')
# # mat.title('scatter')
# # mat.legend()
# # mat.show()







# # viewers=[10,20,11,55,33]
# # age=[10,22,55,23,29]
# # mat.hist(viewers,age,color='r',rwidth=10)
# # mat.title('histogram')
# # mat.show()





# import matplotlib.pyplot as mat

# youtube_views=[534,258,689,401,724,689,350]
# facebook_views=[123,342,700,304,405,650,325]
# days=range(1,8)

# mat.plot(days,youtube_views,label='Youtube views',color='cyan',lw=4)
# mat.plot(days,facebook_views,label='Yfacebook views',color='r',lw=4)

# mat.xlabel('Number of Days')
# mat.ylabel('Views')
# mat.title('Analysis Graph')
# mat.legend()
# mat.show()





# overloading of binary operator

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __add__(self,o):
#         return self.a + o.a,self.b + o.b

# o=A(2,1)
# o2=A(7,3)
# o3=o+o2
# print(o3)



# overloading of comparison op./


# class A:
#     def __init__(self,a):
#         self.a=a

#     def __isub__(self,o):
#         if self.a==o.a:
#             return True
#         else:
#             return False

# obj1=A(1827)
# obj2=A(8765)
# if obj1==obj2:
#     print('obj1 is equal to obj2')
# else :
    # print('obj 2 is not equal to obj 1')




# class A:
#     def __init__(self, a):
#         self.a = a
 
#     # Overloading ~ operator, but with two operands
#     def __neg__(self):
#         # return "This is the ~ operator, overloaded as binary operator."
#         x=-self.a
#         return x 
# ob1 = A(2)
# # ob2 = A(3)
 
# print(-ob1)

# class A:
#     def __init__(self,a):
#         self.a=a

#     def __iadd__(self,o):
#         self.a += o.a
#         return self.a
# o=A(2)
# o2=A(7)
# o+=o2
# print(o) 









# class base:
#     def __init__(self,name):
#         print('My Name is ',name)

# class base2:
#     def __init__(self,name):
#         print('I am ',name)

# class derived(base,base2):
#     def __init__(self):
#         print('I am derived Class')
#         super().__init__('Zara')
#         base2.__init__(self,'Tanya')



# ob=derived()
# print(derived.__mro__)


# class A:
#     # __amount=45

#     # def hello(self):
#     #     print('Amount is ',A.__amount)

#     def __init__(self,a,b,c):
#         self.a=a
#         self._b=b
#         self.__c=c





# onj=A(1,2,3)

# print(onj.a)
# print(onj._b)
# print(onj._A__c)


# class stu:
#     def print1(self):
#         print('p1')
# class b(stu):        
#     def print1(self):
#         print('p2')
# c=b()
# c.print1()
# # c.print1(9)




# class Vector:
#     def __init__(self, x_comp, y_comp):
#         self.x_comp = x_comp
#         self.y_comp = y_comp

#     def __abs__(self):
#         return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5
# vector = Vector(3, 4)
# print
# 
# 




# (abs(vector))
# # 5.0

# import matplotlib.pyplot as mat

# # facebook_views=[1000,1500,1800,1900,2200,6754,1777,2100,677,2000]
# youtube_views=[678,1777,3241,2434,1899,4567,5641,1890,888,2300]
# y=[1,2,3,4,5,6,7,8,9,10]
# # mat.hist(facebook_views,y,label='facebook views',color='r',rwidth=10)
# mat.hist(youtube_views,y,label='youtube views',color='cyan',rwidth=10)
# mat.title('histogram')
# mat.legend()
# mat.show()


# word=['one','one','two','three','three']
# w=[]
# for i in word:
#     if i not in w:
#         w.append(i)

# print(w)


# class A:
#     def getdata(self):
#         self.a=input('ENter the string:')
#     def putdata(self):
#         return self.a
# obj=A()
# obj.getdata()
# print(obj.putdata())


# s='computer'
# str=list(s)
# for i in s:



# import pandas as pd

# # using list
# l=[['Name','Age'],['Tanya',20],['Vanshita',19],['Souvik',19]]

# df=pd.DataFrame(l)

# print(df)



# import pandas as pd
# import numpy as np
# d={'Name':['Tanya','Vanshita','Souvik'],'Age':[20,19,19]}
# df=pd.DataFrame(d)
# print(df)

# d={
#     'A':[100,200,np.nan],
#     'B':[np.nan,250,120],
#     'C':[555,np.nan,np.nan],
#     'D':[pd.NaT,pd.Timestamp("2002-03-08"),pd.NaT]
# }
# df=pd.DataFrame(d)
# for i in df.itertuples():
#     print()
#     print(i)
# # x=df.fillna(method='ffill')
# print(x)
# y=df.fillna(method='bfill')
# print(y)
# a={"A":0,'B':1,'C':2,'D':4}
# y=df.fillna(value=a,limit=1)
# print(y)












# import random
# def rand(n):
#     l=[]
#     for i in range(n):
#         i=random.randint(1,1000)
#         l.append(i)
#         print(l)
#         c=0
#         s=0
#         p=1
#         for j in l:
#            s+=j
#            p*=j
#            avg=s/n
#            if j%2!=0:
#                c=c+1
#     return s,p,avg,c

# print(rand(5))


# def create():
#     l=[]
#     for i in range(int(input())):
#         list_elm=eval(input())
#         if i not in l:
#             l.append(list_elm)
#         else:
#             print('Item already exist')
    
# print(create())






# d={1:{'name':'Tanya','age':20},2:{'name':'Akshit','age':22}}
# print(d[1]['name'])

# d[3]={}
# d[3]['name']='Vanshita'
# d[3]['age']=19
# print(d)

# for i in d:
#     for j in d[i]:

#         print(j,'=',d[i][j])
# print()




# def binary(l,e):
#     beg=0
#     end=len(l)-1
#     mid=(beg+end)//2
#     while beg<=mid:

#         if l[mid]>e:
#             end=mid-1
#         elif l[mid]<e:
#             beg=mid+1
#         else:
#             return mid
#         return False

        

# res=binary([1,2,3,5,22,56,90],90)
# if res!=False:
#     print('Present')
# else:
#     print('ni')










# def selection(l):
#     for i in range(len(l)):
#         min=i
#         for j in range(i+1,len(l)):
#             if l[j]<l[i]:
#                 min=j
#         (l[i],l[min])=(l[min],l[i])
#     return l
# l=[5,1,8,4,23,87]
# print(selection(l))
# # print(l)







# BUBBLE SORT

# def bubble(l):
#     for j in range(len(l)):
#         for i in range(0,len(l)-j-1):

#             if l[i]>l[i+1]:
#                temp=l[i]
#                l[i]=l[i+1]
#                l[i+1]=temp
#     return l

# print(bubble([4,2,6,8,5]))



# SELECTION SORT

# def selectionsor(l):
#     for i in range(len(l)):
#         min=i
#         for j in range(i+1,len(l)):
#             if l[j]>l[i]:
#                 min=j
#         (l[i],l[min])=(l[min],l[i])
#     return l
# print(selectionsor([2,3,1,5,43,9]))
                

# INSERTIONSORT

# def insertionsort(l):
#     for i in range(l):
#         key=l[i]
#         j=i-1
#         while j>=0 and key<l[i]:
#             l[j+1]




# n=int(input("Enter a number: "))
# a=[]
# while(n>0):
#     dig=n%2
#     a.append(dig)
#     n=n//2
# a.reverse()
# print("Binary Equivalent is: ")
# for i in a:
#     print(i,end=" ")

# n=int(input("Enter a binary number: "))
# dec_num=0
# m=1
# length=len(str(n))
# for i in range(length):
#     rem=n%10
#     dec_num+=rem*m
#     m=m*2
#     n=int(n/10)

# # print(dec_num)
# l='computer'
# li=[]
# for i in range(len(l)):
#     if i==3:
#         break
#     li.append(l[i])
# m=','.join(li)
# print(m)


# myfile=open("tanya.txt",'w')
# myfile.write('Hi There to all I \'m technical Head of GEEKFORGEEKS')
# myfile.close()
# print('Sucessfully written')

# myfile=open('tanya.txt','r')
# print(myfile.read())
# myfile.close()
# myfile=open('tanya.txt','a')
# myfile.write('I am really hounuered to be a part of gfg')
# myfile.close()


# import random

# # myfile=open('final.txt','w')
# # for i in range(1,51):
# #     i=random.randint(500,1000)
# #     myfile.write(str(i) + '\n')
# # myfile.close()
# # print('Successfully written')

# myfile2=open('final.txt','r')
# a=myfile2.readlines()
# for i in a:
#     if int(i)%3==0 and int(i)%5==0:
#         print(i)
# myfile2.close()



# def count():
#     # count=0
#     myfile=open('final.txt','w')
#     myfile.write(input('Enter word:'))
#     myfile.close()
#     myfile2=open('final.txt','r')
#     i=myfile2.read()
#     for char in i:

#         c=char.capitalize()
#         print(c)
#     # return c

# print(count())


# import csv
# csvfile=open('detail.csv')
# csv_read_file=csv.reader(csvfile)
# for i in csv_read_file:
    # print(i)
# l=[['Name','Age'],['tanya',20],['Akshit',23]]
# csvfile=open('1.csv','w')
# csvwrite=csv.writer(csvfile)
# csvwrite.writerows(l)
# print('successfully written')
# csvfile.close()
# csvfile=open('1.csv')
# csv_read_file=csv.reader(csvfile)
# for i in csv_read_file:
#     print(i)



# l2=[['Name','Age'],['Vanshita',20]]
# csvfile2=open('1.csv','a')
# csvwritefile=csv.writer(csvfile2)
# csvwritefile.writerows(l2)
# print('successfully written')
# csvfile2.close()
# myfile=open("neha.txt","w")
# myfile.write("hi hw r u")
# myfile.close()
# myfile=open("neha.txt","w")
# myfile.write("hi hw r u123\n")
# myfile.close()
# myfile=open("neha.txt","a")
# myfile.write("hi hw r u567")
# myfile.close()
# print("successfully written")
# myfile1=open("neha.txt","r")
# print(myfile1.read())
# myfile1.close()










# LIST REVISION

# l=['tanya','Akshit','Ajay','Anjali','Nitti','karan','tanya']
# l_c=['Arman','Rayan','ambika']
# print(l)
# print(type(l))
# l.append('Yukti')
# print(l)
# l.insert(5,'Puneet')
# print(l)
# l.extend(l_c)
# print(l)

# l.pop()
# print(l)
# del l[5]
# print(l)
# l.remove('Anjali')
# print(l)

# print(l.count('tanya'))

# l.sort()
# print(l)

# m=','.join(l)
# print(m)


# def squ(l):
#     sq=[]
#     for i in l:    
#         sq.append(i**2)
#     return sq
# print(squ([1,2,3,4,5]))
# li=[1,2,3,4,5]
# l=[i**2 for i in li if i%2==0]
# print(l)

# reverse a list without using reverse function

# l=[1,2,3,4,5]
# ne=[]
# for i in range(len(l)):
#     pop_element=l.pop()
#     ne.append(pop_element)
# print(ne)

# ['abc','tuv']=['cba','vut']
# l=['abc','tuv','xyz']
# re=[]
# for i in l:
#     r=i[::-1]
#     re.append(r)
# print(re)


# l='hi how are you'
# m=l.split()
# print(m)
# j=', '.join(m)
# print(j)


#STRING

# str='Hi I Love programming'
# print(str.lower())
# print(str.upper())
# print(str.title())
# print(str.count('m'))
# print(str.isdigit())
# print(str.isalnum())
# print(str.isalpha())
# print(str.capitalize())
# print(str.replace('p','P'))
# print(str)
# print(str.find('I'))




# name=input('Enter your name:')
# for i in range(0,len(name)):
#     print(f'{i}:{name.count(i)}')

# winning_num=43
# guess=1
# n=int(input('Guess number between 1 and 100='))
# game_over=False
# while True:
#     if n==winning_num:
#         print('right guess')
#         break

#     else:
#         if n>winning_num:
#             print('high number guessed')
#         else:
#             print('low number guessed')
#         guess+=1
#         n=int(input('Try again  by entering one more time:'))

  
# name='Tanya'
# for i in range(len(name)):
#     print(i])






# def is_palindrom(name):
#     rev=name[::-1]
#     if name==rev:
#         print('String is palindrome')
#     else:
#         print('Not palindrome')
# is_palindrom('tanya')

# def fibonnaci(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print(a,b,end=' ')
#         for i in range(n):

#             c=a+b
#             a=b
#             b=c
#             print(b,end=' ')
# fibonnaci(5)

# l=[-i for i in range(1,11)]
# print(l)
# l=['tanya','vanshita','Samridhi']
# k=[i[:1] for i in l]
# print(k)

# l=[True,False,[1,2,3],1,1.0,3]
# req=[]
# for i in l:
#     if type(i)==int or type(i)==float:
#         req.append(i)
# print(req)


# new=[i**2 if i%2==0 else -i for i in range(1,11) ]
# print(new)





# dict={
#     'name':'Tanya','age':20,'course':'cse',
#     'fav_movie':['yjhd','bgmc','kb','a']
# }
# more={
#     'series':['suits','tvd','eip']
# }
# # no INDEXING
# for k,v in dict.items():
#     print(f'{k}={v}')

# dict.update(more)
# print(dict)

# print(dict.get('series'))

# def word_count(str):
#     chr={}
#     for i in str:
#         chr[i]=str.count(i)    #dictname[key]=value
#     return chr
# val=word_count('Tanya') 
# for k,v in val.items():
#     print(f'{k}={v}')
# string='Tanya'
# d={char:string.count(char) for char in string}
# print(d)

# d={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(d)

# myfile=open('ak.txt','w')
# myfile.write('hi i have successfully learned python')
# myfile.close()

# print('written done')

# f=open('ak.txt','r')
# f.seek(20)
# print(f.tell())
# print(f.readline())
# \


# def prime(n):
#     flag=False
#     if n>0:
#         for i in range(2,n//2):
#             if n%i==0:
#                 flag=True
#                 break
#     if flag:
#         print('np')
#     else:
#         print('p')
# prime(31)

# l=['static','madamimadam','cseece','eyes']
# l2=[]
# for i in l:
#     if i==i[::-1]:
#         var1=print('yes',end=' ')
#         l2.append(var1)
#     else:
#         var2=print('no',end=' ')
    
#     l2.append(var2)
# m=','.join(l2)
# print(m)
# c=list(map(lambda i:i==i[::-1] ,l))
# print(c)


# d={'john':33,'Ray':56,'Charlie':78}
# di={key:value for key,value in d.items() if value%2!=0 and value<50 }
# print(di)



# s="computer"
# print(list(s))
# print(tuple(s))
# print('*'.join(s))
# s1=[]
# for i in range(len(s)):
#     if i==3:
#         # s1.append(i)
#         break
#     s1.append(s[i])
# m=','.join(s1)
# print(m)

# a=10
# b=15
# print(bin(b))
# print(bin(a&b))
# print(bin(a|b))
# print(bin(a&b))
# print(bin(a^b))

# print(b)

# import math

# def sphere(r):
#     v=(4*3.14*math.pow(r,3))/3
#     print(v)

# sphere(4)
# 1st=[1,2,3]
# 1st[3]

# myfile=open('ak.txt')
# v=myfile.read()
# for i in v:
#     l=i.capitalize()

#     print(l)
# myfile.close() 

# l=[i**2 if i%5==0 else i  for i in range(100) ]
# print(l)

# A=1,2,3,4
# a,b,c,d=A
# print(d)

# str='I AM LEARNING PYTHON'
# print(str.replace(' ','&'))

# print(str)


# def prime():
#     flag=False
#     a=int(input())
#     b=int(input())
#     for i in range(a,b):
#         if i>0:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#                 else:
#                     print(j)

    
# print(prime())



# while True:
#     try:
#         n=eval(input('The entry is '))
#         res=1/int(n)

#     except ValueError:
#         print('oops! error occured.')
#         print('Next Entry.')

#     except ZeroDivisionError:
#         print('oops! error occured.')
#         print('Next Entry.')


#     else:
#         print(f'Thr reciprocal of {n} is {res}')                                                                                       
#         break




# def enterage(age):
#     assert age>0,"Age cant be negative"
#     print(age)

# enterage(-2)


# import random

# print(random.sample(range(500),5

# import math
# l=[math.sqrt(x) for x in range(1,101) if x%5==0]
# print(l)



# D= {1: 'A', 2: 'B', 3: 'C'}
# d={}

# # for i in D:
# #     d.update(i)
# # print(d)
# d.update(D)
# print(d)



# s='PYTHON'
# l=list(s)
# l.remove('T')
# l.remove('H')
# print(l)
# s2=str(l)
# print(s2)
# m=''.join(l)

# print(m)



# arr=[[1,2],[3,4],[5,6],[7,8]]
# print(arr[0])
# print(arr[0][1])


# create a dynamic matric using for loop

# n=3
# m=4
# a=[0]*4
# for i in range(n):
#     a[i]=[0]*m
# print(a)

# a=int(input("ENTER NUMBER OF ROWS:"))
# b=int(input("ENTER NUMBER OF COLUMNS:"))
# c=[[int(input('Enter element')) for i in range(b)]for j in range(a)]
# for i in range(a):
#     for j in range(b):
#         print(c[i][j],end=" ")
#     print()

# class A:
#     def base(self):
#         print('BASE CLASS')
# class B(A):
#     def de(self):
#         print('DERIVED CLASS')
# class C(A):
#     def d2(self):
#         print('df')

# obj=C()
# obj.de()
# obj.base()
# # obj.d2()
# class A:
#     def __init__(self,name):
#         print('CLASS A ',name)

# class B:
#     def __init__(self,name):
#         print('CLASS B ',name)

# class C(A,B):
#     def __init__(self):
#         print('CLASS C')
#         super().__init__('Tanya')
#         B.__init__(self,'Akshit')

# obj=C()

# d={'a':300,'b':986}
# s=0
# for i in d.values():
#     s+=i
# print(s)

# s=7,8,9,8
# l=list(s)
# print(l)
# n=[str(i) for i in l]
# print(n)
# print(tuple(n))

# l='           ppanya gyftd'
# print(l.replace(' ',''))

# class B:
#     def __init__(self):
#         print('jhgf')
# class d(B):
#     def __init__(self):
#         print('hgh')
#         super().__init__()

# o=d()







# import matplotlib.pyplot as mat

# # line graph
# x=[12,23,11,16,32]
# x2=[10,20,25,30,29]
# y=[91,100,89,79,39]
# y2=[89,90,79,55,23]
# mat.plot(x,y,label='First',marker='D',markerfacecolor='r',color='k',ls='-.',lw=3)
# mat.plot(x2,y2,label='Second',marker='D',markerfacecolor='b',color='r',ls='-.',lw=3)

# mat.xlabel('Quanity')
# mat.ylabel('Cost')
# mat.title('Line Graph')
# mat.legend()
# mat.savefig('D:\python proj\line.pdf',format='pdf')
# mat.show()


# pie chart

# from tracemalloc import start
# import matplotlib.pyplot as mat

# x=[22,54,23,79,89]
# y=['A','B','C','D','E']
# color=['blue','r','g','cyan','grey']
# ex=[0,0.2,0,0,0.2]
# mat.pie(x,labels=y,colors=color,explode=ex,startangle=90,autopct='%1.1f%%',shadow=True)
# mat.title('Pie Chart')

# mat.show()




# mat.hist(x1,y,color='r',label='First')
# # mat.scatter(x2,y,color='k',label='Second')
# mat.xlabel('xyz')

# mat.ylabel('abc')
# mat.title('Histogram Graph')
# mat.show()

  
# # import matplotlib.pyplot as mat
# # import numpy as n# SCATTER GRAPH
# # from cProfile import label
# # from turtle import color
# import matplotlib.pyplot as mat
# x1=[10,21,22,15,23]
# # x2=[32,45,43,67,89]
# y=[10,20,30,40,50]p
# face=[1000,1500,1800,1900,2200,6754]
# you=[678,1777,3241,2434,1899,4967]
# sr=np.arange(len(face))
# mat.bar(sr,face,color='g',width=0.2)
# mat.bar(sr+0.2,you,color='r',width=0.2)
# mat.show()
  

# a=10
# b=15

# print(a&b)
# print(a|b)
# print(a^b)
# print(a>>3)
# print(a<<2)



# for i in range(5,0,-1):
#     print(i)

# # x=100
# class a:
#     x=12
#     def cal(self):
#         print(self.x)
# ab=a()
# print(ab.x)





# class cal:
#     def great(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!= None:
#             if a>b and a>c:
#                 print(a)
#             elif b>a and b>c:
#                 print(b)
#             else:
#                 print(c)
#         elif a!=None and b!=None:
#             if a>b:
#                 print(a)
#             else:
#                 print(b)
#         elif a!=None:
#             print(a)

# o=cal()
# o.great(1,22,32)

s='PYTHON'
# PRAM
# l=list(s)
# # l2=[]
# l.remove('O')
# l.remove('G')
# l.remove('R')
# print(l)
# print(''.join(l))

# s1='TH'
# s2=" "
# for i in s:
#     if i not in s1:
#         if i not in s2:
#             s2+=i
# print(s2)
# with open('neha.txt') as myfile:
#     print(myfile.write('o'))
# myfile.close()
# import random
# x=(random.randint(0,1))


# print(x)



