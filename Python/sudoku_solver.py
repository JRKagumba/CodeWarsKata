"""
Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.
"""


def sudoku(puzzle):
    
    letters =['A','B','C','D','E','F','G','H','I']
    numbers =['1','2','3','4','5','6','7','8','9']
    nums = [1,2,3,4,5,6,7,8,9]

    lst_of_sqrs = [letters[i]+numbers[j] for i in range(9) for j in range(9)]
    arr = [[0 for i in range(9)] for j in range(9)]

    Sudoku_Dict = {}
    for i in range(9):
        for j in range(9):
            arr[i][j]= letters[i]+numbers[j]

    for i in lst_of_sqrs:
        Sudoku_Dict[i]={}
        Sudoku_Dict[i]['possib_vals']=[1,2,3,4,5,6,7,8,9]
        Sudoku_Dict[i]['peers']=[]    
    
    #Creating the list of units
    unit_lst=[]
    for i in range(9):   #Row Units
        unit_lst.append(arr[i])
    for i in range(9):   #Column Units
        unit_lst.append([arr[j][i] for j in range(9)])    
    for x in range(3):   #3 by 3 Sections
        for y in range(3):
            lst=[]
            for i in range(3*x,3*(x+1)):
                for j in range(3*y,3*(y+1)):
                    lst.append(arr[i][j])    
            unit_lst.append(lst)


    #Append peers to dict              
    for i in lst_of_sqrs:            
        for unit in unit_lst:
            if i in unit:
                for cell in unit:
                    if (cell != i) and (cell not in Sudoku_Dict[i]['peers']):
                        Sudoku_Dict[i]['peers'].append(cell)

    ZeroChecker=[0]
    while 0 in ZeroChecker:                    

        #Getting values from puzzle to dict
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    Sudoku_Dict[letters[i]+numbers[j]]['possib_vals'] = [puzzle[i][j]]                 

        #Eliminate from peers
        for i in lst_of_sqrs:
            if len(Sudoku_Dict[i]['possib_vals']) == 1:
                for peer in Sudoku_Dict[i]['peers']:
                    if Sudoku_Dict[i]['possib_vals'][0] in Sudoku_Dict[peer]['possib_vals']:
                        Sudoku_Dict[peer]['possib_vals']=[x for x in Sudoku_Dict[peer]['possib_vals'] if x != Sudoku_Dict[i]['possib_vals'][0]]
                        

        #Only Possibility?
        for i in lst_of_sqrs:
            if len(Sudoku_Dict[i]['possib_vals']) > 1:
                for j in range(len(Sudoku_Dict[i]['possib_vals'])):
                    Only_Poss = True
                    for peer in Sudoku_Dict[i]['peers']:
                        if Sudoku_Dict[i]['possib_vals'][j] in Sudoku_Dict[peer]['possib_vals']:
                            Only_Poss = False
                            break

                    if Only_Poss == True:
                        Sudoku_Dict[i]['possib_vals']=[Sudoku_Dict[i]['possib_vals'][j]]
                        break

        #Getting values from dict to puzzle               
        for i in range(9):
            for j in range(9):
                if len(Sudoku_Dict[letters[i]+numbers[j]]['possib_vals']) == 1:
                    puzzle[i][j] = Sudoku_Dict[letters[i]+numbers[j]]['possib_vals'][0]  
                    
                    
        #Check for 0s in board
        ZeroChecker=[]
        for row in puzzle:
            for cell in row:
                ZeroChecker.append(cell)
    

    return puzzle
