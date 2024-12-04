import re
def horizontal(input_string):
    pattern1 = r"XMAS"  
    # horizontal
    matches1 = re.findall(pattern1,input_string)
    #finding in reverse in horizontal
    matches2 = re.findall(pattern1[::-1],input_string)
    return len(matches1+matches2)

def vertical(input_string):
    with open("text.txt") as f:
        lst = f.readlines()
    row = len(lst)
    grid = lst
    
    # print((grid))
    if(len(grid)!=row):
        print("[*] The Text is not a perfect Square")
        exit()
    
    verticals = []
    for i in range(len(grid[0].strip())): 
        column = ''.join(row[i] for row in grid)  
        verticals.append(column)
    
    input_string = ''
    for i in verticals:
        for j in i:
            input_string +=j
    
    pattern3 = r"XMAS"      # vertical
    matches3 = re.findall(pattern3,input_string)
    matches4 = re.findall(pattern3[::-1],input_string)
    return len(matches3 + matches4)
         

def diagnol_right(file): 
    # converting all the diagonls into rows starting from top left to bottom right
    
    n = 0  
    with open(file) as f:
        grid = f.readlines()

    grid_from_column = []
    grid_from_row = []
    
    # this will extract all the pattern from diagnol startin from column
    
    for j in range(len(grid[0].strip())):
        row = ''
        for i in range(j,len(grid)):
            eqn = [i,i-n]
            row += grid[eqn[0]][eqn[1]]
        grid_from_column.append(row)
        n+=1
        
    # this will extract all the pattern from starting from row
    # but why starting from 1 (think about it!)
    
    n= 0
    for j in range(len(grid[0].strip())-1):
        row = ''
        for i in range(j,len(grid)-1):
            eqn = [i-n,i+1]
            row += grid[eqn[0]][eqn[1]]
        grid_from_row.append(row)
        n+=1  
    
    print(grid_from_row,grid_from_column)
    final = "".join(row for row in grid_from_row) + "".join(column for column in grid_from_column)
    
    pattern = r"XMAS"
    matches1 = re.findall(pattern, final)
    matches2 = re.findall(pattern[::-1], final)
    return len(matches1+matches2)

def diagnol_left(file):
     # converting all the diagonls into rows starting from top right to bottom left
     
    with open(file) as f:
        grid = f.readlines()

    col = len(grid[0]) #6
    n=0
    grid_from_column = []
    grid_from_row = []
    
    # this will extract all the pattern from diagnol startin from column
    for j in range(len(grid[0].strip())): #0 - 6 (exlucde 6)
        row = ''
        m=0
        for i in range(len(grid[0].strip())-n):  # 0 - 6(exlucde 6)
            eqn = [i+n,col-2-m]   # "\n"  was counted 2 char so col-2-m
            row += grid[eqn[0]].strip()[eqn[1]]

            m+=1
        n+=1

        grid_from_column.append(row)      
 
    n=0
    #  this will extract all the pattern from diagnol startin from column
    for j in range(len(grid[0].strip())-1): # 0 - 6 (exlucde 6)
       row = ''
       m=0
       for i in range(len(grid[0].strip())-n-1): #neglecting one iteration  
           eqn = [i,col-3-m-n]   # "\n"  was counted as 2 char so col-2-m
           row += grid[eqn[0]].strip()[eqn[1]]
           m+=1
       n+=1

       grid_from_row.append(row)    
    
    final = "".join(row for row in grid_from_row) + "".join(column for column in grid_from_column)
    pattern = r"XMAS"
    matches1 = re.findall(pattern, final)
    matches2 = re.findall(pattern[::-1], final)
    return len(matches1+matches2) 
    
with open("text.txt") as f:
    input_string = f.read()
 #Compute the result#
result = horizontal(input_string.strip()) + vertical(input_string.strip())+ diagnol_right("text.txt") + diagnol_left("text.txt")
print("Sum of all valid pattern of XMAS:", result)
