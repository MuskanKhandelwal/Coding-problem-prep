#####Printing patterns###########
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(1,end='')
#     print()

# k=5
# for i in range (0,6):
#     for j in range(0,k):
#         print(end=' ')
#     k=k-1
#     for j in range(0,i+1):
#         print("1",end='')
#     print()

########V Pattern ################
# spaces=8
# for i in range(1,6):
#     for j in range(1,i+1):
#             print(j,end='')
#     for k in range(1,spaces+1):
#         print(end=' ')
#     spaces=spaces-2
#     for j in range(i,0,-1):
#             print(j,end='')
#     print()

#####Perfect Number#########

# T=int(input())
# while(T>0):
#     sum=0
#     n=int(input())
#     for i in range(1,n):
#         if(n%i==0):
#             sum+=i
#     if (sum==n):
#         print("true")
#     else:
#         print("false")
#     T=T-1

#####bablu and Dablu####
# T=int(input())
# while(T>0):
#     N=int(input())
#     x=N%8
#     if(x==0):
#         print(N-1,"SL",sep='')
#     elif(x==1):
#         print(N+3,"LB",sep='')
#     elif(x==2):
#         print(N+3,"MB",sep='')
#     elif(x==3):
#         print(N+3,"UB",sep='')
#     elif(x==4):
#         print(N-3,"LB",sep='')
#     elif(x==5):
#         print(N-3,"MB",sep='')
#     elif(x==6):
#         print(N-3,"UB",sep='')
#     elif(x==7):
#         print(N+1,"SU",sep='')
#     T=T-1

####Ten from two#####
# T=int(input())
# while(T>0):
#     n=int(input())
#     if(n%10==0):
#         print(0)
#     elif(n%10==5):
#         n=n*2
#         if(n%10==0):
#             print(1)
#         else:
#             print(-1)
#     else:
#       print(-1)
#     T=T-1


#####Shopping Cost ########

# T=int(input())
# while(T>0):
#     q,p=input().split()
#     q=float(q)
#     p=float(p)
#     if (q>100):
#         cost=(q*p)-(0.2*q*p)
#     else:
#         cost=q*p
#     print(cost)


####Fit square#######
# T=int(input())
# block=0
# block2=0
# block1=0
# while (T>0):
#     m,n=input().split()
#     m=int(m)
#     n=int(n)
#     if((m%2==0)):
#         for i in range(0,m,2):
#             for j in range(0,n):
#                 block+=1
#         print(block)
#     elif((m%2!=0)and(n%2!=0)):
#         for i in range(0,m-1,2):
#             for j in range(0,n):
#                 block+=1
#         for k in range(0,n-1,2):
#             block2+=1
#         total=block+block2
#         print(total)
#     elif((m%2!=0)and(n%2==0)):
#         for i in range(0,m-1,2):
#             for j in range(0,n):
#                 block+=1
#         for k in range(0,n,2):
#             block2+=1
#         total=block+block2
#         print(total)
#     T=T-1
###Correct answer to fit square####
# T=int(input())
# while(T>0):
#     m,n=input().split()
#     m=int(m)
#     n=int(n)
#     area=m*n
#     block=int(area/2)
#     print(block)
#     T=T-1

####Fascinating Number####
# T=int(input())
# def isUnique(x):
#     r1=x%10
#     x=x//10
#     r2=x%10
#     x=x//10
#     r3=x%10
#     x=x//10
#     r4=x%10
#     if(r1==r2 or r1==r3 or r1==r4 or r2==r3 or r2==r4 or r3==r4):
#         return 0
#     else:
#         return 1
# while(T>0):
#     n=int(input())
#     for i in range(n+1,9999):
#         p=isUnique(i)
#         if(p==1):
#             break
#         elif(p==0):
#             continue
#     print(i)
#     T=T-1

######House Number############
# T=int(input())
# p=0
# def count(n):
#     i=1
#     while True:
#         n=n//10
#         if(n>0):
#             i=i+1
#             continue
#         else:
#             break
#     return i
# while(T>0):
#   n=int(input())
#   p=count(n)
#   k=p-1
#   nine=int("9"*k)
#   number=nine+(n-nine)*p
#   print(number)
#   T=T-1

# T=int(input())
# def findDigits(N):
#     if N == 1:
#         return 1
#     s = str(N)
#
#     return len(s) + findDigits(N - 1)
#
#
# # Driver Code
#
# # Given N
# while(T>0):
#     N = int(input())
#     print(findDigits(N))
#     T=T-1

###2nd method####
# T=int(input())
# def totalDigits(n):
#     number_of_digits = 0
#
#     for i in range(1, n, 10):
#         number_of_digits = (number_of_digits +
#                             (n - i + 1))
#
#     return number_of_digits
#
#
# while(T>0):
#     n=int(input())
#     s=totalDigits(n) + 1
#     print(s)
#     T=T-1

# T=int(input())
# p=0
# def count(n):
#     i=1
#     while True:
#         n=n//10
#         if(n>0):
#             i=i+1
#             continue
#         else:
#             break
#     return i
# while(T>0):
#   n=int(input())
#   p=count(n)
#   if(p==1):
#       print(n)
#   elif(p==2):
#       print(9+(n-9)*2)
#   elif(p==3):
#       print(9+90*2+(n-99)*3)
#   elif(p==4):
#       print(9+90*2+900*3+(n-999)*4)
#   elif(p==5):
#       print(9+90*2+900*3+9000*4+(n-9999)*5)
#   elif(p==6):
#       print(9+90*2+900*3+9000*4+90000*5+(n-99999)*6)
#   elif(p==7):
#       print(9+90*2+900*3+9000*4+90000*5+900000*6+(n-999999)*7)
#   elif(p==8):
#       print(9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7+(n-9999999)*8)
#   elif(p==9):
#       print(9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7+90000000*8+(n-99999999)*9)
#   elif(p==10):
#       print(9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7+90000000*8+900000000*9+(n-999999999)*10)
#   T=T-1


#####Good Number#####
# T=int(input())
#
# while(T>0):
#   n=int(input())
#   s=0
#   i=0
#   while(s<=n):
#     s=s+(3**i)
#     #print(s)
#     i=i+1
#   while(s>=n):
#       s=s-3**i
#
#   T=T-1

T=int(input())

while(T>0):
  n=int(input())
  x=1
  sum=0
  while(sum<n):
    sum+=x
    x=int(x*3)
  while(x>0):
     if(sum-x>=n and x>0):
         sum-=x
         x=x/3
         x=int(x)
     elif x>0 :
         x=x/3
         x=int(x)
  print(int(sum))
  T=T-1