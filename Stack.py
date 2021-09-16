####Stack using arrays########
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#     def pop(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         else:
#             self.tos=self.tos-1
#             self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is Empty")
#             return
#         return self.arr[self.tos]
#
# def main():
#     st=Stack()
#     n=int(input())
#     for ele in input().split():
#         st.push(int(ele))
#     print(st.size())
#     while(st.size()!=0):
#         print(st.top())
#         st.pop()
#
# if __name__ == '__main__':
#     main()

#####Stack from linked list#########
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Stack:
#     def __init__(self):
#         self.head=None
#         self.tos=-1
#     def isEmpty(self):
#         if(self.head is None):
#             return True
#         return False
#     def push(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tos+=1
#             return
#         newNode.next=self.head
#         self.head=newNode
#         self.tos+=1
#
#     def pop(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         self.head=self.head.next
#         self.tos-=1
#     def size(self):
#         return self.tos+1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         return self.head.data
#
# def main():
#     st=Stack()
#     for ele in input().split():
#         st.push(int(ele))
#     print(st.size())
#     while(st.size()!=0):
#         print(st.top())
#         st.pop()
#
# if __name__ == '__main__':
#     main()

###Balanced bracket expression###
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#     def pop(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         else:
#             self.tos=self.tos-1
#             self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is Empty")
#             return
#         return self.arr[self.tos]
#
# def main():
#     t=int(input())
#     while(t>0):
#         st = Stack()
#         str=input()
#         flag=1
#         for ele in str:
#             if(ele=='('):
#                 st.push(ele)
#             else:
#                 if(st.isEmpty()):
#                     flag=0
#                     break
#                 st.pop()
#         if(st.isEmpty() is False or flag==0):
#             print("Bracket expression is not balanced")
#         else:
#             print("Bracket expression is balanced")
#
#         t=t-1
#
# if __name__ == '__main__':
#     main()

######Balanced bracket expression(multiple type of brackets)######
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#     def pop(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         else:
#             self.tos=self.tos-1
#             self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is Empty")
#             return
#         return self.arr[self.tos]
# def main():
#     t=int(input())
#     while(t>0):
#         st = Stack()
#         str=input()
#         flag=1
#         for ele in str:
#             if(ele=='(' or ele=='[' or ele=='{'):
#                 st.push(ele)
#             else:
#                 if(st.isEmpty()):
#                     flag=0
#                     break
#                 if((st.top()=='(' and ele==')') or (st.top()=='[' and ele==']') or (st.top()=='{' and ele=='}')):
#                     st.pop()
#         if(st.isEmpty()==False or flag==0):
#             print("Not balanced")
#         else:
#             print("Balanced")
#         t=t-1
#
# if __name__ == '__main__':
#     main()

#####Infix to postfix########
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#     def pop(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         else:
#             self.tos=self.tos-1
#             self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is Empty")
#             return
#         return self.arr[self.tos]
# def precedence(str):
#     if(str=="^"):
#         return 3
#     if(str=="*" or str=="/"):
#         return 2
#     if(str=="+" or str=="-"):
#         return 1
#     if(str=='(' or str==")"):
#         return -1
#     else:
#         return 0 #meaning its an operand and not an operator
#
# def main():
#     st=Stack()
#     arr=list(input().split())
#     ans=""
#     for i in range(len(arr)):
#         val=precedence(arr[i])
#         if(val==0):
#             ans+=arr[i]
#         else:
#             #If arr[i] is opening bracket
#             if(arr[i]=="("):
#                 st.push(arr[i])
#             elif(arr[i]==")"):
#                 while(st.isEmpty() is False and st.top()!="("):
#                     ans+=st.top()
#                     st.pop()
#                 if(st.top()=="("):
#                     st.pop()
#             #if arr[i] is an operator
#             else:
#                 while(st.isEmpty() is False and precedence(arr[i])<=precedence(st.top())):
#                     ans+=st.top()
#                     st.pop()
#                 st.push(arr[i])
#     while(st.isEmpty() is False):
#         ans+=st.top()
#         st.pop()
#     print(ans)
#
# if __name__ == '__main__':
#     main()

#####Evaluation of postfix expression########
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#     def pop(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         else:
#             self.tos=self.tos-1
#             self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is Empty")
#             return
#         return self.arr[self.tos]
#
# def isOp(str):
#     if(str=="*"):
#         return 4
#     if(str=="/"):
#         return 3
#     if(str=="-"):
#         return 2
#     if(str=="+"):
#         return 1
#     else:
#         return 0
# def main():
#     st=Stack()
#     n=int(input())
#     arr=list(input().split())
#     for i in range(n):
#         val=isOp(arr[i])
#         if(val==0):
#             st.push(int(arr[i]))
#         else:
#             op1=st.top()
#             st.pop()
#             op2=st.top()
#             st.pop()
#             if(val==4):
#                 st.push(op2*op1)
#             if(val==3):
#                 st.push(op2/op1)
#             if(val==2):
#                 st.push(op2-op1)
#             if(val==1):
#                 st.push(op2+op1)
#     print(st.top())
#
#
#
# if __name__ == '__main__':
#     main()
# import sys
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#         self.min_ele = sys.maxsize
#         self.min = []
#     def push(self,data):
#         if (self.top==-1):
#             self.top += 1
#             self.arr.append(data)
#             self.min_ele = data
#             self.min.append(self.min_ele)
#             return
#         self.tos+=1
#         self.arr.append(data)
#         self.min_ele=min(self.min_ele,data)
#         self.min.append(self.min_ele)
#     def pop(self):
#         if(self.isEmpty()):
#             print(-1)
#             return
#         else:
#             self.tos=self.tos-1
#             popped_ele=self.arr.pop()
#             self.min.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print(-1)
#             return
#         print(self.arr[self.tos])
#     def getMin(self):
#         if(self.isEmpty()):
#             print (-1)
#             return
#         print(self.min_ele)
#
# def main():
#     st=Stack()
#     q=int(input())
#     for i in range(q):
#         l=list(map(int,input().split()))
#         q1=l[0]
#         if(q1==1):
#             q2=l[1]
#             st.push(q2)
#         if(q1==2):
#             st.pop()
#         if(q1==3):
#             st.top()
#         if(q1==4):
#             st.getMin()
#
#
#
# if __name__ == '__main__':
#     main()

####Stock span problem####
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         span=[1]*n
#         for i in range(1,n):
#             for j in range(i-1,-1,-1):
#                 if(arr[i]>=arr[j]):
#                     span[i]+=1
#                 else:
#                     break
#         for ele in span:
#             print(ele,end=" ")
#         print()
#         t=t-1
# if __name__ == '__main__':
#     main()

####Stock span problem(optimized approach)###
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         st=[]
#         st.append(0)
#         span=[1]*n
#         for i in range(1,n):
#             while(len(st)>0 and arr[st[-1]]<=arr[i]):
#                 st.pop()
#             if(len(st)<=0):
#                 span[i]=i+1
#             else:
#                 span[i]=i-st[-1]
#             st.append(i)
#         for ele in span:
#             print(ele,end=" ")
#         print()
#         t=t-1
# if __name__ == '__main__':
#     main()

####Sort stack using recursion####
# def insertSorted(stack,value):
#     if(len(stack)==0 or value>stack[-1]):
#         stack.append(value)
#         return
#     top=stack.pop()
#     insertSorted(stack,value)
#     stack.append(top)
# def stackSorting(stack):
#     if(len(stack)==0):
#         return
#     top=stack.pop()
#     stackSorting(stack)
#     insertSorted(stack,top)
#
# def main():
#     stack=list(map(int,input().split()))
#     print("Stack before sorting=",stack)
#     stackSorting(stack)
#     print("Stack after sorting=", stack)
# if __name__ == '__main__':
#     main()

######Find the redundant bracket#####
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#     def pop(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         else:
#             self.tos=self.tos-1
#             self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is Empty")
#             return
#         return self.arr[self.tos]
#
# def main():
#     t=int(input())
#     while(t>0):
#         st = Stack()
#         str=input()
#         flag=1
#         for ele in str:
#             if(ele=='(' or ele=="+" or ele=="-" or ele=="*" or ele=="/" ):
#                 st.push(ele)
#             else:
#                 if(st.isEmpty()):
#                     flag=0
#                     break
#                 st.pop()
#         if(st.isEmpty() is False or flag==0):
#             print("Bracket expression is not balanced")
#         else:
#             print("Bracket expression is balanced")

#         t=t-1
#
# if __name__ == '__main__':
#     main()

###GetMinimum Element From Stack###
# class stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#         self.minarr=[]
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#         if(len(self.minarr)==0 or self.minarr[-1]>=data):
#             self.minarr.append(data)
#     def pop(self):
#         if(self.isEmpty() or len(self.minarr)==0):
#             print(-1)
#             return
#         else:
#             x=self.arr[-1]
#             self.tos-=1
#             self.arr.pop()
#             if(x==self.minarr[-1]):
#                 self.minarr.pop()
#     def top(self):
#         if (self.isEmpty()):
#             print(-1)
#             return
#         print(self.arr[self.tos])
#     def getMin(self):
#         if(self.isEmpty() or len(self.minarr)==0):
#             print(-1)
#             return
#         print( self.minarr[-1])
#
#     def isEmpty(self):
#         return self.tos==-1
# def main():
#     st=stack()
#     q=int(input())
#     for i in range(q):
#         l=list(map(int,input().split()))
#         q1=l[0]
#         if(q1==1):
#             q2=l[1]
#             st.push(q2)
#         if(q1==2):
#             st.pop()
#         if(q1==3):
#             st.top()
#         if(q1==4):
#             st.getMin()
# if __name__ == '__main__':
#     main()

#####Find the redundant braces####
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.tos=-1
#     def push(self,data):
#         self.tos+=1
#         self.arr.append(data)
#     def pop(self):
#         if(self.isEmpty()):
#             return
#         else:
#             self.tos-=1
#             self.arr.pop()
#
#     def top(self):
#         if(self.isEmpty()):
#             return
#         else:
#             return self.arr[self.tos]
#
#     def isEmpty(self):
#         return self.tos==-1
# def main():
#     st=Stack()
#     str=input()
#     ops=['+','-','*','/']
#     for ele in str:
#         if (ele == '(' ):
#             st.push(ele)
#         elif(ele in ops):
#             st.pop()
#     if (st.isEmpty()):
#         print(0)
#     else:
#         print(1)
# if __name__ == '__main__':
#     main()

####Compile code####
class stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1
    def push(self,data):
        self.tos+=1
        self.arr.append(data)
    def pop(self):
        if(self.isEmpty()):
            return
        self.tos-=1
        self.arr.pop()
    def isEmpty(self):
        return self.tos==-1
def main():
    st=stack()
    t=int(input())
    while(t>0):
        n=int(input())
        arr1=input()
        for ele in arr1:
            if(ele=='<'):
                st.push()
            elif(ele=='>'):
                st.pop()
        t=t-1