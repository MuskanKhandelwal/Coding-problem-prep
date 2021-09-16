####Introduction to linked list#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# x=Node(10) #So the node will be named x and its next value will be none for now
# y=Node(20)
# print(x)
# print(y)
# x.next=y
# print(x.next)
# print(y.data)
# print(y.next)
# print(x.data)
# print(x.next.data)
#print(y.next.data) #AttributeError: 'NoneType' object has no attribute 'data'


####Create singly linked list using INSERTION AT THE END####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#         else:
#             temp=self.head
#             while(temp.next is not None):
#                 temp=temp.next
#             temp.next=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):   ##Here not temp.next because we want to get to last node print it and then cross it
#             print(temp.data,end=' ')
#             print(temp,end=' ')
#             print(temp.next)
#             temp=temp.next
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

####Create singly linked list using INSERTION AT THE END USING TAIL####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             print(temp,end=' ')
#             print(temp.next)
#             temp=temp.next
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()


####Create singly linked list using INSERTION AT THE BEGINNING####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def insertAtbegin(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#         else:
#             newNode.next=self.head
#             self.head=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             print(temp,end=' ')
#             print(temp.next)
#             temp=temp.next
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtbegin(arr[i])
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

######Singly linked list Insertion at ith position#########
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def insertAtBeginning(self,data):
#         newNode = Node(data)
#         if(self.head is None):
#             self.head=newNode
#         else:
#             newNode.next=self.head
#             self.head=newNode
#     def insertAtithPosition(self,i,data):
#         newNode=Node(data)
#         if(i==0):
#             self.insertAtBeginning(data)
#         else:
#             count=0
#             temp=self.head
#             while(temp.next is not None and count is not i-1):
#                 count+=1
#                 temp=temp.next
#             if(temp.next is None and i>count+1): ##invalid position
#                 return
#             else:
#                 newNode.next=temp.next
#                 temp.next=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             # print(temp,end=' ')
#             # print(temp.next)
#             temp=temp.next
#         print()
# def main():
#     SinglyLinkedList= LinkedList()
#     SinglyLinkedList2=LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtBeginning(arr[i])
#         SinglyLinkedList2.insertAtEnd(arr[i])
#     SinglyLinkedList2.insertAtithPosition(5,100)
#
#     SinglyLinkedList.printSinglyLinkedList()
#     SinglyLinkedList2.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

####Find the middle element######
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             temp=temp.next
#         print()
#     def printMidElement(self,mid):
#         count=0
#         temp=self.head
#         while(temp is not None and count!=mid):
#             count+=1
#             temp=temp.next
#         print(temp.data)
#
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         singlyLinkedList=LinkedList()
#         arr=list(map(int,input().split()))
#         if (n % 2 == 0):
#             mid = (n // 2)
#         else:
#             mid = n // 2
#         for i in range (n):
#             singlyLinkedList.insertAtEnd(arr[i])
#         singlyLinkedList.printMidElement(mid)
#
#         T=T-1
#
# if __name__ == '__main__':
#     main()

####Length of linked list(Iteratively)####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             temp=temp.next
#     def lengthofLinkedList(self):
#         temp=self.head
#         count=0
#         while(temp is not None):
#             count+=1
#             temp=temp.next
#         return count
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     print(SinglyLinkedList.lengthofLinkedList())
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

####Length of linked list(Recursively)####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             temp=temp.next
#     def LLR(self,temp):
#         if(temp is None):
#             return 0
#         else:
#             return 1+self.LLR(temp.next)
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     temp=SinglyLinkedList.head
#     print(SinglyLinkedList.LLR(temp))
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

####Deletion at the end (Single linked list)#######
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def deleteAtEnd(self):
#         if(self.head is None):
#             return
#         elif(self.head.next is None):
#             self.head=None
#         else:
#             sl=self.head
#             while(sl.next.next is not None):
#                 sl=sl.next
#             self.tail=sl
#             sl.next=None
#
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             temp=temp.next
#
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     SinglyLinkedList.deleteAtEnd()
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

####Deletion at the beginning (Single linked list)#######
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def deleteAtBegin(self):
#         if(self.head is None):
#             return
#         else:
#             self.head=self.head.next
#
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             temp=temp.next
#
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     SinglyLinkedList.deleteAtBegin()
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

####Deletion at ith position######
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#         else:
#             self.tail.next=newNode
#             self.tail=newNode
#     def deleteAtBegin(self):
#         if(self.head is None):
#             return
#         else:
#             self.head=self.head.next
#     def deleteAtGivenPosition(self,i):
#         n=self.LLR(self.head)
#         if(self.head is None or i>n-1):
#             return
#         if(i==0):
#             self.deleteAtBegin()
#             return
#         if(i==n-1):
#             self.deleteAtEnd()
#             return
#         count=0
#         temp=self.head
#         while(temp is not None and count is not (i-1)):
#             count+=1
#             temp=temp.next
#         temp.next=temp.next.next
#
#     def LLR(self, temp):
#         if(temp is None):
#             return 0
#         else:
#             return 1+self.LLR(temp.next)
#
#     def deleteAtEnd(self):
#         if(self.head is None):
#             return
#         elif(self.head.next is None):
#             self.head=None
#         else:
#             sl=self.head
#             while(sl.next.next is not None):
#                 sl=sl.next
#             self.tail=sl
#             sl.next=None
#
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             temp=temp.next
#
# def main():
#     SinglyLinkedList= LinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     #SinglyLinkedList.deleteAtBegin()
#     SinglyLinkedList.deleteAtGivenPosition(3)
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

####Doubly linked list#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# def main():
#     x=Node(1)
#     y=Node(2)
#     z=Node(3)
#     p=Node(4)
#     x.next=y
#     y.prev=x
#     y.next=z
#     z.prev=y
#     z.next=p
#     p.prev=z
#     temp=x
#     while(temp is not None):
#         print(temp.prev,end=' ')
#         print(temp.data,end=' ')
#         print(temp,end=' ')
#         print(temp.next)
#         temp=temp.next
#
# if __name__ == '__main__':
#     main()

#####Insert at begin and end of doubly linked list#####
# class Node:
#     def __init__(self,data):
#         self.next=None
#         self.data=data
#         self.prev=None
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtBeginning(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             return
#         self.head.prev=newNode
#         newNode.next=self.head
#         self.head=newNode
#
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             return
#         self.tail.next=newNode
#         newNode.prev=self.tail
#         self.tail=newNode
#
#     def insertAtGivenPosition(self,i,data):
#         newNode=Node(data)
#         n=self.lengthofLinkedList()
#         if(i==0):
#             self.insertAtBeginning(data)
#             return
#         if(i==n):
#             self.insertAtEnd(data)
#             return
#         if(i>n):
#             print("Invaid position")
#             return
#         count=0
#         temp=self.head
#         while(temp.next is not None and count is not (i-1)):
#             count+=1
#             temp=temp.next
#         newNode.prev=temp
#         newNode.next=temp.next
#         temp.next.prev=newNode
#         temp.next=newNode
#
#     def printDoublyLinkedList(self):
#         temp=self.head
#         while (temp is not None):
#             print(temp.prev, end=' ')
#             print(temp.data, end=' ')
#             print(temp,end=' ')
#             print(temp.next)
#             temp = temp.next
#     def lengthofLinkedList(self):
#         temp=self.head
#         count=0
#         while(temp is not None):
#             count+=1
#             temp=temp.next
#         return count
# def main():
#     doublyLinkedList=DoublyLinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         doublyLinkedList.insertAtBeginning(arr[i])
#     doublyLinkedList.insertAtGivenPosition(3,100)
#     doublyLinkedList.printDoublyLinkedList()
#     doublyLinkedList.insertAtGivenPosition(0, 100)
#     doublyLinkedList.printDoublyLinkedList()
#     doublyLinkedList.insertAtGivenPosition(6, 100)
#     doublyLinkedList.printDoublyLinkedList()
# if __name__ == '__main__':
#     main()

####Double linked list(deletion)#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class DoublyLinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def deletionFromEnd(self):
#         if(self.head is None):
#             print("Linked list is empty")
#             return
#         temp=self.tail.prev
#         temp.next=None
#         self.tail.prev=None
#         self.tail=temp
#     def deletionFromBeginning(self):
#         if (self.head is None):
#             print("Linked list is empty")
#             return
#         temp=self.head.next
#         if(temp is None):
#             self.head=None
#             return
#         self.head.next=None
#         temp.prev=None
#         self.head=temp
#     def deleteFromGivenPosition(self,i):
#         n=self.lengthofLinkedList()
#         if(i>=n):
#             print("Invalid position")
#             return
#         if(i==0):
#             self.deletionFromBeginning()
#             return
#         if(i==n-1):
#             self.deletionFromEnd()
#             return
#         count=0
#         temp=self.head
#         while(temp.next is not None and count is not i):
#             count+=1
#             temp=temp.next
#         temp1=temp.prev
#         temp2=temp.next
#         temp.prev=None
#         temp.next=None
#         temp1.next=temp2
#         temp2.prev=temp1
#
#     def printDoublyLinkedList(self):
#         temp=self.head
#         while (temp is not None):
#             #print(temp.prev, end=' ')
#             print(temp.data, end=' ')
#             #print(temp,end=' ')
#             #print(temp.next)
#             temp = temp.next
#         print()
#
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             return
#         self.tail.next=newNode
#         newNode.prev=self.tail
#         self.tail=newNode
#
#     def lengthofLinkedList(self):
#         temp=self.head
#         count=0
#         while(temp is not None):
#             count+=1
#             temp=temp.next
#         return count
# def main():
#     doublyLinkedList=DoublyLinkedList()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         doublyLinkedList.insertAtEnd(arr[i])
#     doublyLinkedList.deleteFromGivenPosition(3)
#     doublyLinkedList.printDoublyLinkedList()
#     doublyLinkedList.deleteFromGivenPosition(0)
#     doublyLinkedList.printDoublyLinkedList()
#     doublyLinkedList.deleteFromGivenPosition(doublyLinkedList.lengthofLinkedList()-1)
#     doublyLinkedList.printDoublyLinkedList()
#     # doublyLinkedList.deletionFromEnd()
#     # doublyLinkedList.printDoublyLinkedList()
#     # doublyLinkedList.deletionFromBeginning()
#     # doublyLinkedList.printDoublyLinkedList()
#
# if __name__ == '__main__':
#     main()


###Circular Linked list#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# x=Node(10)
# y=Node(20)
# z=Node(30)
# x.next=y
# y.next=z
# z.next=x
# print(x)
# print(y)
# print(z)
# print(x.next)
# print(y.next)
# print(z.next)
#
# temp=x
# while(True):
#     print(temp.data,end=' ')
#     temp=temp.next
#     if(temp==x):
#         break

######Insertion in circular linked list####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class CircularLinkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             self.tail.next=self.head
#             return
#         self.tail.next=newNode
#         self.tail=newNode
#         self.tail.next=self.head
#
#     def insertAtBeg(self,data):
#         newNode=Node(data)
#         if (self.head is None):
#             self.head = newNode
#             self.tail = newNode
#             self.tail.next = self.head
#             return
#         newNode.next=self.head
#         self.head=newNode
#         self.tail.next=self.head
#     def printLL(self):
#         temp=self.head
#         while(True):
#             print(temp,end=' ')
#             print(temp.data,end=' ')
#             print(temp.next)
#             temp=temp.next
#             if(temp==self.head):
#                 break
#         print()
# def main():
#     circularLinkedlist=CircularLinkedlist()
#     circularLinkedlist2=CircularLinkedlist()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         circularLinkedlist.insertAtEnd(arr[i])
#         circularLinkedlist2.insertAtBeg(arr[i])
#     circularLinkedlist.printLL()
#     print()
#     circularLinkedlist2.printLL()
#
#
# if __name__ == '__main__':
#     main()

####Deletion in circular linked list#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class CircularLinkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             self.tail.next=self.head
#             return
#         self.tail.next=newNode
#         self.tail=newNode
#         self.tail.next=self.head
#
#     def deleteAtBeg(self):
#         if(self.head is None):
#             print("Linked list is empty")
#             return
#         if(self.head.next is self.head):
#             self.head=None
#             self.tail=None
#             return
#         self.head=self.head.next
#         self.tail.next=self.head
#     def deleteAtEnd(self):
#         if(self.head is None):
#             print("Linked list is empty")
#             return
#         if(self.head.next is self.head):
#             self.head=None
#             self.tail=None
#             return
#         temp=self.head
#         while(temp.next is not self.tail):
#             temp=temp.next
#         self.tail.next=None
#         self.tail=temp
#         self.tail.next=self.head
#
#     def printLL(self):
#         temp=self.head
#         if(self.head is None):
#             return
#         while(True):
#             print(temp,end=' ')
#             print(temp.data,end=' ')
#             print(temp.next)
#             temp=temp.next
#             if(temp==self.head):
#                 break
#         print()
# def main():
#     circularLinkedlist=CircularLinkedlist()
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         circularLinkedlist.insertAtEnd(arr[i])
#     circularLinkedlist.deleteAtEnd()
#     circularLinkedlist.printLL()
#     circularLinkedlist.deleteAtBeg()
#     circularLinkedlist.printLL()
#
# if __name__ == '__main__':
#     main()

####Left rotate Doubly linked list be N####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class DoublyLinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def rotateNnode(self,N):
#         temp=self.head
#         count=0
#         while(temp is not None and count is not N-1):
#             temp=temp.next
#             count+=1
#         temp2=temp.next
#         if(temp2 is None):
#             return
#         temp.next=None
#         temp2.prev=None
#         self.tail.next=self.head
#         self.head.prev=self.tail
#         self.head=temp2
#         self.tail=temp
#
#
#     def printDoublyLinkedList(self):
#         temp=self.head
#         while (temp is not None):
#             #print(temp.prev, end=' ')
#             print(temp.data, end=' ')
#             #print(temp,end=' ')
#             #print(temp.next)
#             temp = temp.next
#         print()
#
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             return
#         self.tail.next=newNode
#         newNode.prev=self.tail
#         self.tail=newNode
#
#     def lengthofLinkedList(self):
#         temp=self.head
#         count=0
#         while(temp is not None):
#             count+=1
#             temp=temp.next
#         return count
# def main():
#     t=int(input())
#     while(t>0):
#         doublyLinkedList=DoublyLinkedList()
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         for i in range(len(arr)):
#             doublyLinkedList.insertAtEnd(arr[i])
#         doublyLinkedList.rotateNnode(k)
#         doublyLinkedList.printDoublyLinkedList()
#         t=t-1
#
# if __name__ == '__main__':
#     main()


###Add one to list#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def insertAtEnd(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#         else:
#             temp=self.head
#             while(temp.next is not None):
#                 temp=temp.next
#             temp.next=newNode
#     def printSinglyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=' ')
#             #print(temp,end=' ')
#             #print(temp.next)
#             temp=temp.next
#         print()
#     def reverseList(self):
#
#     def addOneToList(self,n):
#         temp=self.head
#         count=0
#         while(temp is not None and count is not n-1):
#             temp=temp.next
#             count+=1
#         temp.data+=1
#         k=temp.data
#         if(k>9):
#
#
# def main():
#     SinglyLinkedList= LinkedList()
#     n=int(input())
#     arr=list(map(int,input().split()))
#     for i in range(len(arr)):
#         SinglyLinkedList.insertAtEnd(arr[i])
#     SinglyLinkedList.printSinglyLinkedList()
#     SinglyLinkedList.addOneToList(n)
#     SinglyLinkedList.printSinglyLinkedList()
# if __name__ == '__main__':
#     main()

######Rotate Doubly List#########


