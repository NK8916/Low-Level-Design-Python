import enum


class GridPosition(enum.Enum):
    EMPTY=0
    RED=1
    YELLOW=2

class Grid:
    def __init__(self,rows,cols):
        self._rows = rows
        self._cols = cols
        self._grid = None
        self.initialize()
    
    def initialize(self):
        self._grid = [[GridPosition.EMPTY for _ in range(self._cols)] for _ in range(self._rows)]
    
    def getGrid(self):
        return self._grid
    
    def getColumnCount(self):
        return self._cols

    def placePieces(self,col,piece):
        while True:
            if col<0 or col>=self._cols:
                raise ("Invalid column position")
            if piece==GridPosition.EMPTY:
                raise ("Invalid piece position")
            for row in range(self._rows-1,-1,-1):
                if self._grid[row][col]==GridPosition.EMPTY:
                    return row
    
    def checkWin(self,connectN,row,col,piece):
        count=0
        for c in range(self._cols):
            if self._grid[row][c]==piece:
                count+=1
            else:
                count=0
            if count==connectN:
                return True
        
        count=0
        for r in range(self._rows):
            if self._grid[r][col]==piece:
                count+=1
            else:
                count=0
            if count==connectN:
                return True
            
        count=0
        for r in range(self._rows):
            c=row+col-r
            if c>=0 and c<self._cols and self._grid[row][c]==piece:
                count+=1
            else:
                count=0
            if count==connectN:
                return True
        
        count=0

        for r in range(self._rows):
            c=col-row+r
            if c>=0 and c<self._cols and self._grid[row][c]==piece:
                count+=1
            else:
                count=0
            if count==connectN:
                return True
        return False


class Player:
    def __init__(self,name,piece) -> None:
        self._name=name
        self._piece=piece
    
    def getName(self):
        return self._name

    def getPiece(self):
        return self._piece

class Game:
    def __init__(self,grid,connectN,targetScore) -> None:
        self._grid=grid
        self._connectN = connectN
        self._targetScore = targetScore
        self._players=[Player("player 1",GridPosition.RED),Player("player 1",GridPosition.YELLOW)]
        self._scores={}
        for player in self._players:
            self._scores[player.getName()]=0
    
    def printBoard(self):
        m,n=len(self._grid),len(self._grid[0])

        for row in range(m):
            row=""
            for col in range(n):
                if self._grid[row][col]==GridPosition.EMPTY:
                    row+="0 "
                elif self._grid[row][col]==GridPosition.RED:
                   row+="R "
                elif self._grid[row][col]==GridPosition.YELLOW:
                    row+="Y "
            print(row)


        
    def playMove(self,player):
        self.printBoard()
        print(f"{player.getName()}'s Turn")
        cols=self._grid.getColumnCount()
        moveCol=input(f"Enter the col between {0} and {cols-1}: ")
        moveRow=self._grid.placePieces(moveCol,player.getPiece())
        return (moveRow,moveCol)

    def playRound(self):
        while True:
            for player in self._players:
                row,col=self.playMove(player)
                checkWin=self._grid(self._connectN,row,col,player.getPiece())
                if checkWin:
                    self._scores[player.getName()]+=1
                    return player
    
    def play(self):
        maxScore=0
        winner=None

        while maxScore<self._targetScore:
            winner=self.playRound()
            print(f"{winner.getName()} won the round")
            maxScore=max(maxScore,self._scores[winner.getName()])
            self._grid.initialize()
        


        


