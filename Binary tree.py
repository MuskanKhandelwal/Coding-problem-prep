# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def main():
#     b1=Node(1)
#     b2=Node(2)
#     b3=Node(3)
#     b1.left=b2
#     b1.right=b3
#     print(b1,b1.left,b1.right)
#     print(b2)
#     print(b3)
# if __name__ == '__main__':
#     main()

####Tree traversal#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def preOrderTraversal(root):
#     if(root is None):
#         return
#     print(root.data, end=" ")
#     preOrderTraversal(root.left)
#     preOrderTraversal(root.right)
# def inOrderTraversal(root):
#     if (root is None):
#         return
#     inOrderTraversal(root.left)
#     print(root.data,end=" ")
#     inOrderTraversal(root.right)
# def postOrderTraversal(root):
#     if (root is None):
#         return
#     postOrderTraversal(root.left)
#     postOrderTraversal(root.right)
#     print(root.data,end=" ")
#
# def main():
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.left.left=Node(4)
#     root.left.right=Node(5)
#     root.right.left=Node(6)
#     root.left.left.left=Node(7)
#     root.left.left.right=Node(8)
#
#     preOrderTraversal(root)
#     print()
#     postOrderTraversal(root)
#     print()
#     inOrderTraversal(root)
#     print()
#
# if __name__ == '__main__':
#     main()

####Height of a tree###
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def preOrderTraversal(root):
#     if(root is None):
#         return
#     print(root.data, end=" ")
#     preOrderTraversal(root.left)
#     preOrderTraversal(root.right)
# def inOrderTraversal(root):
#     if (root is None):
#         return
#     inOrderTraversal(root.left)
#     print(root.data,end=" ")
#     inOrderTraversal(root.right)
# def postOrderTraversal(root):
#     if (root is None):
#         return
#     postOrderTraversal(root.left)
#     postOrderTraversal(root.right)
#     print(root.data,end=" ")
# def heightOfBT(root):
#     if(root is None):
#         return -1
#     lside=heightOfBT(root.left)
#     rside=heightOfBT(root.right)
#     if(lside>rside):
#         return lside+1
#     else:
#         return rside+1
# def main():
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.left.left=Node(4)
#     root.left.right=Node(5)
#     root.right.left=Node(6)
#     root.left.left.left=Node(7)
#     root.left.left.right=Node(8)
#     root.left.left.right.left=Node(9)
#     print(heightOfBT(root))
#
# if __name__ == '__main__':
#     main()

####Size of a Tree####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def preOrderTraversal(root):
#     if(root is None):
#         return
#     print(root.data, end=" ")
#     preOrderTraversal(root.left)
#     preOrderTraversal(root.right)
# def SizeOfBT(root):
#     if(root is None):
#         return 0
#     return SizeOfBT(root.left)+SizeOfBT(root.right)+1
#     # lside=SizeOfBT(root.left)
#     # rside=SizeOfBT(root.right)
#     # return lside+rside+1
# def main():
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.left.left=Node(4)
#     root.left.right=Node(5)
#     root.right.left=Node(6)
#     root.left.left.left=Node(7)
#     root.left.left.right=Node(8)
#     root.left.left.right.left=Node(9)
#     root.left.left.right.left.left=Node(10)
#     print(SizeOfBT(root))
#
# if __name__ == '__main__':
#     main()

####Level Order Traversal#####
# class QueueUsingList:
#     def __init__(self):
#         self.que=[]
#         self.size=0
#         self.front=0
#     def enqueue(self,data):
#         self.que.append(data)
#         self.size+=1
#     def isEmpty(self):
#         return self.size==0
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("Queue is empty")
#             return
#         temp=self.que[self.front]
#         self.front+=1
#         self.size-=1
#         return temp
#     def frontele(self):
#         if (self.isEmpty()):
#             print("Queue is empty")
#             return
#         return self.que[self.front]
#     def printQueue(self):
#         if (self.isEmpty()):
#             print("Queue is empty")
#             return
#         for i in range(self.size):
#             print(self.que[self.front + i],end=" ")
#         print()
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def preOrderTraversal(root):
#     if(root is None):
#         return
#     print(root.data, end=" ")
#     preOrderTraversal(root.left)
#     preOrderTraversal(root.right)
# def levelOrderTraversal(root):
#     if(root is None):
#         return
#     queue=QueueUsingList()
#     queue.enqueue(root)
#     while(queue.size>0):
#         temp=queue.dequeue()
#         print(temp.data, end=" ")
#
#         if(temp.left is not None):
#             queue.enqueue(temp.left)
#         if(temp.right is not None):
#             queue.enqueue(temp.right)
# def main():
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.left.left=Node(4)
#     root.left.right=Node(5)
#     root.right.left=Node(6)
#     root.left.left.left=Node(7)
#     root.left.left.right=Node(8)
#     root.left.left.right.left=Node(9)
#     root.left.left.right.left.left=Node(10)
#     levelOrderTraversal(root)
#
# if __name__ == '__main__':
#     main()

####Min and max in Binary Tree#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
# def preOrderTraversal(root):
#     if(root is None):
#         return
#     print(root.data,end=" ")
#     preOrderTraversal(root.left)
#     preOrderTraversal(root.right)
# def minValue(root):
#     if(root is None):
#         return 1000000000000
#     res=root.data
#     lside=minValue(root.left)
#     rside=minValue(root.right)
#     if(lside<res):
#         res=lside
#     if(rside<res):
#         res=rside
#     return res
# def maxValue(root):
#     if(root is None):
#         return -100
#     res=root.data
#     lside=maxValue(root.left)
#     rside=maxValue(root.right)
#     if(lside>res):
#         res=lside
#     if(rside>res):
#         res=rside
#     return res
#
# def main():
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.left.left=Node(4)
#     root.left.right=Node(5)
#     root.right.left=Node(6)
#     root.left.left.left=Node(7)
#     root.left.left.right=Node(8)
#     root.left.left.right.left=Node(9)
#     root.left.left.right.left.left=Node(10)
#     print(minValue(root))
#     print(maxValue(root))
#
# if __name__ == '__main__':
#     main()

#####Balanced Binary Tree######
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
# def preOrderTraversal(root):
#     if(root is None):
#         return
#     print(root.data,end=" ")
#     preOrderTraversal(root.left)
#     preOrderTraversal(root.right)
# def heightOfBT(root):
#     if(root is None):
#         return -1
#     lside=heightOfBT(root.left)
#     rside=heightOfBT(root.right)
#     if(lside>rside):
#         return lside+1
#     else:
#         return rside+1
# def isBalanced(root):
#     if(root is None):
#         return True
#     lh=heightOfBT(root.left)
#     rh=heightOfBT(root.right)
#     if(lh-rh>1 or rh-lh>1):
#         return False
#     lside=isBalanced(root.left)
#     rside=isBalanced(root.right)
#     if(lside and rside):
#         return True
#     else:
#         return False
#
#
# def main():
#     root=Node(1)
#     root.left=Node(2)
#     root.right=Node(3)
#     root.left.left=Node(4)
#     root.left.right=Node(5)
#     root.right.left=Node(6)
#     root.left.left.left=Node(7)
#     root.left.left.right=Node(8)
#     root.left.left.right.left=Node(9)
#     root.left.left.right.left.left=Node(10)
#     print(isBalanced(root))
#
# if __name__ == '__main__':
#     main()

####Build Tree using level order traversal####
# from queue import Queue
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def inOrderTraversal(root):
#     if (root is None):
#         return
#     inOrderTraversal(root.left)
#     print(root.data,end=" ")
#     inOrderTraversal(root.right)
#
# def buildTreeLevelWise(ip):
#     if(len(ip)==0 or ip[0]==-1):
#         return None
#     root=Node(ip[0])
#     qu=Queue()
#     qu.put(root)
#     i=1
#     while(qu.empty() is False and i<len(ip)):
#         currNode=qu.get()
#         currVal=ip[i]
#         if(currVal !='-1'):
#             currNode.left=Node(currVal)
#             qu.put(currNode.left)
#         i=i+1
#         if(i>=len(ip)):
#             break
#         currVal=ip[i]
#         if(currVal !='-1'):
#             currNode.right=Node(currVal)
#             qu.put(currNode.right)
#         i+=1
#     return root
# def main():
#     ip=list(input().split())
#     root=buildTreeLevelWise(ip)
#     inOrderTraversal(root)
# if __name__ == '__main__':
#     main()

####Build tree using Inorder and PosstOrder#####
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BuildTree:
    def __init__(self):
        self.pI=0
    def btUsingIP(self,inOrder,preOrder,st,end):
        if(st>end):
            return None

        treeNode=Node(preOrder[self.pI])
        self.pI+=1
        inInd=self.search(inOrder,st,end,treeNode.data)
        if(st==end):
            return treeNode
        treeNode.left=self.btUsingIP(inOrder,preOrder,st,inInd-1)
        treeNode.right=self.btUsingIP(inOrder,preOrder,inInd+1,end)
        return treeNode
    def search(self,arr,st,end,val):
        for i in range(st,end+1):
            if(arr[i]==val):
                return i
    def preOrder(self,root):
        if(root is not None):
            print(root.data,end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

def main():
    inOrder=list(input().split())
    preOrder=list(input().split())
    bt=BuildTree()
    root=bt.btUsingIP(inOrder,preOrder,0,len(inOrder)-1)
    bt.preOrder(root)
if __name__ == '__main__':
    main()



