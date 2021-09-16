###open with write mode###
# f=open("H:\\file handling\\testfile.txt","w")
# t=int(input())
# f.write(str(t)+"\n")
# while(t!=0):
#     n=int(input())
#     f.write(str(n)+"\n")
#     t=t-1
# f.close()


###Open with read mode######
# f=open("H:\\file handling\\testfile.txt","r")
#print(f.read(4)) #First four characters

# print(f.readline())
# print(f.readline())
#
# for line in f:
#     print(line,end="")

# print(f.readlines())

# data=f.readlines()
# print(data)
# for line in data:
#     word=line.split()
#     print(word)

####open with append mode####
# f=open("H:\\file handling\\testfile.txt","a")
# f.write("\nAppend Function") #it will append it at the end, if we do it in write mode it'll overrride the entire file


####Array Generator####
'''
Test
Size
element of array space-separated
'''
# import random
# f = open("H:\\file handling\\testCaseFile.txt","w")
# t=10
# f.write(str(t)+"\n")
# for i in range(t):
#     size=random.randrange(1,10)
#     f.write(str(size)+"\n")
#     for j in range(size):
#         ele=random.randrange(1,10)
#         f.write(str(ele)+" ")
#     f.write("\n")

'''
index of min element
minimum element and print its index
# '''
# f=open("H:\\file handling\\expectedOutput.txt","w")
# r=open("H:\\file handling\\testCaseFile.txt","r")
# t=int(r.readline().strip())
# while(t>0):
#     n=int(r.readline().strip())
#     data=r.readline().strip()
#     arr=list(map(int,data.split()))
#     min=arr[0]
#     ind=0
#     for i in range(1,n):
#         if(arr[i]<min):
#             min=arr[i]
#             ind=i
#     f.write(str(ind)+"\n")
#     t=t-1