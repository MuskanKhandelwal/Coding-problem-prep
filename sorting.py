#####Bubblesort######
# def bubblesort(arr,n):
#     for i in range(n):
#         swapped=0
#         for j in range(n-i-1):
#             if(arr[j]>arr[j+1]):
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 swapped+=1
#         if(swapped==0):
#             break
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         bubblesort(arr,n)
#         for i in range(n):
#             print(arr[i],end=' ')
#         t=t-1
# if __name__ == '__main__':
#     main()

####Selection sort#####
# def selectionsort(arr,n):
#     for i in range(n):
#         min_ind=i
#         for j in range(i+1,n):
#             if(arr[j]<arr[min_ind]):
#                 min_ind=j
#             arr[i],arr[min_ind]=arr[min_ind],arr[i]
#
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         selectionsort(arr,n)
#         for i in range(n):
#             print(arr[i],end=' ')
#         t=t-1
# if __name__ == '__main__':
#     main()

####Insertiorn sort#######
# def insertionsort(arr,n):
#     for i in range(1,n):
#         temp=arr[i]
#         j=i-1
#         while(j>-1 and arr[j]>temp):
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=temp
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         insertionsort(arr,n)
#         for i in range(n):
#             print(arr[i],end=' ')
#         t=t-1
# if __name__ == '__main__':
#     main()

#####Merge two sorted arrays#######
# def mergesortedarray(arr1,arr2,n,m):
#     arr3=[None]*(n+m)
#     i=0
#     j=0
#     k=0
#     while(i<n and j<m):
#         if(arr1[i]<arr2[j]):
#             arr3[k]=arr1[i]
#             k=k+1
#             i=i+1
#         else:
#             arr3[k]=arr2[j]
#             k=k+1
#             j=j+1
#     while(i<n):
#         arr3[k]=arr1[i]
#         k=k+1
#         i=i+1
#     while(j<m):
#         arr3[k]=arr2[j]
#         k=k+1
#         j=j+1
#     return arr3
# def main():
#     t=int(input())
#     while(t>0):
#         n,m=map(int,input().split())
#         arr1=list(map(int,input().split()))
#         arr2=list(map(int,input().split()))
#         fin=mergesortedarray(arr1,arr2,n,m)
#         for i in range(n+m):
#             print(fin[i],end=' ')
#         print()
#         t=t-1
# if __name__ == '__main__':
#     main()
#
#####Merge sort########
# def merge(arr,l,mid,r):
#     n=mid-l+1
#     m=r-mid
#     arr1=[0]*n
#     arr2=[0]*m
#     for i in range(n):
#         arr1[i]=arr[l+i]
#     for i in range(m):
#         arr2[i]=arr[mid+1+i]
#     i=0
#     j=0
#     k=l
#     while(i<n and j<m):
#         if(arr1[i]<arr2[j]):
#             arr[k]=arr1[i]
#             k=k+1
#             i=i+1
#         else:
#             arr[k]=arr2[j]
#             k=k+1
#             j=j+1
#     while(i<n):
#         arr[k]=arr1[i]
#         k=k+1
#         i=i+1
#     while(j<m):
#         arr[k]=arr2[j]
#         k=k+1
#         j=j+1
#
# def mergesort(arr,l,r):
#     if(l<r):
#         mid=l+(r-l)//2
#         mergesort(arr,l,mid)
#         mergesort(arr,mid+1,r)
#         merge(arr,l,mid,r)
#
# from sys import setrecursionlimit
# setrecursionlimit(100000000)
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         mergesort(arr,0,n-1)
#         for i in range(n):
#             print(arr[i],end=' ')
#         print()
#         t=t-1
# if __name__ == '__main__':
#     main()

###Median of sorted array#######
# def insertionsort(arr,n):
#     for i in range(1,n):
#         temp=arr[i]
#         j=i-1
#         while(j>-1 and arr[j]>temp):
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=temp
#
# def main():
#     n=int(input())
#     arr=list(map(int,input().split()))
#     insertionsort(arr,n)
#     k=(n+1)//2
#     print(arr[k-1])
# if __name__ == '__main__':
#     main()

####Maximum chocolates########
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         arr.sort()
#         k=n-1
#         t=0
#         while(k>=0):
#             t=t+arr[k]
#             #print(t)
#             k=k-2
#         print(t)
#         T=T-1
#
# if __name__ == '__main__':
#     main()

####Arranging the stones#####
# def mergesortedarray(arr1,arr2,l1,l2):
#     arr3=[None]*(l1+l2)
#     i=0
#     j=0
#     k=0
#     while(i<l1 and j<l2):
#         if(arr1[i]<arr2[j]):
#             arr3[k]=arr1[i]
#             k=k+1
#             i=i+1
#         else:
#             arr3[k]=arr2[j]
#             k=k+1
#             j=j+1
#     while(i<l1):
#         arr3[k]=arr1[i]
#         k=k+1
#         i=i+1
#     while(j<l2):
#         arr3[k]=arr2[j]
#         k=k+1
#         j=j+1
#     return arr3
#
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         if(n%2==0):
#             mid=n//2
#         else:
#             mid=(n//2)+1
#         arr1=arr[0:mid]
#         arr2=arr[mid:n]
#         l1=len(arr1)
#         l2=len(arr2)
#         fin=mergesortedarray(arr1,arr2,l1,l2)
#         for i in range(l1+l2):
#             print(fin[i],end=' ')
#         print()
#         #print(arr1,arr2)
#         t=t-1
# if __name__ == '__main__':
#     main()

#######Sort the numbers#####
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         for i in range(n):
#             if(arr[i]==0):
#                 print(arr[i],end=' ')
#         for i in range(n):
#             if(arr[i]==1):
#                 print(arr[i],end=' ')
#         for i in range(n):
#             if(arr[i]==2):
#                 print(arr[i],end=' ')
#         print()
#         T=T-1
#
# if __name__ == '__main__':
#     main()

####The last game#####
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         arr.sort()
#         if(n%2==0):
#             mid=(n//2)-1
#         else:
#             mid=(n//2)
#         print(arr[mid])
#
#         T=T-1
#
# if __name__ == '__main__':
#     main()

####Find the misplaced elements######
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         arr1=[]
#         for i in range(n):
#             arr1.append(arr[i])
#         arr1.sort()
#         count=0
#         for i in range(n):
#             if(arr1[i]!=arr[i]):
#                 count+=1
#         print(count)
#         T=T-1
#
# if __name__ == '__main__':
#     main()


####Sort in a unique way######
# def merge(arr,l,mid,r):
#     n=mid-l+1
#     m=r-mid
#     arr1=[0]*n
#     arr2=[0]*m
#     for i in range(n):
#         arr1[i]=arr[l+i]
#     for i in range(m):
#         arr2[i]=arr[mid+1+i]
#     i=0
#     j=0
#     counter=0
#     counter1=0
#     while(i<n-1):
#         if(arr[i+1]>=arr[i]):
#             i+=1
#             counter1+=1
#         else:
#             break
#     if(counter1+1==n):
#         if(counter1>counter):
#             counter=counter1
#     counter2=0
#     while (j < m - 1):
#         if (arr[j + 1] >= arr[j]):
#             j += 1
#             counter2 += 1
#         else:
#             break
#     if (counter2 + 1 == m):
#         if (counter2 > counter):
#             counter=counter2
#     return counter
#
#
# def mergesort(arr,l,r):
#     counter=0
#     if(l<r):
#         mid=l+(r-l)//2
#         counter+=mergesort(arr,l,mid)
#         counter+=mergesort(arr,mid+1,r)
#         counter+=merge(arr,l,mid,r)
#     return counter
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         #count=0
#         #k=0
#         flag=True
#         for i in range(n-1):
#             if(arr[i+1]>=arr[i]):
#                 continue
#             else:
#                 flag=False
#         #print(count)
#         if(flag):
#             print(n)
#         else:
#             k=(mergesort(arr,0,n-1))
#             print(k)
#             # if(k==0):
#             #     print(1)
#             # else:
#             #     print(k)
#         T=T-1
# if __name__ == '__main__':
#     main()
# def merge(arr,l,mid,r):
#     n=mid-l+1
#     m=r-mid
#     arr1=[0]*n
#     arr2=[0]*m
#     for i in range(n):
#         arr1[i]=arr[l+i]
#     for i in range(m):
#         arr2[i]=arr[mid+1+i]
#     i=0
#     j=0
#     counter=0
#     counter1=0
#     while(i<n-1):
#         if(arr[i+1]>=arr[i]):
#             i+=1
#             counter1+=1
#         else:
#             break
#     if(counter1+1==n):
#         if(counter1>counter):
#             counter=counter1
#     counter2=0
#     while (j < m - 1):
#         if (arr[j + 1] >= arr[j]):
#             j += 1
#             counter2 += 1
#         else:
#             break
#     if (counter2 + 1 == m):
#         if (counter2 > counter):
#             counter=counter2
#     return counter
#
#
# def mergesort(arr,l,r):
#     counter=0
#     if(l<r):
#         mid=l+(r-l)//2
#         counter+=mergesort(arr,l,mid)
#         counter+=mergesort(arr,mid+1,r)
#         counter+=merge(arr,l,mid,r)
#     return counter
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         flag=True
#         for i in range(n-1):
#             if(arr[i+1]>=arr[i]):
#                 continue
#             else:
#                 flag=False
#         #print(count)
#         if(flag):
#             print(n)
#         else:
#             k=(mergesort(arr,0,n-1))
#             if(k==0):
#                 print(1)
#             else:
#                 print(k)
#         T=T-1
# if __name__ == '__main__':
#     main()
# def sort(arr,l,h):
#     c=0
#     r=0
#     y=0
#     mid=l+ (h-l)//2
#     for i in range(l,h):
#         if arr[i]<arr[i+1]:
#             c+=1
#             if i<=mid:
#                 r+=1
#             else:
#                 y+=1
#     if c==(h-l):
#         return c+1
#     elif r>=y:
#         return sort(arr,l,mid)
#     else:
#         return sort(arr,mid+1,k-1)
# t=int(input())
# for i in range(t):
#     k=int(input())
#     arr=list(map(int,input().split()))
#     count=0
#     for i in range(k-1):
#         if(arr[i+1]>=arr[i]):
#             count+=1
#     if(count==k-1):
#         print(k)
#     else:
#         print(sort(arr,0,k-1))

#####Quick sort#####
# def partition(arr,l,r):
#     x=arr[r]
#     i=l-1
#     for j in range(l,r):
#         if(arr[j]<=x):
#             i=i+1
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[i+1],arr[r]=arr[r],arr[i+1]
#     return i+1
#
# def quicksort(arr,l,r):
#     if(l<r):
#         p=partition(arr,l,r)
#         quicksort(arr,l,p-1)
#         quicksort(arr,p+1,r)
#
# from sys import setrecursionlimit
# setrecursionlimit(100000000)
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         quicksort(arr, 0, n - 1)
#         for i in range(n):
#             print(arr[i],end=' ')
#         print()
#
#         T=T-1
# if __name__ == '__main__':
#     main()

####Counting sort########
# def countingsort(arr,n,k):
#     freq=[0]*(k+1)
#     for i in range(n):
#         freq[arr[i]]+=1
#     count=[0]*(k+1)
#     count[0]=freq[0]
#     for i in range(1,k):
#         count[i]=count[i-1]+freq[i]
#     brr=[None]*n
#     for i in range(n-1,-1,-1):
#         count[arr[i]]-=1
#         brr[count[arr[i]]]=arr[i]
#     return brr
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         max=-1
#         for i in range(n):
#             if(max<arr[i]):
#                 max=arr[i]
#         k=max
#         arr=countingsort(arr,n,k)
#         for i in range(n):
#             print(arr[i],end=' ')
#         print()
#
#         T=T-1
# if __name__ == '__main__':
#     main()

#####Inversion count########
# def merge(arr,l,mid,r):
#     n=mid-l+1
#     m=r-mid
#     arr1=[0]*n
#     arr2=[0]*m
#     for i in range(n):
#         arr1[i]=arr[l+i]
#     for i in range(m):
#         arr2[i]=arr[mid+1+i]
#     inv_count=0
#     i=0
#     j=0
#     k=l
#     while(i<n and j<m):
#         if(arr1[i]<=arr2[j]):
#             arr[k]=arr1[i]
#             k=k+1
#             i=i+1
#         else:
#             arr[k]=arr2[j]
#             inv_count+=(n-i)
#             k=k+1
#             j=j+1
#     while(i<n):
#         arr[k]=arr1[i]
#         k=k+1
#         i=i+1
#     while (j < m):
#         arr[k] = arr2[j]
#         k = k + 1
#         j = j + 1
#     return inv_count
#
# def mergesort(arr,l,r):
#     inv_count=0
#     if(l<r):
#         mid=l+(r-l)//2
#         inv_count+=mergesort(arr,l,mid)
#         inv_count+=mergesort(arr,mid+1,r)
#         inv_count+=merge(arr,l,mid,r)
#     return inv_count
#
# from sys import setrecursionlimit
# setrecursionlimit(100000000)
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         print(mergesort(arr,0,n-1))
#         T=T-1
# if __name__ == '__main__':
#     main()

# def isPrime(n):
#     if (n <= 1): return False;
#     if (n <= 3): return True;
#
#     if (n % 2 == 0 or n % 3 == 0):
#         return False
#
#     i = 5;
#     while (i * i <= n):
#         if (n % i == 0 or n % (i + 2) == 0):
#             return False
#         i = i + 6
#
#     return True;
#
#
# def primeBitsInRange(l, r):
#     count = 0
#     for i in range(l, r + 1):
#
#         tot_bit = bin(i).count('1');
#         if (isPrime(tot_bit)):
#             count += 1;
#
#     return count;
#
#
# def main():
#     T=int(input())
#     while(T>0):
#         l,r=map(int,input().split())
#         print(primeBitsInRange(l,r))
#         T=T-1
#
# if __name__ == '__main__':
#     main()

# t = int(input())
# res = []
# for tc in range(t):
#     n = int(input())
#     items = list(map(int,input().split()))[:n]
#     i = 0
#     max = 0
#     itemType = items[0]
#     while i<n:
#         c = 1
#         j=i+1
#         while j<n:
#             if items[i]==items[j] and j!=i+1:
#                 c+=1
#                 if j<n-1 and items[j]==items[j+1]:
#                     j+=1
#
#             j+=1
#         if max<c:
#             max=c
#             itemType = items[i]
#             #print(items)
#         elif (max==c and itemType>items[i]):
#             max=c
#             itemType=items[i]
#             #print(items)
#         i+=1
#     res.append(itemType)
# for tc in range(t):
#     print(res[tc])
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         for i in range(n):
#             item=arr[i]
#             for j in range(i+1,n):
#
#         T=T-1
#
# if __name__ == '__main__':
#     main()


####Find the window######
# import sys
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         start=0
#         end=n-1
#
#         while(start<n-1):
#             if(arr[start]>arr[start+1]):
#                 break
#             start+=1
#         while(end>0):
#             if(arr[end]<arr[end-1]):
#                 break
#             end-=1
#         max=-1
#         min=sys.maxsize
#         for i in range(start,end+1):
#             if(max<arr[i]):
#                 max=arr[i]
#             if(min>arr[i]):
#                 min=arr[i]
#         for i in range(start):
#             if(arr[i]>min):
#                 start=i
#         for i in range(end,n):
#             if(arr[i]<max):
#                 end=i
#         print(start,end)
#
#         T=T-1
# if __name__ == '__main__':
#     main()

#######Search triplets#######
# def triplet(arr,n):
#     i=n-1
#     while(i>=0):
#         j=0
#         k=i-1
#         while(j<k):
#             flag=False
#             if(arr[i]==arr[j]+arr[k]):
#                 flag=True
#                 print(arr[i],arr[j],arr[k])
#                 return
#             elif(arr[i]>arr[j]+arr[k]):
#                 j+=1
#             else:
#                 k-=1
#         i-=1
#     if(flag==False):
#         print(-1)
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         triplet(arr,n)
#         T=T-1
# if __name__ == '__main__':
#     main()


#####Segregate negative and positive values#######
def merge(arr,temp,low,mid,high):
    k=low
    for i in range(low,mid+1):
        if(arr[i]<0):
            temp[k]=arr[i]
            k=k+1
    for j in range(mid+1,high+1):
        if(arr[j]<0):
            temp[k]=arr[j]
            k=k+1
    for i in range(low,mid+1):
        if(arr[i]>=0):
            temp[k]=arr[i]
            k=k+1
    for j in range(mid+1,high+1):
        if(arr[j]>=0):
            temp[k]=arr[j]
            k=k+1
    for i in range(low,high+1):
        arr[i]=temp[i]


def segregate(arr,temp,low,high):
    if(high==low):
        return
    mid=(low+high)//2
    segregate(arr,temp,low,mid)
    segregate(arr,temp,mid+1,high)
    merge(arr,temp,low,mid,high)
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=list(map(int,input().split()))
        temp=arr.copy()
        segregate(arr,temp,0,n-1)
        for ele in arr:
            print(ele,end=" ")
        print()
        T=T-1

if __name__ == '__main__':
    main()