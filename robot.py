def robot():
    Move = 0
    posoncol = 0
    posonrow = 0
    dir = 'S'
    while True:
        val = input('enter your command: ')
        if val == 'quit':
            break
        else:
            valLenght = len(val)
            
            for row in range(valLenght):
                Move = 0
                MoveEast=0
                MoveNorth=0
                MoveSouth=0
                MoveWest=0
                if val[row] != 'M':
                    if dir == 'W':
                        dir = val[row]
                        
                    elif dir == 'E':
                        
                        dir = val[row]
                        
                    elif dir == 'N':
                        dir  = val[row]
                        
                    elif dir == 'S':
                        dir = val[row]
                else:
                    if  dir == 'W':
                        Move += 1
                        MoveWest -= Move
                    elif  dir == 'E':
                        Move += 1
                        
                        MoveEast += Move
                        
                    elif  dir == 'N':
                        Move += 1
                        MoveNorth -= Move
                    elif dir == 'S':
                        
                        Move += 1
                        MoveSouth += Move
                        
                
            
            
                posoncol +=   MoveEast + MoveWest
                posonrow +=   MoveSouth + MoveNorth
                

            
            if posoncol < 0 :
                posoncol = 0
            if posoncol > 4 :
                posoncol = 4

            if posonrow < 0:
                posonrow = 0
            if posonrow > 3 :
                posonrow = 3
            
            print(posonrow,posoncol,dir)

robot()

        


