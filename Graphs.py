####Graph Representation####
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.adjMat=[]
#         for i in range(self.vertex):
#             self.adjMat.append([0]*self.vertex)
#
#     def addEdge(self,u,v):
#         self.adjMat[u][v]=1
#         self.adjMat[v][u]=1
#
#     def edgePresent(self,u,v):
#         if(self.adjMat[u][v]==1):
#             return True
#         else:
#             return False
#
#     def removeEdge(self,u,v):
#         if(self.edgePresent(u,v)):
#             self.adjMat[u][v]=0
#             self.adjMat[v][u]=0
#
#     def printMat(self):
#         for i in range(self.vertex):
#             for j in range(self.vertex):
#                 print(self.adjMat[i][j],end=" ")
#             print()
#
# def main():
#     n,e=map(int,input().split())
#     graph=Graph(n)
#     for i in range(e):
#         u,v=map(int,input().split())
#         graph.addEdge(u,v)
#     graph.printMat()
#     graph.removeEdge(1,2)
#     print("After removal")
#     graph.printMat()
# if __name__ == '__main__':
#     main()

######Adjacency List Representation####
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.graph=[None]*self.vertex
#     def addEdge(self,u,v):
#         newNode=Node(v)
#         newNode.next=self.graph[u]
#         self.graph[u]=newNode
#
#         newNode = Node(u)
#         newNode.next = self.graph[v]
#         self.graph[v] = newNode
#     def edgePresent(self,u,v):
#         temp=self.graph[u]
#         while(temp is not None):
#             if(temp.data==v):
#                 return True
#             temp=temp.next
#         return False
#
#     def edgeRemove(self,u,v):
#         count=0
#         if(self.edgePresent(u,v)):
#             temp=self.graph[u]
#         while(temp is not None):
#             count+=1
#             if(temp.data==v):
#                 return
#         if(count==1):
#             self.graph[u]=temp.next
#             temp.next=None
#         else:
#
#         #delete the linked list node
#
#     def printGraph(self):
#         for i in range(self.vertex):
#             print("Adjacency list of vertex {} is = ".format(i),end=" ")
#             temp=self.graph[i]
#             while temp:
#                 print("->",temp.data,end=" ")
#                 temp=temp.next
#             print()
#
# def main():
#     n,e=map(int,input().split())
#     gr=Graph(n)
#     for i in range(e):
#         u,v=map(int,input().split())
#         gr.addEdge(u,v)
#
#     gr.printGraph()
#     x,y=map(int,input().split())
#     print(gr.edgePresent(x,y))
#
# if __name__ == '__main__':
#     main()

####Breadth First Search#####
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
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.adjMat=[]
#         for i in range(self.vertex):
#             self.adjMat.append([0]*self.vertex)
#
#     def addEdge(self,u,v):
#         self.adjMat[u][v]=1
#         self.adjMat[v][u]=1
#
#     def edgePresent(self,u,v):
#         if(self.adjMat[u][v]==1):
#             return True
#         else:
#             return False
#
#     def removeEdge(self,u,v):
#         if(self.edgePresent(u,v)):
#             self.adjMat[u][v]=0
#             self.adjMat[v][u]=0
#     def bfs(self,v):
#         qu=QueueUsingList()
#         qu.enqueue(v)
#         visited=[False]*self.vertex
#         visited[v]=True
#         while(qu.isEmpty() is False):
#             node=qu.dequeue()
#             print(node,end=" ")
#             for i in range(self.vertex):  #V+E
#                 if(self.adjMat[node][i]==1 and visited[i]==False):
#                     qu.enqueue(i)
#                     visited[i]=True
#
#     def printMat(self):
#         for i in range(self.vertex):
#             for j in range(self.vertex):
#                 print(self.adjMat[i][j],end=" ")
#             print()
#
#
# def main():
#     n,e=map(int,input().split())
#     graph=Graph(n)
#     for i in range(e):
#         u,v=map(int,input().split())
#         graph.addEdge(u,v)
#     graph.bfs(0)
#
#
# if __name__ == '__main__':
#     main()

#####Depth First search####
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.adjMat=[]
#         for i in range(self.vertex):
#             self.adjMat.append([0]*self.vertex)
#
#     def addEdge(self,u,v):
#         self.adjMat[u][v]=1
#         self.adjMat[v][u]=1
#
#     def edgePresent(self,u,v):
#         if(self.adjMat[u][v]==1):
#             return True
#         else:
#             return False
#
#     def removeEdge(self,u,v):
#         if(self.edgePresent(u,v)):
#             self.adjMat[u][v]=0
#             self.adjMat[v][u]=0
#     def dfs(self,u,visited):
#         print(u,end=" ")
#         visited[u]=True
#         for i in range(self.vertex):
#             if(self.adjMat[u][i]==1 and visited[i]==False):
#                 self.dfs(i,visited)
#
#
#     def printMat(self):
#         for i in range(self.vertex):
#             for j in range(self.vertex):
#                 print(self.adjMat[i][j],end=" ")
#             print()
#
# def main():
#     n,e=map(int,input().split())
#     graph=Graph(n)
#     for i in range(e):
#         u,v=map(int,input().split())
#         graph.addEdge(u,v)
#     visited=[False]*graph.vertex
#     graph.dfs(6,visited)
#
#
# if __name__ == '__main__':
#     main()

####DFS on disconnected graph#####
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.adjMat=[]
#         for i in range(self.vertex):
#             self.adjMat.append([0]*self.vertex)
#
#     def addEdge(self,u,v):
#         self.adjMat[u][v]=1
#         self.adjMat[v][u]=1
#
#     def edgePresent(self,u,v):
#         if(self.adjMat[u][v]==1):
#             return True
#         else:
#             return False
#
#     def removeEdge(self,u,v):
#         if(self.edgePresent(u,v)):
#             self.adjMat[u][v]=0
#             self.adjMat[v][u]=0
#     def dfs(self,u,visited):
#         print(u,end=" ")
#         visited[u]=True
#         for i in range(self.vertex):
#             if(self.adjMat[u][i]==1 and visited[i]==False):
#                 self.dfs(i,visited)
#
#
#     def printMat(self):
#         for i in range(self.vertex):
#             for j in range(self.vertex):
#                 print(self.adjMat[i][j],end=" ")
#             print()
#
#
# def main():
#     n,e=map(int,input().split())
#     graph=Graph(n)
#     for i in range(e):
#         u,v=map(int,input().split())
#         graph.addEdge(u,v)
#     visited=[False]*graph.vertex
#     for i in range(graph.vertex):
#         if(visited==False):
#             graph.dfs(i,visited)
#         print()
#
#
# if __name__ == '__main__':
#     main()

###Number of connected components and is graph connected or disconnected####
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.adjMat=[]
#         for i in range(self.vertex):
#             self.adjMat.append([0]*self.vertex)
#
#     def addEdge(self,u,v):
#         self.adjMat[u][v]=1
#         self.adjMat[v][u]=1
#
#     def edgePresent(self,u,v):
#         if(self.adjMat[u][v]==1):
#             return True
#         else:
#             return False
#
#     def removeEdge(self,u,v):
#         if(self.edgePresent(u,v)):
#             self.adjMat[u][v]=0
#             self.adjMat[v][u]=0
#     def dfs(self,u,visited):
#         print(u,end=" ")
#         visited[u]=True
#         for i in range(self.vertex):
#             if(self.adjMat[u][i]==1 and visited[i]==False):
#                 self.dfs(i,visited)
#
#
#     def printMat(self):
#         for i in range(self.vertex):
#             for j in range(self.vertex):
#                 print(self.adjMat[i][j],end=" ")
#             print()
#
#
# def main():
#     n,e=map(int,input().split())
#     graph=Graph(n)
#     for i in range(e):
#         u,v=map(int,input().split())
#         graph.addEdge(u,v)
#     count=0
#     visited=[False]*graph.vertex
#     for i in range(graph.vertex):
#         if(visited[i] is False):
#             graph.dfs(i,visited)
#             count+=1
#         print()
#     print("The number of connected components: ",count)
#     if(count>1):
#         print("Disconnected Graph")
#     else:
#         print("Connected Graph")
#
#
# if __name__ == '__main__':
#     main()

####Path exists or not####
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
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.graph=[None]*self.vertex
#
#     def addEdge(self,u,v):
#         node=Node(v)
#         node.next = self.graph[u]
#         self.graph[u]=node
#
#     def edgePresent(self,u,v):
#         temp=self.graph[u]
#         while temp:
#             if (temp.data==v):
#                 return  True
#             temp=temp.next
#         return False
#     def isPath(self,src,dest):
#         visited=[False]*self.vertex
#         qu=QueueUsingList()
#         qu.enqueue(src)
#         visited[src]=True
#         while(qu.isEmpty() is False):
#             node=qu.dequeue()
#             if(node==dest):
#                 return True
#             temp=self.graph[node]
#             while(temp):
#                 if(visited[temp.data]==False):
#                     qu.enqueue(temp.data)
#                     visited[temp.data]=True
#                 temp=temp.next
#         return False
#     def printGraph(self):
#         for i in range(self.vertex):
#             print("Adjacency list of vertex {} is = ".format(i), end=" ")
#             temp = self.graph[i]
#             while temp:
#                 print("->", temp.data, end=" ")
#                 temp = temp.next
#             print()
#
# def main():
#     n,e=map(int,input().split())
#     graph=Graph(n)
#     for i in range(e):
#         u,v=map(int,input().split())
#         graph.addEdge(u,v)
#     src,dest=map(int,input().split())
#     print(graph.isPath(src,dest))
#
#
# if __name__ == '__main__':
#     main()


####Minimum remove####
# def main():
#     T=int(input())
#     while(T>0):
#         n,e=map(int,input().split())
#         k=n-1
#         r=e-k
#         print(r)
#         T=T-1
#
# if __name__ == '__main__':
#     main()

###Buying Restaurants###
#No of vertices count for the restaurant not edges
# tc = int(input())
# for i in range(tc):
#     e = int(input())
#     arr=[0]*10001
#     for x in range(e):
#         a,b = map(int,input().split())
#         arr[a]=1
#         arr[b]=1
#     c=0
#     for x in arr:
#         if x==1:
#             c+=1
#     print(c)

###Graphs are falling####
# def main():
#     n=int(input())
#     list1=list(map(int,input().split()))
#     sum=0
#     for i in range (len(list1)):
#         sum+=list1[i]
#     degree=int(2*(n-1))
#     if(sum==degree):
#         print("Yes")
#     else:
#         print("No")
#
# if __name__ == '__main__':
#     main()
#

####Graph Tree###
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.adjMat=[]
#         for i in range(self.vertex):
#             self.adjMat.append([0]*self.vertex)
#
#     def addEdge(self,u,v):
#         self.adjMat[u][v]=1
#         self.adjMat[v][u]=1
#
#     def edgePresent(self,u,v):
#         if(self.adjMat[u][v]==1):
#             return True
#         else:
#             return False
#
#     def removeEdge(self,u,v):
#         if(self.edgePresent(u,v)):
#             self.adjMat[u][v]=0
#             self.adjMat[v][u]=0
#     def dfs(self,u,visited):
#         #print(u,end=" ")
#         visited[u]=True
#         for i in range(self.vertex):
#             if(self.adjMat[u][i]==1 and visited[i]==False):
#                 self.dfs(i,visited)
# def main():
#     T=int(input())
#     while(T>0):
#         n,e=map(int,input().split())
#         graph=Graph(n)
#         for i in range(e):
#             u, v = map(int, input().split())
#             graph.addEdge(u, v)
#         count = 0
#         visited = [False] * graph.vertex
#         for i in range(graph.vertex):
#             if (visited[i] is False):
#                 graph.dfs(i, visited)
#                 count += 1
#             #print()
#         if (count > 1):
#             print("NO")
#         else:
#             print("YES")
#         T=T-1
#
# if __name__ == '__main__':
#     main()


###Longest Path ####Not completed
# class Graph:
#     def __init__(self,n):
#         self.vertex=n
#         self.adjMat=[]
#         for i in range(self.vertex):
#             self.adjMat.append([0]*self.vertex)
#
#     def addEdge(self,u,v):
#         self.adjMat[u][v]=1
#         self.adjMat[v][u]=1
#
#     def edgePresent(self,u,v):
#         if(self.adjMat[u][v]==1):
#             return True
#         else:
#             return False
#
#     def removeEdge(self,u,v):
#         if(self.edgePresent(u,v)):
#             self.adjMat[u][v]=0
#             self.adjMat[v][u]=0
#     def dfs(self,u,visited,curr_max,res):
#         #print(u,end=" ")
#         visited[u]=True
#         curr_max += 1
#         for i in range(self.vertex):
#             if(self.adjMat[u][i]==1 and visited[i]==False):
#                 self.dfs(i,visited,curr_max,res)
#         print(curr_max,end=" ")
#         res=max(res,curr_max)
#         print(res)
#         return res
#
# def main():
#     T=int(input())
#     while(T>0):
#         n,e=map(int,input().split())
#         graph=Graph(n)
#         for i in range(e):
#             u, v = map(int, input().split())
#             graph.addEdge(u, v)
#         count = 0
#         visited = [False] * graph.vertex
#         curr_max=0
#         res=0
#         for i in range(graph.vertex):
#             if (visited[i] is False):
#                 k=graph.dfs(i, visited,curr_max,res)
#                 count += 1
#                 print(k)
#         T=T-1
# if __name__ == '__main__':
#     main()

####Detect Cycle####
class QueueUsingList:
    def __init__(self):
        self.que=[]
        self.front=0
        self.size=0
    def isEmpty(self):
        return self.size==0
    def enqueue(self,data):
        self.que.append(data)
        self.size+=1
    def dequeue(self):
        if(self.isEmpty()):
            print("queue is empty")
            return
        temp=self.que[self.front]
        self.front+=1
        self.size-=1
        return temp

    def frontele(self):
        if(self.isEmpty()):
            print("Queue is empty ")
            return
        return self.que[self.front]
    def printQueue(self):
        if(self.isEmpty()):
            print("Queue is empty ")
            return
        for i in range(self.size):
            print(self.que[self.front+i],end=" ")
        print()
class Graph:
    def __init__(self,n):
        self.vertex=n
        self.adjMat=[]
        for i in range(self.vertex):
            self.adjMat.append([0]*self.vertex)

    def addEdge(self,u,v):
        self.adjMat[u][v]=1
        self.adjMat[v][u]=1

    def edgePresent(self,u,v):
        if(self.adjMat[u][v]==1):
            return True
        else:
            return False

    def removeEdge(self,u,v):
        if(self.edgePresent(u,v)):
            self.adjMat[u][v]=0
            self.adjMat[v][u]=0

    def isCyclicConnected(self,v,visited):
        qu=QueueUsingList()
        qu.enqueue(v)
        visited[v]=True
        parent=[-1]*self.vertex
        while(qu.isEmpty() is False):
            node=qu.dequeue()
            for i in range(self.vertex):
                if(self.adjMat[node][i]==1):
                    if(visited[i]==False):
                        qu.enqueue(i)
                        visited[i]=True
                        parent[i]=node
                    elif(parent[node]!=i):
                        return True
        return False

    def printMat(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.adjMat[i][j],end=" ")
            print()


def main():
    n,e=map(int,input().split())
    graph=Graph(n)
    for i in range(e):
        u,v=map(int,input().split())
        graph.addEdge(u,v)
    visited=[False]*graph.vertex
    flag=0
    for i in range(graph.vertex):
        if(visited[i] is False and graph.isCyclicConnected(i,visited)):
            flag=1
            break
    if(flag==1):
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()