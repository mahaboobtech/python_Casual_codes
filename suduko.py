import numpy  as np
# from sympy import false, re  
grid = [[0,0,0,1,5,0,0,4,0],[7,0,9,6,3,0,8,5,2],[4,5,3,7,2,0,1,0,9],[9,0,1,0,4,2,0,0,0],[0,0,0,0,9,0,0,8,0],[0,6,5,0,0,7,2,0,0],[0,9,4,0,0,0,0,7,8],[0,0,0,0,7,0,9,0,6],[6,0,0,0,0,5,0,0,0]]

print(np.matrix(grid))

def check(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for j in range(0,9):
        if grid[j][x]==n:
            return False
    y0= (y//3)*3
    x0= (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False
    return True

def solve():
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if check(y,x,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    print(np.matrix(grid))


solve()
# print(check(4,4,5))
