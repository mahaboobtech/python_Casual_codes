n = int(input("enter the triangle sequence "))
k = n+1
for i in range(k):
    for j in range(k-i):
        print(" ",end="")
    for n in range(2*i+1):
        if n==0 or n==2*i or i==k-1:
            print("*",end="")
        else:
            print(' ',end="")
    print()

# for j in range(2*i+1):
#         if j==0 or j==2*i or i==row-1:
#             print('*',end='')
#         else:
#             print(' ', end='')
