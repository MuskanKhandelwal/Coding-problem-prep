# T=int(input())
# while(T>0):
#   n=int(input())
#   name=input()
#   a=0
#   d=0
#   A='A'
#   D='D'
#   for ele in name:
#     if(A in ele):
#       a+=1
#
#     elif(D in ele):
#         d += 1
#
#
#   if(a>d):
#     print("Aditya")
#   elif(a<d):
#     print("Danish")
#   else:


#     print("AdiDan")
#   T=T-1


####Duplicate Character#####
# T=int(input())
# while(T>0):
#     str=input()
#     freq=[0]*26
#     for i in range(len(str)):
#         freq[ord(str[i])-97]+=1
#     flag=0
#     for i in range(26):
#         if(freq[i]>1):
#             print("{}={}".format(chr(i+97),freq[i]),end=' ')
#             flag=1
#     if(flag==0):
#         print(-1)
#     else:
#         print()
#     T=T-1

###Print prefix and suffix#####
# str1=input()
# for i in range(0,len(str1)):
#     for j in range(0,i+1):
#         print(str1[j],end='')
#     print()
#
# for i in range(len(str1)):
#     print(str1[len(str1)-i-1:len(str1)])
#


####Fake password##
# T=int(input())
# while(T>0):
#     org=input()
#     fake=input()
#     lf=fake[0:2]
#     lr=fake[2:]
#     left=lr+lf
#     right=fake[len(fake)-2:]+fake[0:len(fake)-2]
#     if(org==left or org==right):
#         print("Yes")
#     else:
#         print("No")
#     T=T-1

####Noble Vowel#####
# T=int(input())
# vowel="aeiou"
# k=0
# while(T>0):
#   str1 = input()
#   for i in range(len(str1)-1):
#     if(i!=len(str1) and str1[i]!='n' and str1[i] not in vowel):
#       if((str1[i+1] in vowel)):
#         k=1
#       else:
#         k=-1
#         break
#     elif(str1[i] in vowel):
#         k=1
#     elif(str1[i]=='n'):
#         k=1
#     else:
#         k=-1
#   if((str1[len(str1)-1] not in vowel)and (str1[len(str1)-1]!='n')):
#       k=-1
#   if(len(str1)==1):
#       if(str1[0]=='n' or str1 in vowel):
#           k=1
#       else:
#           k=-1
#
#   if(k==1):
#     print("YES")
#   elif(k==-1):
#     print("NO")
#   T=T-1



####Find first character#########
# def countNonRepeating(inputStr):
#     resSeen=[]
#     resUnseen=[]
#     for ele in inputStr:
#         if ele in resUnseen:
#             resSeen.append(ele)
#             resUnseen.remove(ele)
#         elif ele in resSeen:
#             continue
#         else:
#             resUnseen.append(ele)
#     if(resUnseen):
#         return inputStr.find(resUnseen[0])
#     else:
#         return -1
#
# for _ in range(int(input())):
#     print(countNonRepeating(input()))


######Decreasing order strings########
# T=int(input())
# while(T>0):
#   st=input()
#   num=[]
#   for ele in st:
#     num.append(ord(ele))
#   num.sort(reverse=True)
#   for i in range(len(num)):
#       print(chr(num[i]),end='')
#   print()
#   T=T-1

####Aman string #####
# T=int(input())
# while(T>0):
#     substr = []
#     def substring(s,n):
#         # Extract 4 length substrings
#         # Using list comprehension + string slicing
#         res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if
#                len(s[i:j]) >= 4]
#         for i in range(len(res)):
#             if("aman" in res[i]):
#                 substr.append(res[i])
#
#     st=input()
#     k="aman"
#     index=[]
#     substring(st,len(st))
#     print(len(substr))
#
#     T=T-1

######Equal string#########(A day spent solving)
# T = int(input())
# while (T > 0):
#     def min_moves(arr,n):
#         m = 10000000
#         for i in range(0,n):
#             curr_count=0
#             for j in range(0,n):
#                 tmp=arr[j]+arr[j]
#                 index=tmp.find(arr[i])
#                 #print(index)
#                 if(index==len(arr[i])):
#                     return -1
#                 curr_count+=index
#             m=min(curr_count,m)
#         return m
#
#
#     n = int(input())
#     st=[]
#     sum=0
#     for i in range(n):
#         st.append(input())
#     out=[]
#     l = len(st[0])
#     #print(l)
#     res=min_moves(st,n)
#     #print(res)
#     if(res<0):
#         print(-1)
#     else:
#         print(res)
#     T = T - 1

####valid string ######
# n=int(input())
# s=[]
# b="()"
# r="("
# l=")"
# #Function to remove () from the string and then count the remaining ( ,)
# def findequal(st):
#     if (len(st) % 2 == 0):
#         while(st.count(b)>0):
#             st=st.replace("()","")
#         #print(st)
#         if (len(st) == 0):
#             return "Yes"
#         elif (st.count(r) == 1 and st.count(l) == 1):
#             return "Yes"
#         elif (st.count(r) > 1 or st.count(l)>1):
#             return "No"
#     else:
#         return "No"
#
# for i in range(n):
#     s.append(input())
# for i in range (n):
#     k=findequal(s[i])
#     print(k)


######Good Prefix#######
# def main():
#     t=int(input())
#     while(t!=0):
#         st=input()
#         k,x=map(int, input().split())
#         count=0
#         freq=[0]*26
#         for i in range(len(st)):
#             ele=ord(st[i])-97
#             freq[ele]+=1
#             if(freq[ele]>x):
#                 if(k>0):
#                     freq[ele]-=1
#                     k-=1
#                 else:
#                     break
#             else:
#                 count+=1
#         print(count)
#         t=t-1
#
# if __name__ == "__main__":
#     main()

#####Find your gift######
# def main():
#     t=int(input())
#     while(t!=0):
#         n=int(input())
#         st=input()
#         x=0
#         y=0
#         cc=''
#         if(st[0]=='L'):
#             x-=1
#             cc='L'
#         elif(st[0]=='R'):
#             x+=1
#             cc='R'
#         elif (st[0] == 'U'):
#             y += 1
#             cc = 'U'
#         else:
#             y -= 1
#             cc = 'D'
#
#         for i in range(1,n):
#             if(cc=='L' or cc=='R'):
#                 if(st[i]=='U'):
#                     y+=1
#                     cc='U'
#                 elif(st[i]=='D'):
#                     y-=1
#                     cc='D'
#             else:
#                 if (st[i] == 'R'):
#                     x += 1
#                     cc = 'R'
#                 elif (st[i] == 'L'):
#                     x -= 1
#                     cc = 'L'
#         print(x,y)
#         t=t-1
#
# if __name__ == "__main__":
#     main()

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

###Chaturs exam paper######
# T=int(input())
# while(T>0):
#   st1=input()
#   n=int(len(st1)/2)
#   sum=0
#   #print(n)
#   for i in range(0,n):
#     if(st1[i]!=st1[len(st1)-i-1]):
#       sum+=abs(ord(st1[i])-ord(st1[len(st1)-i-1]))
#   print(sum)
#   T=T-1


###Subsequence(codechef)#####
# import  sys
# def main():
#     t=int(input())
#     while(t!=0):
#         n=int(input())
#         st=input()
#         min=sys.maxsize
#         lastoccur=[-1]*26
#         for i in range(n):
#             ele=ord(st[i])-97
#             if(lastoccur[ele]==-1):
#                 lastoccur[ele]=i
#             else:
#                 val=i-lastoccur[ele]-1
#                 lastoccur[ele]=i
#                 if(min>val):
#                     min=val
#         if(min==sys.maxsize):
#             print(0)
#         else:
#             print(n-1-min)
#         t=t-1
#
# if __name__ == "__main__":
#     main()

####Plus plus is minus#####
# t=int(input())
# while(t>0):
#   st1=input()
#   st2=input()
#   l=0
#   r=0
#   for i in range(min(len(st1),len(st2))):
#     if(st1[l]==st2[r]):
#       #print(st1[l], st2[r])
#       l+=1
#       r+=1
#       continue
#
#     elif(st1[l]=="-" and st1[l+1]=="-" and st2[r]=="+"):
#       #print(st1[l], st2[r])
#       l+=2
#       r+=1
#     else:
#       break
#
#   if(l==len(st1) and r==len(st2)):
#     print("YES")
#   else:
#     print("NO")
#   t=t-1

###Pattern concatenation###
T=int(input())
while(T>0):
    def findvalid(st1):
        for i in range(2,len(st1)):
            if((int(st1[i]))==int(st1[i-1])+int(st1[i-2])):
                k=1
            else:
                k=-1
                #print((int(st1[2])+(int(st1[1]))))
                break

        return k
    n=input()
    if(len(n)==1):
        print("no")
        break
    elif (n[0]== n[1] and len(n)==2):
        print("Yes")
        break
    else:
        z=findvalid(n)
    if(z==1):
        print("yes")
    elif(z==-1):
        print("no")
    T=T-1