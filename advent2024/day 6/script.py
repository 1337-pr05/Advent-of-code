def grid(file):
    # up down right left
    dir = ["^","V", ">", "<"] # show case the turtle
    grid = []
    with open(file) as f:
        lst = (f.readlines())      
    grid.extend([i.strip() for i in lst])
    start = initial_positon(grid)
    return grid,start
    
def initial_positon(grid):
    for i in grid:
        for j in i:
            if(j == "^"):
                return [grid.index(i),i.index(j)]
            else:
                continue
    return[-1,-1]
def traversel(grid,start):
    traveled_pos = []
    jump = 1
    x , y = start
    x_inc = y_inc = 0
    row = len(grid)
    col = len(grid[0])
    turtle = grid[x][y] 
    if(turtle == "^"):
        x_inc, y_inc = -1,0
    elif(turtle == "V"):
        x_inc, y_inc = 1,0
    elif(turtle == ">"):
        x_inc, y_inc = 0,1
    elif(turtle == "<"):
        x_inc, y_inc = 0,-1
    else:
        print("[*] No starting Position Found exiting!")
        return 
    
    while((x < row-1) and (y<col-1) and (x>0) and (y>0)):#this will make sure our turtle is inside the grid        
        x_update = x  + x_inc
        y_update = y  + y_inc
        #print(x,y,"   ",grid[x_update][y_update],turtle)
        if(grid[x_update][y_update] == "#"):
                if(turtle == "^"):
                    x_inc, y_inc = 0,1
                    turtle = ">"
                    continue
                elif(turtle == "V"):
                    x_inc, y_inc = 0,-1
                    turtle = "<"
                    continue
                elif(turtle == ">"):
                    x_inc, y_inc = 1,0
                    turtle = "V"
                    continue
                elif(turtle == "<"):
                    x_inc, y_inc = -1,0
                    turtle = "^"
                    continue
        elif(grid[x_update][y_update]=="." and ((x_update,y_update) not in traveled_pos)):
            jump+=1
            traveled_pos.append((x_update,y_update))
        x += x_inc
        y += y_inc
    return jump
grid_, start = grid("text.txt")

print(traversel(grid_,start))


