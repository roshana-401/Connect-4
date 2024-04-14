import numpy as np
from colorama import Fore


def changeTurn(turn,player):
    if turn==player[0]:
        return 1
    else:
        return 0


def insertInCol(numberOfCol,color):
    playGround[capacityOfColumns[numberOfCol-1]-1][numberOfCol-1]=color
    capacityOfColumns[numberOfCol-1]-=1
    if capacityOfColumns[numberOfCol-1]==0:
        showcol.remove(numberOfCol)

def printPlayGround():
    for row in range(0,5):
        print("\t",end="")

        print(Fore.BLACK,"[",Fore.RESET,end ="")
        for col in range(0,5):
            if playGround[row][col]=="red":
                print(Fore.RED,"red",Fore.RESET,end ="")
            elif playGround[row][col]=="yellow":
                print(Fore.YELLOW,"yell",Fore.RESET,end ="")
            else:
                print(Fore.BLACK,"none",Fore.RESET,end ="")
            
            if col!=4:
                print(Fore.BLACK,",",Fore.RESET,end ="")
            else:
                print(Fore.BLACK,"]",Fore.RESET)
def checkRow():
    numberOfColor=0
    selectColor=""
    for row in range(4,-1,-1):
        selectColor=playGround[row][0]
        if selectColor!='none':
            numberOfColor=0
            for col in range(0,5):
                if playGround[row][col]=="yellow" or playGround[row][col]=="red":
                    if playGround[row][col]==selectColor:
                        numberOfColor+=1
                        if numberOfColor==4:
                            return selectColor
                    else:
                        selectColor=playGround[row][col]
                        numberOfColor=1
                else:
                    break
        else:
            break
    return "null"

def checkColumn():
    numberOfColor=0
    selectColor=""
    for col in range(0,5):
        selectColor=playGround[4][col]
        if selectColor!='none':
            numberOfColor=0
            for row in range(4,-1,-1):
                if playGround[row][col]=="yellow" or playGround[row][col]=="red":
                    if playGround[row][col]==selectColor:
                        numberOfColor+=1
                        if numberOfColor==4:
                            return selectColor
                    else:
                        selectColor=playGround[row][col]
                        numberOfColor=1
                else:
                    break
        else:
            break
    return "null"

def chanceRow(step,row,col):

    color=playGround[row][col]
    if color!='none':
        boolcolor=False
    else:
        boolcolor=True
    if playGround[row+step][col]=='none' or playGround[row+step][col]==color or boolcolor==True:
      
        if boolcolor==True and playGround[row+step][col]!='none':
            color=playGround[row+step][col]
            boolcolor=False
        if playGround[row+step+step][col]=='none' or playGround[row+step+step][col]==color or boolcolor==True:
            
            if boolcolor==True and playGround[row+step+step][col]!='none':
                color=playGround[row+step+step][col]
                boolcolor=False
            if playGround[row+step+step+step][col]=='none' or playGround[row+step+step+step][col]==color or boolcolor==True:
                
                if playGround[row+step+step+step][col]!='none' and playGround[row+step+step][col]!='none' and playGround[row+step][col]!='none' and playGround[row][col]!='none':
                    return False
                return True
    return False

def chanceCol(step,row,col):       
    color=playGround[row][col]
    if color!='none':
        boolcolor=False
    else:
        boolcolor=True
    if playGround[row][col+step]=='none' or playGround[row][col+step]==color or boolcolor==True:
       
        if boolcolor==True and playGround[row][col+step]!='none':
            color=playGround[row][col+step]
            boolcolor=False
        if playGround[row][col+step+step]=='none' or playGround[row][col+step+step]==color or boolcolor==True:
                       
            if boolcolor==True and playGround[row][col+step+step]!='none':
                color=playGround[row][col+step+step]
                boolcolor=False
            if playGround[row][col+step+step+step]=='none' or playGround[row][col+step+step+step]==color or boolcolor==True:
                
                if playGround[row][col+step+step+step]!='none' and playGround[row][col+step+step]!='none' and playGround[row][col+step]!='none' and playGround[row][col]!='none':
                    return False    
                return True
    return False

def chanceCross(stepCol,stepRow,row,col):       
    color=playGround[row][col]
    if color!='none':
        boolcolor=False
    else:
        boolcolor=True
    if -1<row+stepRow<5 and -1<col+stepCol<5 and (playGround[row+stepRow][col+stepCol]=='none' or playGround[row+stepRow][col+stepCol]==color or boolcolor==True):

        if boolcolor==True and playGround[row+stepRow][col+stepCol]!='none':
            color=playGround[row+stepRow][col+stepCol]
            boolcolor=False
        if -1<row+stepRow+stepRow<5 and -1<col+stepCol+stepCol<5 and (playGround[row+stepRow+stepRow][col+stepCol+stepCol]=='none' or playGround[row+stepRow+stepRow][col+stepCol+stepCol]==color or boolcolor==True):        
            if boolcolor==True and playGround[row+stepRow+stepRow][col+stepCol+stepCol]!='none':
                color=playGround[row+stepRow+stepRow][col+stepCol+stepCol]
                boolcolor=False
            if -1<row+stepRow+stepRow+stepRow<5 and -1<col+stepCol+stepCol+stepCol<5 and (playGround[row+stepRow+stepRow+stepRow][col+stepCol+stepCol+stepCol]=='none' or playGround[row+stepRow+stepRow+stepRow][col+stepCol+stepCol+stepCol]==color or boolcolor==True):
                if playGround[row+stepRow+stepRow+stepRow][col+stepCol+stepCol+stepCol]!='none' and playGround[row+stepRow+stepRow][col+stepCol+stepCol]!='none' and playGround[row+stepRow][col+stepCol]!='none' and  playGround[row][col]!='none':
                    return False         
                return True
    return False

def chance():
    numOfChance=0
    for row in range(0,5):
        for col in range(0,5):
                if 5-(row+1)+1>=4:
                    test=chanceRow(1,row,col)
                    if test==True:
                        numOfChance+=1
                if 5-(col+1)+1>=4:
                    test=chanceCol(1,row,col)
                    if test==True:
                        numOfChance+=1
                if 0<=col<=2 and 0<=row<=1:
                    test=chanceCross(1,1,row,col)
                    if test==True:
                        numOfChance+=1
                if 0<=col<=2 and 3<=row<=4:
                    test=chanceCross(1,-1,row,col)
                    if test==True:
                        numOfChance+=1
    return numOfChance
    # print(numOfChance)

def checkCross():
    numberOfColor=0
    selectColor=""
    values=[[5,1,5,1],[5,0,5,1],[4,0,4,1],[5,3,-1,-1],[5,4,-1,-1],[4,4,0,-1]]
    for i in range(0,6,1):

        row=values[i][0]
        start=values[i][1]
        end=values[i][2]
        step=values[i][3]
        
        selectColor=playGround[row-1][start]
        numberOfColor=0
        for col in range(start,end,step):
            row-=1
            if selectColor!='none':
                if playGround[row][col]=="yellow" or playGround[row][col]=="red":
                    if playGround[row][col]==selectColor:
                        numberOfColor+=1
                        if numberOfColor==4:
                            return selectColor
                    else:
                        selectColor=playGround[row][col]
                        numberOfColor=1
                else:
                    break
            else:
                break
      
    return "null"



player=[]
color=[]
for i in range(1,3):
    print(f"The name of the player{i}")
    player.append(input().strip())
    if i!=2:
        while (True):
            print(f"{player[i-1]} ,choose your color:(red/yellow)")
            colorTest=input().strip().lower()
            colorTest=colorTest.replace(" ","")
            if colorTest!="red" and colorTest!="yellow":
                print("Invalid value!!!")
            else:     
                color.append(colorTest)
                break

if color[0]=="red":
    color.append("yellow")
else:
    color.append("red")

while True:
    playGround=np.full((5,5),"none",dtype='U6')
    playerTurn=0
    showcol=[1,2,3,4,5]
    capacityOfColumns=[5,5,5,5,5]
    loop=0
    numOfChance=0
    while True:
        loop+=1
        print(f"The color of the {player[0]} is {color[0]}")
        print(f"The color of the {player[1]} is {color[1]}\n")
        print("This is the playground: ")
        printPlayGround()
        print(f"\n Turn: {player[playerTurn]}\n")
        while True:
            try:
                print(f"Enter the column you want: {showcol}")
                colSelect=int(input().replace(" ",""))
                if colSelect not in showcol:
                    print(f"The number must be in the range {showcol}!!!")
                    continue
                break
            except:
                print("Invalid value!!!")
        insertInCol(colSelect,color[playerTurn])
        playerTurn=changeTurn(player[playerTurn],player)
        chanceAgain=chance()
        if chanceAgain==0:
            print("The game has reached a dead end!!!!")
            break
        if loop>=7:
            print("eweuyuewy")
            row=checkRow()
            col=checkColumn()
            cross=checkCross()
            if row!="null" or col!="null" or cross!="null":
                if row==color[0] or col==color[0] or cross==color[0]:
                    print(f"**{player[0]} has won**")
                else:
                    print(f"**{player[1]} has won**")
                break
    print("Do you want to play again?(y or n)")
    answer=input().replace(" ","")
    if answer=="n":
        break