
def valid_solution(board):
    boolean = True
    
    #check each row
    for i in range(9):
        if len(set(board[i])) != 9:
            boolean = False
    
    #check each column
    for i in range(9):
        lst=[]
        for j in range(9):
            lst.append(board[j][i])
        if len(set(lst)) != 9:
            boolean = False
    
    #check each 3 by 3 section
    for x in range(3):
        for y in range(3):
            lst=[]
            for i in range(3*x,3*(x+1)):
                for j in range(3*y,3*(y+1)):
                    lst.append(board[i][j])
            if len(set(lst)) != 9:
                boolean = False 
    
    return boolean