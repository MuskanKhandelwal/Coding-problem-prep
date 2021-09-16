####Bottom up approach####
# def parent(i):
#     return (i-1)//2
#
# def left(i):
#     return (2*i)+1
#
# def right(i):
#     return (2*i)+2
#
# def build_heap(heap,n):
#     for i in range((n//2)-1,-1,-1):
#         heapify_down(heap,n,i)
#
# def heapify_down(heap,n,i):
#     s=i
#     l=left(i)
#     r=right(i)
#     if(l<n and heap[l]<heap[s]):
#         s=l
#     if(r<n and heap[r]<heap[s]):
#         s=r
#     if(s!=i):
#         heap[i],heap[s]=heap[s],heap[i]
#         heapify_down(heap,n,s)
# def print_heap(heap,n):
#     for i in range(n):
#         print(heap[i],end=" ")
#     print()
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         build_heap(arr,n)
#         print_heap(arr,n)
#         t=t-1
# if __name__ == '__main__':
#     main()

###Top down approach######
# def parent(i):
#     return (i-1)//2
# def left(i):
#     return (2*i)+1
#
# def right(i):
#     return (2*i)+2
#
# def heapify_up(heap,i):
#     while(i!=0 and heap[parent(i)]>heap[i]):
#         heap[parent(i)],heap[i]=heap[i],heap[parent(i)]
#         i=parent(i)
#
# def insert(heap,i,ele):
#     heap[i]=ele
#     heapify_up(heap,i)
# def print_heap(heap,n):
#     for i in range(n):
#         print(heap[i],end=" ")
#     print()
#
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         heap=[None]*n
#         i=0
#         for ele in input().split():
#             insert(heap,i,int(ele))
#             i=i+1
#         print_heap(heap,n)
#         t=t-1
# if __name__ == '__main__':
#     main()

####Heap sort#####
# def parent(i):
#     return (i-1)//2
# def left(i):
#     return (2*i)+1
#
# def right(i):
#     return (2*i)+2
#
# def heapify_down(heap,n,i):
#     s=i
#     l=left(i)
#     r=right(i)
#     if(l<n and heap[l]<heap[s]):
#         s=l
#     if(r<n and heap[r]<heap[s]):
#         s=r
#     if(s!=i):
#         heap[i],heap[s]=heap[s],heap[i]
#         heapify_down(heap,n,s)
#
#
# def build_heap(heap,n):
#     for i in range((n//2)-1,-1,-1):
#         heapify_down(heap,n,i)

# def print_heap(heap,n):
#     for i in range(n-1,-1,-1):
#         print(heap[i],end=" ")
#     print()
#
# def heap_sort(heap,n):
#     build_heap(heap,n)
#     for i in range(n-1,-1,-1):
#         heap[0],heap[i]=heap[i],heap[0]
#         heapify_down(heap,i,0)
#
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         heap_sort(arr,n)
#         print_heap(arr,n)
#         t=t-1
# if __name__ == '__main__':
#     main()

####Heap operations####
# def parent(i):
#     return (i-1)//2
# def left(i):
#     return (2*i)+1
#
# def right(i):
#     return (2*i)+2
#
# def heapify_up(heap,i):
#     while(i!=0 and heap[parent(i)]>heap[i]):
#         heap[parent(i)],heap[i]=heap[i],heap[parent(i)]
#         i=parent(i)
#
# def insert(heap,i,ele):
#     heap[i]=ele
#     heapify_up(heap,i)
#
# def heapify_down(heap,n,i):
#     s=i
#     l=left(i)
#     r=right(i)
#     if(l<n and heap[l]<heap[s]):
#         s=l
#     if(r<n and heap[r]<heap[s]):
#         s=r
#     if(s!=i):
#         heap[i],heap[s]=heap[s],heap[i]
#         heapify_down(heap,n,s)
# def extract_min(heap,size):
#     temp=heap[0]
#     heap[0]=heap[size-1]
#     size-=1
#     heapify_down(heap,size,0)
#     return temp
# def print_heap(heap,n):
#     for i in range(n):
#         print(heap[i],end=" ")
#     print()
#
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         heap=[None]*n
#         i = 0
#         size=0
#         for ele in input().split():
#             size+=1
#             insert(heap,i,int(ele))
#             i+=1
#         #print(heap[0],end =" ")
#         min_ele=extract_min(heap,size)
#         print(min_ele,end=" ")
#         print_heap(heap,n)
#         t=t-1
# if __name__ == '__main__':
#     main()

####Extract min and decrease key####
# class HeapImplementation:
#     def __init__(self,n):
#         self.size=n
#
#     def parent(self,i):
#         return (i-1)//2
#
#     def left(self,i):
#         return 2*i +1
#
#     def right(self,i):
#         return 2*i +2
#
#     def heapify_down(self,heap,n,i):
#         l=self.left(i)
#         r=self.right(i)
#         s=i
#         if(l<n and heap[l]<heap[s]):
#             s=l
#         if (r < n and heap[r] < heap[s]):
#             s=r
#         if(s!=i):
#             heap[i],heap[s]=heap[s],heap[i]
#             self.heapify_down(heap,n,s)
#
#     def build_heap(self,heap):
#         for i in range(self.size//2 -1,-1,-1):
#             self.heapify_down(heap,self.size,i)
#
#     def extract_heap(self,heap):
#         temp=heap[0]
#         #swap last and first element
#         heap[0],heap[self.size-1]=heap[self.size-1],heap[0]
#         self.size=self.size-1
#         self.heapify_down(heap,self.size,0)
#         return temp
#
#     def decrease_key(self,heap,index,val):
#         heap[index]=val
#         self.heapify_up(heap,index)
#
#     def heapify_up(self,heap,i):
#         while(i!=0 and heap[self.parent(i)]>heap[i]):
#             heap[i],heap[self.parent(i)]=heap[self.parent(i)],heap[i]
#             i=self.parent(i)
#     def print_heap(self,heap):
#         for i in range(self.size):
#             print(heap[i],end=" ")
#         print()
#
# def main():
#     t=int(input())
#     while(t>0):
#         n=int(input())
#         arr=list(map(int,input().split()))
#         heap=HeapImplementation(n)
#         heap.build_heap(arr)
#         heap.print_heap(arr)
#         print(heap.extract_heap(arr))
#         k=int(input())
#         heap.decrease_key(arr,k,-1)
#         heap.print_heap(arr)
#         t=t-1
# if __name__ == '__main__':
#     main()

###Heap decrease####
# class HeapImplementation:
#     def __init__(self,n):
#         self.size=n
#
#     def parent(self,i):
#         return (i-1)//2
#
#     def left(self,i):
#         return 2*i +1
#
#     def right(self,i):
#         return 2*i +2
#
#     def heapify_down(self,heap,n,i):
#         l=self.left(i)
#         r=self.right(i)
#         s=i
#         if(l<n and heap[l]<heap[s]):
#             s=l
#         if (r < n and heap[r] < heap[s]):
#             s=r
#         if(s!=i):
#             heap[i],heap[s]=heap[s],heap[i]
#             self.heapify_down(heap,n,s)
#
#     def build_heap(self,heap):
#         for i in range(self.size//2 -1,-1,-1):
#             self.heapify_down(heap,self.size,i)
#
#     def extract_heap(self,heap):
#         temp=heap[0]
#         #swap last and first element
#         heap[0],heap[self.size-1]=heap[self.size-1],heap[0]
#         self.size=self.size-1
#         self.heapify_down(heap,self.size,0)
#         return temp
#
#     def decrease_key(self,heap,index,val):
#         heap[index]=val
#         self.heapify_up(heap,index)
#         self.extract_heap(heap)
#
#     def heapify_up(self,heap,i):
#         while(i!=0 and heap[self.parent(i)]>heap[i]):
#             heap[i],heap[self.parent(i)]=heap[self.parent(i)],heap[i]
#             i=self.parent(i)
#     def print_heap(self,heap):
#         for i in range(self.size):
#             print(heap[i],end=" ")
#         print()
#
# def main():
#     t=int(input())
#     while(t>0):
#         n,k=map(int,(input().split()))
#         arr=list(map(int,input().split()))
#         heap=HeapImplementation(n)
#         heap.build_heap(arr)
#         heap.print_heap(arr)
#         #print(heap.extract_heap(arr))
#         #k=int(input())
#         heap.decrease_key(arr,k-1,-1)
#         #heap.extract_heap(arr)
#         heap.print_heap(arr)
#         t=t-1
# if __name__ == '__main__':
#     main()

###HeapQ min heap###
# import heapq
# def print_heap(heap):
#     for i in range(len(heap)):
#         print(heap[i],end=" ")
#     print()
# def main():
#     arr=list(map(int,input().split()))
#     heapq.heapify(arr)
#     print_heap(arr)
#
#     heapq.heappush(arr,100)
#     print_heap(arr)
#
#     print(heapq.heappop(arr))
#     print_heap(arr)
#
#     heapq.heapreplace(arr,200)
#     print_heap(arr)
#
# if __name__ == '__main__':
#     main()

###HeapQ max heap##
# import heapq
# def print_heap(heap):
#     for i in range(len(heap)):
#         print(heap[i],end=" ")
#     print()
# def main():
#     arr=list(map(int,input().split()))
#     heapq._heapify_max(arr)
#     print_heap(arr)
#
#     print(heapq._heappop_max(arr))
#     print_heap(arr)
#
#     heapq._heapreplace_max(arr,-1)
#     print_heap(arr)
#
#     arr.append(1000)
#     heapq._siftdown_max(arr,0,len(arr)-1)
#     print_heap(arr)
#
# if __name__ == '__main__':
#     main()

###Small String###
# import heapq
# def main():
#     t=int(input())
#     while(t>0):
#         str,q=input().split()
#         q=int(q)
#         arr=[]
#         for i in range(q): #0 to q-1
#             arr.append(str[i])
#         heapq.heapify(arr)
#         i=q
#         final=""
#         while(len(arr)!=0):
#             final+=heapq.heappop(arr)
#             if(i<len(str)):
#                 arr.append(str[i])
#             heapq.heapify(arr)
#             i+=1
#         print(final)
#         t=t-1
# if __name__ == '__main__':
#     main()

###K largest elements####
# import heapq
# def main():
#     t=int(input())
#     while(t!=0):
#         n,k=map(int,input().split())
#         arr=list(map(int,input().split()))
#         heapq._heapify_max(arr)
#         while(k!=0):
#             print(heapq._heappop_max(arr),end=" ")
#             k=k-1
#         print()
#         t=t-1
# if __name__ == '__main__':
#     main()

###Binary tree is max heap or not ###
###Queue using List####
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
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#
# def preOrderTraversal(root):
#     if(root is None):
#         return
#     print(root.data,end=" ")
#     preOrderTraversal(root.left)
#     preOrderTraversal(root.right)
#
# def isCompleteBT(root):
#     if(root is None):
#         return None
#     queue=QueueUsingList()
#     queue.enqueue(root)
#     flag=False
#     while(queue.size>0):
#         temp=queue.dequeue()
#         if(temp.left is not None):
#             if(flag is True):
#                 return False
#             queue.enqueue(temp.left)
#         else:
#             flag=True
#         if(temp.right is not None):
#             if(flag is True):
#                 return False
#             queue.enqueue(temp.right)
#         else:
#             flag=True
#     return True
# def main():
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.left.left=Node(4)
#     root.left.right=Node(5)
#     root.right.left=Node(6)
#     root.right.right=Node(7)
#     root.left.left.left=Node(8)
#     #root.left.left.left.right= Node(9)
#     if(isCompleteBT(root)):
#         print("Tree is complete binary tree")
#     else:
#         print("Not a complete Binary tree")
# if __name__ == '__main__':
#     main()

####Maximum Books####
# class HeapImplementation:
#     def __init__(self,n):
#         self.size=n
#
#     def parent(self,i):
#         return (i-1)//2
#
#     def left(self,i):
#         return 2*i +1
#
#     def right(self,i):
#         return 2*i +2
#
#     def heapify_down(self,heap,n,i):
#         l=self.left(i)
#         r=self.right(i)
#         s=i
#         if(l<n and heap[l]<heap[s]):
#             s=l
#         if (r < n and heap[r] < heap[s]):
#             s=r
#         if(s!=i):
#             heap[i],heap[s]=heap[s],heap[i]
#             self.heapify_down(heap,n,s)
#
#     def build_heap(self,heap):
#         for i in range(self.size//2 -1,-1,-1):
#             self.heapify_down(heap,self.size,i)
#
#     def extract_heap(self,heap):
#         temp=heap[0]
#         #swap last and first element
#         heap[0],heap[self.size-1]=heap[self.size-1],heap[0]
#         self.size=self.size-1
#         self.heapify_down(heap,self.size,0)
#         return temp
#
#     def decrease_key(self,heap,index,val):
#         heap[index]=val
#         self.heapify_up(heap,index)
#
#     def heapify_up(self,heap,i):
#         while(i!=0 and heap[self.parent(i)]>heap[i]):
#             heap[i],heap[self.parent(i)]=heap[self.parent(i)],heap[i]
#             i=self.parent(i)
#     def print_heap(self,heap):
#         for i in range(self.size):
#             print(heap[i],end=" ")
#         print()
#
# def main():
#     t=int(input())
#     while(t>0):
#         n,k=map(int,(input().split()))
#         arr=list(map(int,input().split()))
#         heap=HeapImplementation(n)
#         heap.build_heap(arr)
#         #heap.print_heap(arr)
#         temp=0
#         count=0
#         while(k-temp>0):
#             temp+=heap.extract_heap(arr)
#             #print(temp)
#             count+=1
#         #heap.decrease_key(arr,k,-1)
#         #heap.print_heap(arr)
#         print(count-1)
#         t=t-1
# if __name__ == '__main__':
#     main()

####Fascinating Multiple Number###
class HeapImplementation:
    def __init__(self,n):
        self.size=n

    def parent(self,i):
        return (i-1)//2

    def left(self,i):
        return 2*i +1

    def right(self,i):
        return 2*i +2

    def heapify_down(self,heap,n,i):
        l=self.left(i)
        r=self.right(i)
        s=i
        if(l<n and heap[l]>heap[s]):
            s=l
        if (r < n and heap[r] > heap[s]):
            s=r
        if(s!=i):
            heap[i],heap[s]=heap[s],heap[i]
            self.heapify_down(heap,n,s)

    def build_heap(self,heap):
        for i in range(self.size//2 -1,-1,-1):
            self.heapify_down(heap,self.size,i)

    def extract_heap(self,heap):
        temp=heap[0]
        #swap last and first element
        heap[0],heap[self.size-1]=heap[self.size-1],heap[0]
        self.size=self.size-1
        self.heapify_down(heap,self.size,0)
        return temp

    def print_heap(self,heap):
        for i in range(self.size):
            print(heap[i],end=" ")
        print()

    def heapify_up(self,heap, i):
        while (i != 0 and heap[self.parent(i)] < heap[i]):
            heap[self.parent(i)], heap[i] = heap[i], heap[self.parent(i)]
            i = self.parent(i)

    def insert(self,heap, i, ele):
        heap[i] = ele
        self.heapify_up(heap, i)
        self.size+=1


def main():
    t=int(input())
    while(t>0):
        n=int(input())
        arr=list(map(int,input().split()))
        heap=HeapImplementation(n)
        heap.build_heap(arr)
        size=len(arr)
        while(size>0):
            p=heap.extract_heap(arr)
            size-=1
            heap.build_heap(arr)
            q=heap.extract_heap(arr)
            size-=1
            heap.build_heap(arr)
            new=(p*3)%(pow(10,9)+7)-(q*2)%(pow(10,9)+7)
            heap.insert(arr,size,new)
            size+=1
        print(new)
        t=t-1
if __name__ == '__main__':
    main()

#####Maximum sub array#####
# def main():
#     n,s=map(int,input().split())
#     arr=list(map(int,input().split()))

