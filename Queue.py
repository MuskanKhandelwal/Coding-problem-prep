######Queue Implementation using circular array#####
# class QueueUsingCircularArray:
#     def __init__(self,capacity):
#         self.que=[None]*capacity
#         self.front=-1
#         self.rear=-1
#         self.size=0
#         self.cap=capacity
#     def isEmpty(self):
#         return self.front==-1
#     def enqueue(self,data):
#         #Queue Full
#         if((self.rear+1)%self.cap==self.front):
#             print("queue is full")
#             return
#         #Currently no element is present
#         if(self.isEmpty()):
#             self.front=self.rear=0
#             self.que[self.rear]=data
#             self.size+=1
#             return
#         self.rear=(self.rear+1)%self.cap
#         self.que[self.rear]=data
#         self.size+=1
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("Queue is empty")
#             return -1
#         #one element in the queue
#         if(self.rear==self.front):
#             temp=self.que[self.front]
#             self.front=self.rear==1
#             self.size -= 1
#             return temp
#         temp=self.que[self.front]
#         self.front=(self.front+1)%self.cap
#         self.size-=1
#         return temp
#     def frontele(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         return self.que[self.front]
#     def printQueue(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         for i in range(self.size):
#             print(self.que[(self.front+i)%self.cap],end=" ")
#         print()
#
# def main():
#     cap=int(input())
#     que=QueueUsingCircularArray(cap)
#     for ele in input().split():
#         que.enqueue(int(ele))
#     que.printQueue()
#     que.dequeue()
#     que.printQueue()
#     que.dequeue()
#     que.printQueue()
#     que.dequeue()
#     que.enqueue(100)
#     que.enqueue(200)
#     que.printQueue()
#
# if __name__ == '__main__':
#     main()

# ###Queue using List####
# class QueueUsingList:
#     def __init__(self):
#         self.que=[]
#         self.front=0
#         self.size=0
#     def isEmpty(self):
#         return self.size==0
#     def enqueue(self,data):
#         self.que.append(data)
#         self.size+=1
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("queue is empty")
#             return
#         temp=self.que[self.front]
#         self.front+=1
#         self.size-=1
#         return temp
#
#     def frontele(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         return self.que[self.front]
#     def printQueue(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         for i in range(self.size):
#             print(self.que[self.front+i],end=" ")
#         print()
#
# def main():
#     que=QueueUsingList()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     que.printQueue()
#     n=3
#     while(n>0):
#         print(que.frontele())
#         que.dequeue()
#         n=n-1
#     que.enqueue(100)
#     que.printQueue()
#     que.enqueue(101)
#     que.printQueue()
#     que.enqueue(102)
#     que.printQueue()
#     que.enqueue(103)
#     que.printQueue()
#
# if __name__ == '__main__':
#     main()

####Queue using linked list####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class QueueUsingLinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.size=0
#     def isEmpty(self):
#         return self.size==0
#     def enqueue(self,data):
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=self.tail=newNode
#             self.size+=1
#             return
#         self.tail.next=newNode
#         self.tail=newNode
#         self.size+=1
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("queue is empty")
#             return
#         #Only one single element
#         if(self.size==1):
#             temp=self.head.data
#             self.head=self.tail=None
#             self.size-=1
#             return temp
#         temp=self.head.data
#         self.head=self.head.next
#         self.size-=1
#         return temp
#     def frontele(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         return self.head.data
#     def printQueue(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         temp=self.head
#         while(temp is not None):
#             print(temp.data,end=" ")
#             temp=temp.next
#         print()
#
# def main():
#     que=QueueUsingLinkedList()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     que.printQueue()
#     n=3
#     while(n>0):
#         print(que.frontele())
#         que.dequeue()
#         n=n-1
#     que.enqueue(100)
#     que.printQueue()
#     que.enqueue(101)
#     que.printQueue()
#     que.enqueue(102)
#     que.printQueue()
#     que.enqueue(103)
#     que.printQueue()
#
# if __name__ == '__main__':
#     main()


######Reverse queue using stack######
# class QueueUsingList:
#     def __init__(self):
#         self.que=[]
#         self.front=0
#         self.size=0
#     def isEmpty(self):
#         return self.size==0
#     def enqueue(self,data):
#         self.que.append(data)
#         self.size+=1
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("queue is empty")
#             return
#         temp=self.que[self.front]
#         self.front+=1
#         self.size-=1
#         return temp
#     def frontele(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         return self.que[self.front]
#     def printQueue(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         for i in range(self.size):
#             print(self.que[self.front +i],end=" ")
#         print()
# class stack:
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
#         self.tos=self.tos-1
#         self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         return self.arr[self.tos]
#
# def main():
#     que=QueueUsingList()
#     st=stack()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     while(que.isEmpty() is False):
#         st.push(que.dequeue())
#     while(st.isEmpty() is False):
#         que.enqueue(st.top())
#         st.pop()
#     que.printQueue()
#
# if __name__ == '__main__':
#     main()

#####Reverse queue using recursion####
# class QueueUsingList:
#     def __init__(self):
#         self.que=[]
#         self.front=0
#         self.size=0
#     def isEmpty(self):
#         return self.size==0
#     def enqueue(self,data):
#         self.que.append(data)
#         self.size+=1
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("queue is empty")
#             return
#         temp=self.que[self.front]
#         self.front+=1
#         self.size-=1
#         return temp
#     def frontele(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         return self.que[self.front]
#     def printQueue(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         for i in range(self.size):
#             print(self.que[self.front +i],end=" ")
#         print()
# def reverse(que):
#     if(que.isEmpty()):
#         return
#     temp=que.dequeue()
#     reverse(que)
#     que.enqueue(temp)
#
# def main():
#     que=QueueUsingList()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     reverse(que)
#     que.printQueue()
#
# if __name__ == '__main__':
#     main()

#####Reverse first K elements####
# class QueueUsingList:
#     def __init__(self):
#         self.que=[]
#         self.front=0
#         self.size=0
#     def isEmpty(self):
#         return self.size==0
#     def enqueue(self,data):
#         self.que.append(data)
#         self.size+=1
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("queue is empty")
#             return
#         temp=self.que[self.front]
#         self.front+=1
#         self.size-=1
#         return temp
#     def frontele(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         return self.que[self.front]
#     def printQueue(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         for i in range(self.size):
#             print(self.que[self.front +i],end=" ")
#         print()
# class stack:
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
#         self.tos=self.tos-1
#         self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         return self.arr[self.tos]
#
# def reverseFirstKele(que,st,k):
#     if(que.isEmpty() or k>que.size or k<=0):
#         return
#     for i in range(k):
#         st.push(que.dequeue())
#     while(st.isEmpty() is False):
#         que.enqueue(st.top())
#         st.pop()
#     for i in range(que.size-k):
#         que.enqueue(que.dequeue())
#
# def main():
#     que=QueueUsingList()
#     st=stack()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     k=int(input())
#     reverseFirstKele(que,st,k)
#     que.printQueue()
#
# if __name__ == '__main__':
#     main()

###Stone Number#####
# class QueueUsingList:
#     def __init__(self):
#         self.que=[]
#         self.front=0
#         self.size=0
#     def isEmpty(self):
#         return self.size==0
#     def enqueue(self,data):
#         self.que.append(data)
#         self.size+=1
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("queue is empty")
#             return
#         temp=self.que[self.front]
#         self.front+=1
#         self.size-=1
#         return temp
#
#     def frontele(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         return self.que[self.front]
#     def printQueue(self):
#         if(self.isEmpty()):
#             print("Queue is empty ")
#             return
#         for i in range(self.size):
#             print(self.que[self.front+i],end=" ")
#         print()
# class stack:
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
#         self.tos=self.tos-1
#         self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         return self.arr[self.tos]
#
# def main():
#     T=int(input())
#     while(T>0):
#         n=int(input())
#         que = QueueUsingList()
#         st=stack()
#         for ele in range(1,n+1):
#             que.enqueue(ele)
#         que.printQueue()
#         while (n > 0):
#             temp=que.dequeue()
#
#             n = n - 1
#         T=T-1
#     que=QueueUsingList()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     que.printQueue()
#     n=3
#     while(n>0):
#         print(que.frontele())
#         que.dequeue()
#         n=n-1
# if __name__ == '__main__':
#     main()

######Queue using stack #####
# class stack:
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
#         self.tos=self.tos-1
#         self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         return self.arr[self.tos]
# class queueUsingStack:
#     def __init__(self):
#         self.s1=stack()
#         self.s2=stack()
#         self.size=0
#     def enqueue(self,data):
#         while(self.s1.isEmpty() is False):
#             self.s2.push(self.s1.top())
#             self.s1.pop()
#         self.s1.push(data)
#         self.size+=1
#         while(self.s2.isEmpty() is False):
#             self.s1.push(self.s2.top())
#             self.s2.pop()
#     def dequeue(self):
#         if(self.s1.isEmpty()):
#             print("Queue Underflow")
#             return
#         data=self.s1.top()
#         self.s1.pop()
#         self.size-=1
#         return data
#
#     def isEmpty(self):
#         return self.size==0
# def main():
#     que=queueUsingStack()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     while(que.isEmpty() is False):
#         print(que.dequeue(),end=" ")
# if __name__ == '__main__':
#     main()

#####Queue using stacj M2#####
# class stack:
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
#         self.tos=self.tos-1
#         self.arr.pop()
#     def size(self):
#         return self.tos+1
#     def isEmpty(self):
#         return self.tos==-1
#     def top(self):
#         if(self.isEmpty()):
#             print("Stack is empty")
#             return
#         return self.arr[self.tos]
# class queueUsingStack:
#     def __init__(self):
#         self.s1=stack()
#         self.s2=stack()
#         self.size=0
#     def enqueue(self,data):
#         self.s1.push(data)
#         self.size+=1
#     def dequeue(self):
#         if(self.s1.isEmpty() and self.s2.isEmpty()):
#             print("Queue Underflow")
#             return
#         if(self.s2.isEmpty()):
#             while(self.s1.isEmpty() is False):
#                 self.s2.push(self.s1.top())
#                 self.s1.pop()
#         data=self.s2.top()
#         self.s2.pop()
#         self.size-=1
#         return data
#
#     def isEmpty(self):
#         return self.size==0
# def main():
#     que=queueUsingStack()
#     for ele in input().split():
#         que.enqueue(int(ele))
#     while(que.isEmpty() is False):
#         print(que.dequeue(),end=" ")
# if __name__ == '__main__':
#     main()

####inbuilt queue###
# from queue import Queue
# from queue import LifoQueue
# q=Queue(maxsize=10)
# q.put(20)
# q.put(2)
# q.put(120)
# q.put(200)
# q.put(30)
# q.put(3)
# q.put(220)
# q.put(14)
# q.put(17)
# q.put(201)
# print(q.empty())
# print(q.full())
# print(q.qsize())
# #q.put_nowait(200)
# while(q.empty() is False):
#     print(q.get())
#
# #print(q.get_nowait())
# q1=LifoQueue()
# q1.put(20)
# q1.put(2)
# q1.put(120)
# q1.put(200)
# q1.put(30)
# while(q1.empty() is False):
#     print(q1.get())

####Deque#####
# class Deque():
#     def __init__(self):
#         self._dq=[]
#     def isEmpty(self):
#         return self._dq==[]
#     def insertRear(self,data):
#         self._dq.append(data)
#     def insertFront(self,data):
#         self._dq.insert(0,data)
#     def deleteRear(self):
#         self._dq.pop()
#     def deleteFront(self):
#         self._dq.pop(0)
#     def size(self):
#         return len(self._dq)
#     def frontEle(self):
#         return self._dq[0]
#     def rearEle(self):
#         return self._dq[-1]
#     def printDeque(self):
#         for ele in self._dq:
#             print(ele,end=" ")
#         print()
#
# def main():
#     deque=Deque()
#     deque.insertFront(5)
#     deque.printDeque()
#     deque.insertFront(10)
#     deque.printDeque()
#     deque.insertRear(1)
#     deque.printDeque()
#     deque.insertRear(12)
#     deque.printDeque()
#
#     deque.deleteRear()
#     deque.printDeque()
#     deque.deleteFront()
#     deque.printDeque()
#
#     print(deque.frontEle())
#     print(deque.rearEle())
#     print(deque.size())
#     print(deque.isEmpty())
# if __name__ == '__main__':
#     main()

####Deque using doubly linked list####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class DequeUsingDLL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.size=0
#     def insertAtFront(self,data):
#         self.size+=1
#         newNode=Node(data)
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             return
#         newNode.next=self.head
#         self.head.prev=newNode
#         self.head=newNode
#     def insertAtRear(self,data):
#         newNode=Node(data)
#         self.size += 1
#         if(self.head is None):
#             self.head=newNode
#             self.tail=newNode
#             return
#         self.tail.next=newNode
#         newNode.prev=self.tail
#         self.tail=newNode
#     def deleteAtFront(self):
#         if(self.head is None):
#             return
#         self.size-=1
#         if(self.head.next is None):
#             self.head=None
#             self.tail=None
#             return
#         self.head=self.head.next
#         self.head.prev.next=None
#         self.head.prev=None
#
#     def deleteAtEnd(self):
#         if(self.head is None):
#             return
#         self.size-=1
#         if(self.head.next is None):
#             self.head=None
#             self.tail=None
#             return
#         self.tail=self.tail.prev
#         self.tail.next.prev=None
#         self.tail.next=None
#     def printDoublyLinkedList(self):
#         temp=self.head
#         while(temp is not None):
#             print(temp.data, end=" ")
#             temp=temp.next
#         print()
# def main():
#     dq=DequeUsingDLL()
#     dq.insertAtFront(5)
#     dq.printDoublyLinkedList()
#     dq.insertAtFront(10)
#     dq.printDoublyLinkedList()
#     dq.insertAtRear(1)
#     dq.printDoublyLinkedList()
#     dq.insertAtRear(12)
#     dq.printDoublyLinkedList()
#     dq.deleteAtEnd()
#     dq.printDoublyLinkedList()
#     dq.deleteAtFront()
#     dq.printDoublyLinkedList()
#
#
# if __name__ == '__main__':
#     main()

######Inbuilt deque######
# import collections
# def main():
#     dq=collections.deque()
#     dq.append(5)
#     dq.append(6)
#     print(dq)
#     dq.appendleft(10)
#     print(dq)
#     dq.append(20)
#     print(dq)
#
#     dq.pop()
#     print(dq)
#     dq.popleft()
#     print(dq)
#     dq.appendleft(5)
#     dq.appendleft(100)
#     print(dq)
#     print(dq.index(5,0,3))
#     dq.remove(5)
#     print(dq)
#     print(dq.count(5))
#     dq.extend([1,2,3])
#     dq.extendleft([7,8,9])
#     print(dq)
#
#     dq.reverse()
#     print(dq)
#     dq.rotate(4)
#     print(dq)
#     dq.rotate(-4)
#     print(dq)
# if __name__ == '__main__':
#     main()

####Find Max in window#####
import collections
def main():
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    dq=collections.deque()
    for i in range(k):
        while(dq and arr[i]>=arr[dq[-1]]):
            dq.pop()
        dq.append(i)
    for i in range(k,n):
        print(arr[dq[0]], end =" ")
        if(dq and dq[0]<=i-k):
            dq.popleft()
        while(dq and arr[i]>=arr[dq[-1]]):
            dq.pop()
        dq.append(i)
    print(arr[dq[0]])

if __name__ == '__main__':
    main()