#### 1 st method #####
# arr=[]
# for ele in input().split():
#     arr.append(int(ele))
# for i in range(len(arr)):
#     print(arr[i],end=' ')
# print(type(arr))

#### 2nd Method, using map and list function ###
# arr1=list(map(int,input().split()))
# for i in range(len(arr1)):
#     print(arr1[i],end=" ")
#
# print(type(arr1))


###Min max problem ####
# T=int(input())
# while(T>0):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     min=10000001
#     max=-1
#     for i in range(n):
#         if arr[i]<min:
#             min=arr[i]
#         if arr[i]>max:
#             max=arr[i]
#     print(min,max) #printf("%d %d"%(min,max)
#     T=T-1
#
# s="a@b@c@d"
# a=list(s.partition("@"))
# print(a)
# b=list(s.split("@",3))
# print(b)

###Find even out ####
# n = int(input())
# arr = list(map(int, input().split()))
# even = []
# odd = []
# for i in range(n):
#     k = arr[i]
#     if k % 2 == 0:
#         even.append(int(k))
#     else:
#         odd.append(int(k))
# for i in range(len(even)):
#     print(even[i], end=' ')
# print()
# for j in range(len(odd)):
#     print(odd[j], end=' ')


##Min house number####
# T=int(input())
# while(T>0):
#   n=int(input())
#   rent=list(map(int,input().split()))
#   min=1000
#   for i in range(n):
#     if rent[i]<min:
#       min=rent[i]
#       k=i
#   print(k)
#   T=T-1

####Last one####
# T=int(input())
# while(T>0):
#   n=int(input())
#   val=list(map(int,input().split()))
#   count=0
#   for i in range(n):
#     if val[i]==1:
#       k=i
#       count+=1
#   if(count==0):
#     print(-1)
#   else:
#     print(k)
#   T=T-1

####Greater than neighbour####
# T=int(input())
# while(T>0):
#   n=int(input())
#   rent=list(map(int,input().split()))
#   neigh=[]
#   count=0
#   for i in range(0,n):
#     if(i==0 and rent[1]<rent[0]):
#       neigh.append(0)
#       count+=1
#     elif(i==n-1 and rent[n-1]>rent[n-2]):
#       l=n-1
#       neigh.append(l)
#       count+=1
#     elif(i!=0 and i!=n-1 and (rent[i]>rent[i+1]) and (rent[i]>rent[i-1] ) ):
#       z=i
#       #print(rent[i])
#       neigh.append(z)
#       count+=1
#   if(count==0):
#     print(-1)
#   else:
#     for ele in range(len(neigh)):
#       print(neigh[ele],end=' ')
#   T=T-1


####Find the missing#####
#Method1 but time limit exceeded
# T=int(input())
# while(T>0):
#   n=int(input())
#   arr=list(map(int,input().split()))
#   s=[]
#   for i in range(1,n+1):
#       s.append(i)
#
#   if(n==2 and (arr[0]!=1)):
#       k=1
#   elif(n==2 and (arr[0]==1)):
#       k=2
#   else:
#      for i in range(0,n):
#         if(s[i] in arr):
#           pass
#         else:
#           k=s[i]
#   print(k)
#
#   T=T-1
#Method 2##
# T=int(input())
# while(T>0):
#   n=int(input())
#   arr=list(map(int,input().split()))
#   s=0
#   c=0
#   for i in range(0,n-1):
#     s+=arr[i]
#     c=c+i+1
#   c+=n
#   print(c-s)
#
#   T=T-1

###Find the leader#####
# T=int(input())
# while(T>0):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     m=0
#     if(n==1):
#         print(arr[0])
#     else:
#         for i in range(n-1,-1,-1):
#             if(arr[i]>=m):
#                 print(arr[i],end=' ')
#                 m=arr[i]
#     print()
#     T=T-1

##Rearange the array##
# T=int(input())
# while (T>0):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     res=[]
#     for i in range(0,n):
#         res.append(arr[n-1-i])
#         res.append(arr[i])
#     for i in range(0,n):
#         print(res[i],end=' ')
#     T=T-1

###Rainbow array####
# T=int(input())
# while(T!=0):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     k=0
#     def check(arr):
#         curr=1
#         printer=1
#         for i in range(n):
#             if(arr[i]==curr):
#                 arr[i]=arr[i]+printer
#                 k=1
#             if(curr==7):
#                 printer=-1
#                 k=-1
#         return k
#     left=0
#     right=n-1
#     curr1=1
#     count=0
#     call=check(arr)
#     while(left<right):
#         if(arr[left]==arr[right]):
#             if(arr[left]==curr1):
#                 count=count+2
#             else:
#                 if curr1!=7:
#                     if count==2*arr[curr1]:
#                         print("Not possible")
#                     else:
#                         curr1+=1
#                         count=2
#                 else:
#                     print("Not possible")
