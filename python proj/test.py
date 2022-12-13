# t=[i**2 for i in range(0,31)]
# print(t[5: :])
# n=int(input())
# l1=[input() for i in range(0,n)]
# n1=int(input())
# l2=[input() for i in range(0,n1)]
# r=l1.extend(l2)
# x=sorted(r)
# print(x)00

# import math
# l=[round(math.sqrt(i),2) for i in range(1,52) if i%5==0]
# print(l)

# l=[1,2,3,4,5,6]
# l1=[]
# if len(l)>=5:
#     for i in l:
#         if i%2==0:
#             l1.append(i+2)
#         else:
#             l1.append(i)

# print(l1)
a=[]
for i in range(1,6):
    l=[]
    for j in range(5):
        l.append((i*5)+j)
    a.append(l)
print(a)