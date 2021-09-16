####Insertion in BST###
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# class BST:
#     def __init__(self):
#         self.root=None
#     def addNode(self,node,data):
#         if(node is None):
#             return Node(data)
#             # newNode=Node(data)
#             # return newNode
#         if(data<node.data):
#             node.left=self.addNode(node.left,data)
#         else:
#             node.right=self.addNode(node.right,data)
#         return node
#     def preOrder(self,node):
#         if(node is None):
#             return
#         print(node.data,end=" ")
#         self.preOrder(node.left)
#         self.preOrder(node.right)
#     def inOrder(self,node):
#         if(node is None):
#             return
#         self.inOrder(node.left)
#         print(node.data, end=" ")
#         self.inOrder(node.right)
# def main():
#     arr=list(map(int,input().split()))
#     bst=BST()
#     for ele in arr:
#         bst.root=bst.addNode(bst.root,ele)
#     bst.preOrder(bst.root)
#     print()
#     bst.inOrder(bst.root)
#
# if __name__ == '__main__':
#     main()


#####Search in BST#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# class BST:
#     def __init__(self):
#         self.root=None
#     def addNode(self,node,data):
#         if(node is None):
#             return Node(data)
#             # newNode=Node(data)
#             # return newNode
#         if(data<node.data):
#             node.left=self.addNode(node.left,data)
#         else:
#             node.right=self.addNode(node.right,data)
#         return node
#     def preOrder(self,node):
#         if(node is None):
#             return
#         print(node.data,end=" ")
#         self.preOrder(node.left)
#         self.preOrder(node.right)
#     def inOrder(self,node):
#         if(node is None):
#             return
#         self.inOrder(node.left)
#         print(node.data, end=" ")
#         self.inOrder(node.right)
#     def search(self,node,data):
#         if(node is None or node.data==data):
#             return node
#         if(data<node.data):
#             return self.search(node.left,data)
#         else:
#             return self.search(node.right,data)
#
#
# def main():
#     arr=list(map(int,input().split()))
#     bst=BST()
#     for ele in arr:
#         bst.root=bst.addNode(bst.root,ele)
#     bst.preOrder(bst.root)
#     print()
#     bst.inOrder(bst.root)
#     print()
#     ele=int(input())
#     if(bst.search(bst.root,ele)==None):
#         print("Search element is not present")
#     else:
#         print("Search element is present")
#
# if __name__ == '__main__':
#     main()
###Min and max value###3
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# class BST:
#     def __init__(self):
#         self.root=None
#     def addNode(self,node,data):
#         if(node is None):
#             return Node(data)
#             # newNode=Node(data)
#             # return newNode
#         if(data<node.data):
#             node.left=self.addNode(node.left,data)
#         else:
#             node.right=self.addNode(node.right,data)
#         return node
#     def preOrder(self,node):
#         if(node is None):
#             return
#         print(node.data,end=" ")
#         self.preOrder(node.left)
#         self.preOrder(node.right)
#     def inOrder(self,node):
#         if(node is None):
#             return
#         self.inOrder(node.left)
#         print(node.data, end=" ")
#         self.inOrder(node.right)
#     def search(self,node,data):
#         if(node is None or node.data==data):
#             return node
#         if(data<node.data):
#             return self.search(node.left,data)
#         else:
#             return self.search(node.right,data)
#     def minValue(self,node):
#         temp=node
#         while(temp.left is not None):
#             temp=temp.left
#         return temp.data
#     def maxValue(self,node):
#         temp=node
#         while(temp.right is not None):
#             temp=temp.right
#         return temp.data
#
#
# def main():
#     arr=list(map(int,input().split()))
#     bst=BST()
#     for ele in arr:
#         bst.root=bst.addNode(bst.root,ele)
#     bst.preOrder(bst.root)
#     print()
#     bst.inOrder(bst.root)
#     print()
#     print(bst.minValue(bst.root))
#     print(bst.maxValue(bst.root))
#
# if __name__ == '__main__':
#     main()


####Deletion in BST#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# class BST:
#     def __init__(self):
#         self.root=None
#     def addNode(self,node,data):
#         if(node is None):
#             return Node(data)
#             # newNode=Node(data)
#             # return newNode
#         if(data<node.data):
#             node.left=self.addNode(node.left,data)
#         else:
#             node.right=self.addNode(node.right,data)
#         return node
#     def delete(self,data):
#         self.root=self.deletionInBST(self.root,data)
#     def deletionInBST(self,node,data):
#         if(node is None):
#             return node
#         if(data<node.data):
#             node.left=self.deletionInBST(node.left,data)
#         elif(data>node.data):
#             node.right=self.deletionInBST(node.right,data)
#         else:
#             if(node.left is None):
#                 return node.right
#             elif(node.right is None):
#                 return node.left
#             else:
#                 node.data=self.minValue(node.right)
#                 node.right=self.deletionInBST(node.right,node.data)
#         return node
#
#     def preOrder(self,node):
#         if(node is None):
#             return
#         print(node.data,end=" ")
#         self.preOrder(node.left)
#         self.preOrder(node.right)
#     def inOrder(self,node):
#         if(node is None):
#             return
#         self.inOrder(node.left)
#         print(node.data, end=" ")
#         self.inOrder(node.right)
#     def search(self,node,data):
#         if(node is None or node.data==data):
#             return node
#         if(data<node.data):
#             return self.search(node.left,data)
#         else:
#             return self.search(node.right,data)
#     def minValue(self,node):
#         temp=node
#         while(temp.left is not None):
#             temp=temp.left
#         return temp.data
#     def maxValue(self,node):
#         temp=node
#         while(temp.right is not None):
#             temp=temp.right
#         return temp.data
#
#
# def main():
#     arr=list(map(int,input().split()))
#     bst=BST()
#     for ele in arr:
#         bst.root=bst.addNode(bst.root,ele)
#     bst.preOrder(bst.root)
#     print()
#     bst.inOrder(bst.root)
#     print()
#     ele=int(input())
#     bst.root=bst.deletionInBST(bst.root,ele)
#     bst.inOrder(bst.root)
# if __name__ == '__main__':
#     main()

# ####Check if BT is BST#####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def isBST(node,minRange,maxRange):
#     if(node is None):
#         return True
#     if(node.data<minRange or node.data>maxRange):
#         return False
#     return isBST(node.left,minRange,node.data) and isBST(node.right,node.data,maxRange)
#
# def main():
#     root=Node(50)
#     root.left=Node(25)
#     root.right=Node(23)
#     root.left.left=Node(15)
#     root.left.right=Node(30)
#     root.right.left=Node(70)
#     root.right.right=Node(85)
#     root.left.left.left=Node(10)
#     root.left.left.right=Node(23)
#     if(isBST(root,float('-inf'),float('inf'))):
#         print("BT is BST")
#     else:
#         print("BT is not BST")
#
# if __name__ == '__main__':
#     main()

####Kth Smallest Element####
'''
    Time complexity: O(N)
    Space complexity: O(N)
    Where 'N' is number of nodes in binary serach tree.
'''
def inorder(root):
  if(root==None):
    return []
  left_list=inorder(root.left)
  right_list=inorder(root.right)
  return left_list+[root.data]+right_list
def KthSmallestNumber(root,k):
  lst=inorder(root)
  if(k>len(lst)):
    return -1
  return (lst[k-1])
