#####Linear search#####
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         t=int(input())
#         flag=0
#         for i in range(n):
#             if(arr[i]==t):
#                 print("Target value is present at index", i)
#                 flag=1
#                 break
#         if(flag==0):
#             print("target value is not present")
#
#     T=T-1
#
# if __name__ == '__main__':
#     main()


#####Number of occurences###
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         str1=input()
#         t='x'
#         count=0
#         for i in range(len(str1)):
#             if(str1[i]==t):
#                 count+=1
#
#         print(count)
#         T=T-1
#
# if __name__ == '__main__':
#     main()

####Floor of a number####
# def main():
#     T=int(input())
#     while(T>0):
#         n,x=map(int,input().split())
#         arr=list(map(int,input().split()))
#         f=0
#         k=-1
#         diff=9999999
#         for i in range(n):
#             if(arr[i]<=x):
#                 diff=min(diff,x-arr[i])
#                 k+=1
#         if(k==-1):
#             print(-1)
#         else:
#             print(k)
#             # f=x%arr[k]
#             # print(f)
#
#         T=T-1
#
# if __name__ == '__main__':
#     main()

#####Binary search#########
# def BinarySearch(arr,n,target):
#     low=0
#     high=n-1
#     while(low<=high):
#         mid=low+(high-low)//2
#         if(arr[mid]==target):
#             return mid
#         if(target>arr[mid]):
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         target=int(input())
#         res=BinarySearch(arr,n,target)
#         if(res==-1):
#             print("target value not present")
#         else:
#             print("target value present at index",res)
#
#         T=T-1
#
#
# if __name__ == '__main__':
#     main()


#####Transition point######
# def transitionsearch(arr,low,high,target,n):
#     if(high>=low):
#         mid = low +(high - low) // 2
#         if (target==arr[mid] and target>arr[mid-1]):
#             return mid
#         elif(target>arr[mid]):
#             return transitionsearch(arr,mid+1,high,target,n)
#         else:
#             return transitionsearch(arr,low,mid-1,target,n)
#     return -1
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         target=1
#         if(arr[0]==1):
#             print(0)
#         else:
#             ans=transitionsearch(arr,0,n-1,target,n)
#             print(ans)
#         # if ans:
#         #     print(ans)
#         # else:
#         #     print(-1)
#         T=T-1
#
# if __name__ == '__main__':
#     main()

####Recursive Binary Search####
# def RecBinarySearch(arr,low,high,target):
#     if(low>high):
#         return
#     mid=low+(high-low)//2
#     if(arr[mid]==target):
#         return mid
#     elif(arr[mid]<target):
#         return RecBinarySearch(arr,mid+1,high,target)
#     else:
#         return RecBinarySearch(arr,low,mid-1,target)
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         target=int(input())
#         res=RecBinarySearch(arr,0,n-1,target)
#         if(res==-1):
#             print("target value not present")
#         else:
#             print("target value present at index",res)
#
#         T=T-1
#
#
# if __name__ == '__main__':
#     main()

#####Lower Bound####
# def lowerbound(arr,n,ele):
#     low=0
#     high=n
#     while(low<high):
#         mid=(low+high)//2
#         if(ele<=arr[mid]):
#             high=mid
#         else:
#             low=mid+1
#     return low
#
# from sys import setrecursionlimit
# setrecursionlimit(100000000)
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         q=int(input())
#         while(q>0):
#             ele=int(input())
#             print(lowerbound(arr,n,ele))
#             q=q-1
#         T=T-1
#
# if __name__ == '__main__':
#     main()


####Upper Bound#####
# def upperbound(arr,n,ele):
#     low=0
#     high=n
#     while(low<high):
#         mid=(low+high)//2
#         if(ele>=arr[mid]):
#             low=mid+1
#         else:
#             high=mid
#     return low
#
# from sys import setrecursionlimit
# setrecursionlimit(100000000)
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         q=int(input())
#         while(q>0):
#             ele=int(input())
#             print(upperbound(arr,n,ele))
#             q=q-1
#         T=T-1
#
# if __name__ == '__main__':
#     main()


####Get the sunlight#######
# def findlight(arr,n,t,count):
#     for i in range(n):
#         if arr[i]>t:
#             t=arr[i]
#             count+=1
#             #print(count,t)
#             #return findlight(arr,n,target,i+1,count)
#     return count
#
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         t=-1
#         count=0
#         k=findlight(arr,n,t,count)
#         print(k)
#         T=T-1
#
# if __name__ == '__main__':
#     main()

####Smallest number####
# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     k=int(input())
#     b = [0]*pow(10,6)
#     for i in range(n):
#         b[arr[i]] += 1
#     for i in range(n):
#         if (b[i]==k):
#             print(i)
#             break
# if __name__ == '__main__':
#     main()


####Number of chocolates (using upper bound)###
#Follow upper bound
#Since here we need the index greater than the price.
# def chocolates(arr,n,x):
#     low=0
#     high=n
#     while(low<high):
#         mid=(low+high)//2
#         if(x>=arr[mid]):
#             low=mid+1
#         else:
#             high=mid
#     return low
#
# def main():
#     n=int(input())
#     arr=list(map(int,input().split()))
#     q=int(input())
#     arr.sort()
#     while(q>0):
#         x=int(input())
#         res=chocolates(arr,n,x)
#         print(res)
#         q=q-1
#
# if __name__ == '__main__':
#     main()

#####No of chocolates (not sorted),iterative######
# def main():
#     n=int(input())
#     arr=list(map(int,input().split()))
#     q=int(input())
#     while(q>0):
#         x=int(input())
#         count=0
#         for i in range(n):
#             if(arr[i]<=x):
#                 count+=1
#         print(count)
#         q=q-1
#
# if __name__ == '__main__':
#     main()


###Maximize the problems######
# def maxprb(time,n):
#     for i in range(1,n+1):
#         time = time-(5*(i))
#         #print(time)
#         if (time == 0):
#             return i
#             break
#         elif (time< 0):
#             return i-1
#             break
#         else:
#             continue
#
# def main():
#     n,k=map(int,input().split())
#     time=240-k
#     if(k==240):
#         print(0)
#     else:
#         ans=maxprb(time,n)
#         if ans:
#             print(ans)
#         else:
#             print(n)
# if __name__ == '__main__':
#     main()

#####Peak house###
# T=int(input())
# while(T>0):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     z=max(arr)
#     max_index=arr.index(z)
#     print(max_index)
#     T=T-1

####Majority votes####
# T=int(input())
# while(T>0):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     frq=[0]*9999999
#     s=-1
#     for i in range(n):
#         frq[arr[i]]+=1
#     win=n//2
#     for i in range(len(frq)):
#         if (frq[i]>win):
#             s=i
#             break
#     if(s==-1):
#         print(-1)
#     else:
#         print(s)
#     T=T-1

###Rotate and find#####
# def findpivot(arr,n,k):
#     low=0
#     high=n
#     while(low<high):
#         mid=low+(high-low)//2
#         if(arr[mid]>arr[high]):
#             low=mid+1
#         else:
#             high=mid
#
#
#
# def findr(arr,n,x,k):
#     for i in range(n):
#         if (arr[i] == x):
#             k=i
#             break
#         else:
#             k=-1
#     return k
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         x=int(input())
#         k=-1
#         ans=findr(arr,n,x,k)
#         print(ans)
#         T=T-1
# if __name__ == '__main__':
#     main()


#####Find mountain top######3
# from sys import setrecursionlimit
# setrecursionlimit(100000000)


######Missing in AP####
# def findmis(arr,low,high,k):
#     if(high<low):
#         return
#     mid=low+(high-low)//2
#     if(arr[mid+1]-arr[mid]!=k):
#         return (arr[mid]+k)
#     if(mid>0 and arr[mid]-arr[mid-1]!=k):
#         return (arr[mid-1]+k)
#     if(arr[mid]==arr[0]+mid*k):
#         return findmis(arr,mid+1,high,k)
#     else:
#         return findmis(arr,low,mid-1,k)
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         k=int((arr[n-1]-arr[0])/n)
#         ans=findmis(arr,0,n-1,k)
#         print(ans)
#
#
#         T=T-1
# if __name__ == '__main__':
#     main()

###Books left###
# def countleft(arr,n,k):
#     count=0
#     for i in range (n):
#         if(arr[i]<=k):
#             count+=1
#         else:
#             break
#     return (n-count)
# def countright(arr,n,k):
#     count=0
#     for i in range (n-1,-1,-1):
#         #print(arr[i])
#         if(arr[i]<=k):
#             count+=1
#         else:
#             break
#     return (n-count)
# def main():
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     ans=0
#     if(arr[0]>k or arr[n-1]==k):
#         ans=countright(arr,n,k)
#         print(ans)
#     elif(arr[n-1]>k or arr[0]==k):
#         ans=countleft(arr,n,k)
#         print(ans)
#     elif(arr[0]==k):
#         ans=countleft(arr,n,k)
#         print(ans)
# if __name__ == '__main__':
#     main()
# n,k=map(int,input().split())
# a=list(map(int,input().split()))
# start=0
# c=0
# end=n-1
# while(start<=end and (a[start]<=k or a[end]<=k)):
#     if start == end:
#       c += 1
#       start +=1
#       end -=1
#       continue
#     if(a[start]<=k):
#       c+=1
#       start+=1
#     if(a[end]<=k):
#       c+=1
#       end-=1
# print(n-c)

###Divisor closest to K(Brute force)#######
# import sys
# import math
# def main():
#     n=int(input())
#     q=int(input())
#     while(q!=0):
#         k=int(input())
#         temp=0
#         mindiff=sys.maxsize
#         ans=0
#         for i in range(1,int(math.sqrt(n)+1)):
#             if(n%i==0):
#                 temp=abs(k-i)
#                 if(mindiff>temp):
#                     mindiff=temp
#                     ans=i
#                 #For second divisor
#                 if(n//i!=i):
#                     temp=abs(k-n//i)
#                     if(mindiff>=temp):
#                         mindiff=temp
#                         ans=n//i
#         print(ans)
#         q=q-1
#
# if __name__ == '__main__':
#     main()

#####Divisor closest to K(optimized approach)####
# import math
# import sys
# def main():
#     n=int(input())
#     q=int(input())
#     div=[]
#     size=int(math.sqrt(n))+1
#     for i in range(1,n):
#         if(n%i==0):
#             div.append(i)
#             if(i!=n//i):
#                 div.append(n//i)
#     div.sort()
#     while(q!=0):
#         k=int(input())
#         if(k<=div[0]):
#             print(div[0])
#         elif(k>=div[len(div)-1]):
#             print(div[len(div)-1])
#         else:
#             low=0
#             high=len(div)-1
#             flag=0
#             mid=0
#             while(low<high and flag==0):
#                 mid=(low+high)//2
#                 if(div[mid]==k):
#                     flag=1
#                     print(div[mid])
#                 else:
#                     if(k<div[mid]):
#                         if(mid>0 and k>div[mid-1]):
#                             if(abs(k-div[mid])>=abs(k-div[mid-1])):
#                                 flag=1
#                                 print(div[mid-1])
#                             else:
#                                 flag=1
#                                 print(mid)
#                         else:
#                             high=mid
#                     else:
#                         if(mid<n-1 and k<div[mid+1]):
#                             if(abs(k-div[mid])>abs(k-div[mid+1])):
#                                 flag=1
#                                 print(div[mid+1])
#                             else:
#                                 flag=1
#                                 print(div[mid])
#                         else:
#                             low=mid+1
#             if(flag==0):
#                 print(div[mid])
#
#
#         q=q-1
# if __name__ == '__main__':
#     main()
#####Interesting array 2#######
# def main():
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     arr.sort()
#
# if __name__ == '__main__':
#     main()

# from collections import defaultdict
# dic=defaultdict(lambda :0)
# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
# for i in range(n):
#     dic[arr[i]-k]+=1
# ans=0
# for i in range(n):
#     ans+=dic[arr[i]]
# print(ans)

###Median Again####
# def main():
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     mid=n//2
#     #print(mid)
#     arr.sort()
#     cnt=1
#     move=0
#     while(move<=k and mid<n-1):
#         diff=arr[mid+1]-arr[mid]
#         if(move+diff*cnt<=k):
#             move+=diff*cnt
#             cnt+=1
#             arr[mid]=arr[mid+1]
#             print(arr)
#             mid+=1
#         else:
#             break
#     if(move<=k):
#         left=k-move
#         print(mid)
#         arr[mid]+=int(left/cnt)
#
#     print(arr[mid])
#
# if __name__ == '__main__':
#     main()

####Stock market######
# def maxprofit(arr,n):
#     profit=0
#     if(n==1):
#         return
#     i=0
#     while(i<(n-1)):
#         while((i<n-1)and(arr[i+1]<=arr[i])):
#             i+=1
#         if(i==n-1):
#             break
#         buy=i
#
#         i+=1
#         while ((i < n) and (arr[i] >= arr[i - 1])):
#             i += 1
#         sell = i - 1
#         profit=profit+abs((arr[buy]-arr[sell]))
#
#     return profit
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         print(maxprofit(arr,n))
#         T=T-1
#
# if __name__ == '__main__':
#     main()

#####Maximum divisors in a range####
# import math
# def main():
#     a,b=map(int,input().split())
#     q=int(input())
#     while(q>0):
#         low,high=map(int,input().split())
#         diva=[]
#         divb=[]
#         sizea=int(math.sqrt(a))+1
#         sizeb=int(math.sqrt(b))+1
#         for i in range(1,sizea):
#             if(a%i==0):
#                 diva.append(i)
#                 if(i!=a//i):
#                     diva.append(a//i)
#         diva.sort()
#         for i in range(1,sizeb):
#             if(b%i==0):
#                 divb.append(i)
#                 if(i!=b//i):
#                     divb.append(b//i)
#         divb.sort()
#         divsa=set(diva)
#         divsb=set(divb)
#         divcommon=divsa & divsb
#         divlist=list(divcommon)
#         # print(diva)
#         # print(divb)
#         #print(divlist)
#         div=[]
#         flag=0
#         for i in range(len(divlist)):
#             if(low<=divlist[i]<=high+1):
#                 div.append(divlist[i])
#         if div:
#             print(max(div))
#         else:
#             print(-1)
#
#         q=q-1
# if __name__ == '__main__':
#     main()

###Optimized approach for max div in range###
# import math
# global gcd_a_b
# gcd_a_b=0
# global divab
# divab=[]
# def GCD(a,b):
#     if(b==0):
#         return a
#     return GCD(b,a%b)
# def binary(low,high,l,h):
#     flag=0
#     while (l < h):
#         mid = (l + h) // 2
#         if(low==high and high<=divab[len(divab)-1] and low>=divab[0]):
#             flag=1
#             return low
#         if (divab[mid] < high):
#             l = mid + 1
#         if (divab[mid] > high):
#             h = mid - 1
#         if (divab[mid] == high):
#             flag=1
#             return (divab[mid])
#         if ((divab[len(divab) - 1] < low) or (divab[0] > high) ):
#             flag=1
#             return -1
#     if(flag==0):
#         return (divab[mid])
#
# def main():
#     a,b=map(int,input().split())
#     q=int(input())
#     global gcd_a_b
#     global divab
#     gcd_a_b = GCD(a, b)
#     size = int(math.sqrt(gcd_a_b)) + 1
#     for i in range(1, size):
#         if (gcd_a_b % i == 0):
#             divab.append(i)
#             if (i != gcd_a_b // i):
#                 divab.append(gcd_a_b // i)
#     divab.sort()
#     #print(divab)
#     while(q>0):
#         low,high=map(int,input().split())
#         l=0
#         h=len(divab)
#         k=binary(low,high,l,h)
#         print(k)
#         q=q-1
#
# if __name__ == '__main__':
#     main()
#

