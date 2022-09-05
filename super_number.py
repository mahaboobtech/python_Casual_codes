def fact(j):
    n = j
    x=[]
    f=1
    for i in range(n,0,-1):
        x.append(i) 
    for i in x:
        f*=i

    return f

def sumofDigits(m):
    n = m
    sumr = 0
    for i in str(n):
        sumr += int(i)

    return sumr

ghoyy= []
temp=[]
hy=" "
for i in range(1000):
    for j in str(i):#making list of a number each digit factorial
        temp.append(fact(int(j)))
        print("the number is ",i)
        print("the temp is ",temp)
        hy= sum(temp)                #converting list to string line wise
        print("the valueis ",hy)
        uh=sumofDigits(hy)#sumof digiting 
        print("the sum of digits is ",uh,"\n")
        if i==hy:
            ghoyy.append(i)
    temp.clear()
    hy=" "
print("the final is ",ghoyy)
