# def PrintNum(n):
#     if(n==0):
#         return
#     print(n)
#     PrintNum(n-1)
#
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# def main():
#     n=int(input())
#     PrintNum(n)
#
# if __name__ =="__main__":
#     main()


####Factorial#######
# def Fact(n):
#     if(n==1 or n==0):
#         return 1
#     return n*Fact(n-1)
#
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# def main():
#     T=int(input())
#     while(T>0):
#       n=int(input())
#       print(Fact(n))
#       T=T-1
#
# if __name__ =="__main__":
#     main()


#####Sum of first N numbers######
# def SumofN(n):
#     if (n==1 or n==0):
#         return n
#     return n+SumofN(n-1)
#
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# def main():
#     T=int(input())
#     while(T>0):
#       n=int(input())
#       print(SumofN(n))
#       T=T-1
#
# if __name__ =="__main__":
#     main()


####Print the pattern###
# def printPattern(n):
#     if (n == 0 or n < 0):
#         print(n, end=" ")
#         return
#     print(n, end=" ")
#     printPattern(n - 5)
#     print(n, end=" ")
#
#
# T = int(input())
# while (T > 0):
#     n = int(input())
#     k = printPattern(n)
#     if k:
#         print(k)
#     T = T - 1

######Sum of digits######
# def findsum(n):
#     sum1=0
#     if (n<=0):
#         return 0
#     return n%10+findsum(n//10)
#
#
# def main():
#     n=int(input())
#     print(findsum(n))
# if __name__ == '__main__':
#     main()
#

#####Fibonacci Numbers######
# def fibonacci(n):
#     if (n==1 or n==0):
#         return n
#     else:
#         return fibonacci(n-1) +fibonacci(n-2)
#
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# def main():
#     T=int(input())
#     while(T>0):
#       n=int(input())
#       print(fibonacci(n))
#       T=T-1
#
# if __name__ =="__main__":
#     main()

######Binary numbers#####
# def binary(n,prev,output,i):
#     if(n==0):
#         for j in range(len(output)):
#             print(output[j],end="")
#         print()
#         return
#     if(prev==0 or prev==-1):
#         output[i]=0
#         binary(n-1,0,output,i+1)
#         output[i]=1
#         binary(n-1,1,output,i+1)
#     else:
#         output[i]=0
#         binary(n-1,0,output,i+1)
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         output=[-1]*n
#         binary(n,-1,output,0)
#         T=T-1
#
# if __name__=="__main__":
#     main()


#######GCD of numbers########
'''Basic Euclidean Algorithm for GCD
The algorithm is based on the below facts.

If we subtract a smaller number from a larger (we reduce a larger number), GCD doesn’t change. So if we keep subtracting
repeatedly the larger of two, we end up with GCD.
Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find remainder 0.
Below is a recursive function to evaluate gcd using Euclid’s algorithm. We can also use modulo operator to work like subtraction'''
# def GCD(a,c):
#     if (c == 0):
#         return a
#     return GCD(c,a%c)
#
# def main():
#     T=int(input())
#     while(T>0):
#         N,P=map(int,input().split())
#         print(GCD(N,P))
#         T=T-1
# if __name__=="__main__":
#     main()

###Combination of numbers#####
# def recurCombi(arr,op,i,index,n,k):
#     if(k==0):
#         for j in range(len(op)):
#             print(op[j],end=' ')
#         print()
#         return
#     for j in range(i,n):
#         op[index]=arr[j]
#         recurCombi(arr,op,j+1,index+1,n,k-1)
# def main():
#     n=int(input())
#     arr=list(map(int,input().split()))
#     k=int(input())
#     op=[0]*k
#     #(arr,op,2indexes for each recursion call,to insert elements in the output list)
#     recurCombi(arr,op,0,0,n,k)
#
# if __name__ == '__main__':
#     main()


####Same String#####
# def isSame(st1):
#     l=len(st1)
#     if l<2:
#         return True
#     elif(st1[0]==st1[l-1]):
#         return isSame(st1[1:l-1])
#     else:
#         return False
# def main():
#     T=int(input())
#     while(T>0):
#         st1=input()
#         ans=isSame(st1)
#         if ans:
#             print("Yes")
#         else:
#             print("No")
#         T=T-1
#
# if __name__ == '__main__':
#     main()


###Sum of subsets###
# def SumOfSubset(a, n):
#     times = pow(2, n - 1)
#
#     Sum = 0
#
#     for i in range(n):
#         Sum = Sum + (a[i] * times)
#
#     return Sum
#
# def main():
#     # Driver Code
#     T=int(input())
#     while(T>0):
#         n = int(input())
#         arr = list(map(int, input().split()))
#         print(SumOfSubset(arr, n))
#         T=T-1
#
# if __name__ == '__main__':
#     main()


#####Equivalent Strings########
# def equal(s):
#     if(len(s)%2!=0):
#         return s
#     a1=equal(s[0:int(len(s)/2)])
#     a2=equal(s[int(len(s)/2):len(s)])
#     if(a1<a2):
#         return a1+a2
#     else:
#         return a2+a1
#
# def main():
#     a=input()
#     b=input()
#     k=int(len(a))
#     if ((equal(a)==equal(b))):
#         print("YES")
#     else:
#         print("NO")
#
# if __name__ == '__main__':
#     main()

###Solution of equation#####
# def count(n,z):
#     total=0
#     if(n==1 and z>=0):
#         return 1
#     for i in range (z+1):
#         total+=count(n-1,z-i)
#     return total
#
# def main():
#     T=int(input())
#     while(T>0):
#         n, z = map(int, input().split())
#         print(count(n, z))
#         T=T-1
# if __name__ == '__main__':
#     main()


###power set###
# def permuterec(str1,n,index=-1,curr=""):
#     if(index==n):
#         return
#     if len(curr)>0:
#         print(curr)
#     for i in range(index+1,n):
#         curr+=str1[i]
#         permuterec(str1,n,i,curr)
#
#         curr=curr[:len(curr)-1]
#
# def powerset(str1):
#     str1="".join(sorted(str1))
#     permuterec(str1,len(str1))
#
#
# def main():
#     str1= input()
#     powerset(str1)
#
# if __name__ == '__main__':
#     main()

####Remove adjacent duplicates######
# def removeAdjDup(str):
#     if(len(str)==1):
#         return str
#     if(str[0]==str[1]):
#         return removeAdjDup(str[1:])
#     return str[0]+removeAdjDup(str[1:])
#
# def main():
#     T=int(input())
#     while(T>0):
#         str=input()
#         print(removeAdjDup(str))
#         T=T-1
# if __name__ == '__main__':
#     main()


###Tower of Hanoi######
# def TowerofHanoi(n,source,destination,helper):
#     if(n==1):
#         print("Move disk from",source," to ",destination)
#         return
#     TowerofHanoi(n-1,source,helper,destination)
#     print("Move disk from", source, " to ", destination)
#     TowerofHanoi(n-1,helper,destination,source)
#
# def main():
#     n = int(input())
#     print(TowerofHanoi(n,1,3,2))
#
# if __name__ == '__main__':
#     main()
global total
total=0
def subsetsum(arr,i,n,sum):
    global total
    if(i>=n):
        total+=sum
        print(total)
        return total
    print(i+1)
    subsetsum(arr,i+1,n,sum+arr[i])
    subsetsum(arr,i+1,n,sum)
def main():
    T=int(input())
    k=0
    while(T>0):
        n = int(input())
        arr = list(map(int, input().split()))
        k=subsetsum(arr,0, n,0)
        print(k)
        T=T-1

if __name__ == '__main__':
    main()
