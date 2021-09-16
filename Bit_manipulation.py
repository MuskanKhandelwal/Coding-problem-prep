# a=5 #101
# b=7 #111
# print(a&b)
# print(a|b)
# print(~a)
# print(~b)
# print(~-4) # ~x=-x-1 =~(-4)=-(-4)-1=3
# print(a<<2) #multiplying 5 by 2^2
# print(b>>2) #dividing 7 by 2^2

####Alone number#####
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=list(map(int,input().split()))
        res=arr[0]
        for i in range(1,n):
            res=res^arr[i]
        print(res)
        T=T-1

if __name__ == '__main__':
    main()