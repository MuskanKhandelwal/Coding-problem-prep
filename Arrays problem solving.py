# ####Array rotation(Basic approach)####
# # def rightRotate(arr,n):
# #     tmp=arr[n-1]
# #     for i in range(n-1,0,-1):
# #         arr[i]=arr[i-1]
# #     arr[0]=tmp
# # def printArr(arr,n):
# #     for i in range(n):
# #         print(arr[i],end=' ')
# #     print()
# # def main():
# #     T=int(input())
# #     while(T>0):
# #         n,k=(map(int,input().split()))
# #         arr=list(map(int,input().split()))
# #         for i in range(k):
# #             rightRotate(arr,n)
# #         printArr(arr,n)
# #
# #         T=T-1
# #
# # if __name__ == '__main__':
# #     main()
#
# ####Array rotation using Reversal algorithm(Method 2) #####
# # def printArr(arr,n):
# #     for i in range(n):
# #         print(arr[i],end=' ')
# #     print()
# #
# # def reverseRightAlgo(arr,i,j):
# #     while(i<j):
# #         temp = arr[i]
# #         arr[i] = arr[j]
# #         arr[j] = temp
# #         i+=1
# #         j-=1
# # def main():
# #     T=int(input())
# #     while(T>0):
# #         n,k=map(int,input().split())
# #         arr=list(map(int,input().split()))
# #         if(k>n):
# #             k=k%n
# #         reverseRightAlgo(arr,n-k,n-1)
# #         reverseRightAlgo(arr,0,n-k-1)
# #         reverseRightAlgo(arr,0,n-1)
# #         printArr(arr,n)
# #         T=T-1
# #
# # if __name__ == '__main__':
# #     main()
#
#
# ###Multiplication of matirx####
# n,m=map(int,input().split())
# mat1=[]
# for i in range(n):
#     mat1.append(list(map(int,input().split())))
#
# mat2=[]
# for i in range(n):
#     mat2.append(list(map(int,input().split())))
# mat3=[]
# for i in range(n):
#     mat3.append([0]*m)
# #Addition
# for i in range(n):
#     for j in range(m):
#         mat3[i][j]=mat1[i][j]+mat2[i][j]
#
# for i in range(n):
#     for j in range(m):
#         print(mat3[i][j],end=' ')
#     print()
#
# #Multiplication
# mat4=[]
# for i in range(n):
#     mat4.append([0]*m)
# for i in range(n):
#     for j in range(m):
#         for k in range(m):
#             mat4[i][j]=mat4[i][j]+(mat1[i][k]*mat2[k][j])
#
#
# for i in range(n):
#     for j in range(m):
#         print(mat4[i][j],end=' ')
#     print()
#
#### Scalar multiplication####
# m, n, k = map(int, input().split())
# mat1 = []
# for i in range(n):
#     mat1.append(list(map(int, input().split())))
# mat3 = []
# for i in range(n):
#     mat3.append([0] * m)
#
# for i in range(n):
#     for j in range(m):
#         mat3[i][j] = k * mat1[i][j]
#
# for i in range(n):
#     for j in range(m):
#         print(mat3[i][j], end=' ')
#     print()


#Lower and upper triangular matrices###
# def printmat(mat,i,j):
#     for i in range(m):
#         for j in range(n):
#             print(mat[i][j], end=' ')
#         print()
#
#
# m,n=map(int,input().split())
# mat1=[]
# mat2=[]
# for i in range(m):
#     mat2.append([0] * n)
#
# for i in range(m):
#     mat1.append(list(map(int,input().split())))
# for i in range(m):
#     for j in range(n):
#         mat2[i][j]=mat1[i][j]
# #Upper triangle
# for i in range(m):
#     for j in range(i+1,n):
#         mat1[i][j]=0
# printmat(mat1,m,n)
#
# #Lower triangle
# for i in range(m):
#     for j in range(n):
#         if(i>j):
#             mat2[i][j]=0
# printmat(mat2,m,n)


###Frequency array#####
# T=int(input())
# while(T>0):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     freq=[0]*40
#     for i in range(n):
#         freq[arr[i]]+=1
#     # for i in range(40):
#     #     if(freq[i]>0):
#     #         print(i,freq[i])
#     flag=0
#     for i in range(40):
#         if(freq[i]>1):
#             flag=1
#             break
#     if(flag==1):
#         print("Not unique")
#     else:
#         print("Unique")
#
#     T=T-1

##Friends age###
# n=int(input())
# arr=list(map(int,input().split()))
# count=0
# for i in range(n):
#     for j in range(n):
#         if(i!=j):
#             if((arr[j]<=0.5*arr[i]+7)or(arr[j]>100 and arr[i]<100)or (arr[j]>arr[i])):
#                 continue
#             else:
#                 count+=1
# print(count)

###Optimized approach for friends age#####
# n=int(input())
# arr=list(map(int,input().split()))
# freq=[0]*121
# for i in range(n):
#     freq[arr[i]]+=1
# ans=0
# for i in range(1,121):
#     for j in range(1,121):
#         if(i<=j*0.5+7):
#             continue
#         if(i>100 and j<100):
#             continue
#         if(i>j):
#             continue
#         ans+=freq[i]*freq[j]
#         if(i==j):
#             ans-=freq[i]
# print(ans)


##Array zigzag###
# n=int(input())
# arr=list(map(int,input().split()))
# def zigzag(arr,n,start):
#     res=0
#     for i in range(start,n,2):
#         x=arr[i]
#         if(i):
#             x=min(x,arr[i-1]-1)
#         if(i+1!=n):
#             x=min(x,arr[i+1]-1)
#         res+=arr[i]-x
#     return res
#
# z=min(zigzag(arr,n,0),zigzag(arr,n,1))
# print(z)

####Quality Factor####
# n = int(input())
# arr = list(map(int, input().split()))
# quality=0
# curr=0
# steps=0
# for i in range(n):
#     # if(arr[i]>quality):
#     #     steps+=abs(arr[i]-quality)
#     #     quality=arr[i]
#     # elif(arr[i]<quality):
#     #     steps+=abs(quality-arr[i])
#     curr=arr[i-1]
#     steps+=abs(arr[i]-curr)
# print(steps)


####Sliding window(Brute Force)#####
# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
# sum=0
# max=-1
# for i in range(0,n-k+1):
#     sum=0
#     for j in range(i,i+k):
#         sum+=arr[j]
#     if(sum>max):
#         max=sum
# print(max)


###Optimized approach####
# def main():
#     T=int(input())
#     while(T!=0):
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         sum=0
#         for i in range(0,k):
#             sum+=arr[i]
#         max=sum
#         for i in range(k,n):
#             sum=sum - arr[i-k]+arr[i]
#             if(sum>max):
#                 max=sum
#         print(max)
#         T=T-1
# if __name__=='__main__':
#     main()


####Interesting array(Brute Force)####
# def main():
#     T=int(input())
#     while(T!=0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         k=int(input())
#         mini=-1
#         maxj=-1
#         flag=0
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if(arr[i]+arr[j]==k):
#                     flag=1
#                     if(j>maxj):
#                         mini=i
#                         maxj=j
#                     elif(maxj==j and mini>i):
#                         mini=i
#                         maxj=j
#         if(flag==0):
#             print("No answer")
#         else:
#             print(mini,maxj)
#         T=T-1
#
#
#
# if __name__=='__main__':
#     main()

####Interesting array(optimized approach)2 pointers technique####
# def main():
#     T=int(input())
#     while(T!=0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         k=int(input())
#         i=0
#         j=n-1
#         flag=0
#         while(i<j):
#             sum=arr[i]+arr[j]
#             if(sum==k):
#                 flag=1
#                 print(i,j)
#                 break
#             elif(sum>k):
#                 j=j-1
#             elif(sum<k):
#                 i=i+1
#         if(flag==0):
#             print("No answer")
#
#         T=T-1
# if __name__=='__main__':
#     main()

####Maximum difference###
# def main():
#     T=int(input())
#     while(T!=0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         max1=0
#         max2=0
#         min1=100000
#         min2 = 100000
#         maxi=0
#         for i in range(n):
#             max1=max(max1,arr[i]+i)
#             min1=min(min1,arr[i]+i)
#             max2=max(max2,arr[i]-i)
#             min2=min(min2,arr[i]-i)
#
#             maxi=max(maxi,max(max1-min1,max2-min2))
#
#
#         print(maxi)
#
#         T=T-1
# if __name__=='__main__':
#     main()


###Pairs###
# n,m=map(int,input().split())
# a=[]
# for i in range(m):
#   l=list(map(int,input().split()))
#   a.append(l)
# freq=[0]*(n+1)
# count=0
# y=0
# k=[0]*n
# for i in range(m):
#     if(a[i][0]==a[0][0] or a[i][1]==a[0][0]):
#         count+=1
#     else:
#         freq[a[i][0]]+=1
#         freq[a[i][1]]+=1
# for i in range(n):
#     if(freq[i]==m-count):
#         k.append("yes")
#
# count1 = 0
# freq1 = [0] * (n + 1)
# y2=0
# j=[0]*n
# for i in range(m):
#     if (a[i][0] == a[0][1] or a[i][1] == a[0][1]):
#         count1 += 1
#     else:
#         freq1[a[i][0]] += 1
#         freq1[a[i][1]] += 1
# for i in range(n):
#     if (freq1[i]==m-count1):
#         j.append("yes")
#
# if(("yes" in j)or("yes" in k)):
#     print("YES")
# else:
#     print("NO")

#####Arithmetic Progression#####
# n=int(input())
# arr=list(map(int,input().split()))
# f1diff=[0]*100001
# f3=[0]*100001
# count=[0]*100001
# for i in range(n):
#     if(count[arr[i]]==-2):
#         continue
#     count[arr[i]]+=1
#     if(count[arr[i]]==2):
#         f1diff[arr[i]]=i-f3[arr[i]]
#     elif(count[arr[i]]>2):
#         if(i-f3[arr[i]]!=f1diff[arr[i]]):
#             count[arr[i]]=-2
#             continue
#     f3[arr[i]]=i
# count2=0
# for i in range(len(count)):
#     if(count[i]>0):
#         count2+=1
# print(count2)
#
# for i in range(len(count)):
#     if (count[i]>0):
#         print(i, f1diff[i])

########Saitama's Punch########
# T=int(input())
# while(T>0):
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     z=0
#     time=0
#     for i in range(1,n):
#         z = arr[i] - arr[i - 1]
#         if z < k:
#             time = time + z
#         else:
#             time = time + k
#
#     print(time+k)
#     T=T-1
#

####Array max###########
# T = int(input())
# while (T > 0):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     max_val=0
#     sum = 0
#     for i in range(0, n):
#         sum=0
#         j=i
#         while(j<n):
#             if(sum+arr[j]<0):
#                 sum=0
#             else:
#                 sum+=arr[j]
#                 max_val=max(sum,max_val)
#             j+=k
#
#     print(max_val)
#     T = T - 1


###Mangda and silly pairs#####
# import math
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
# aeven=[]
# aodd=[]
# beven=[]
# bodd=[]
# sum=0
# sum1=0
# sum2=0
# for i in range(len(A)):
#     if(A[i]%2==0):
#         aeven.append(A[i])
#     else:
#         aodd.append(A[i])
#     if (B[i]%2== 0):
#         beven.append(B[i])
#     else:
#         bodd.append(B[i])
# for i in range(min(len(aodd),len(bodd))):
#     sum1=sum1+math.floor((aodd[i]+bodd[i])/2)
#
# for i in range(min(len(beven),len(aeven))):
#     sum2=sum2+math.floor((beven[i]+aeven[i])/2)
#
#
# sum=sum1+sum2
# print(sum)
