import numpy as np

class GridWorld:
    def __init__(self):
        self.grid = [['P',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','G']]
        # self.is_slippery = False
        self.create_frozen_tiles(True)
        
    def create_frozen_tiles(self,random):
        if random:
            count = 0
            while count<4:
                row = np.random.randint(0,4)
                col = np.random.randint(0,4)
                if (self.grid[row][col]!='P' or 'G') and self.grid[row][col]==' ':
                    count+=1
                    print(f"row {row} and col {col}")
                    self.grid[row][col]='H'

        else: 
            self.grid[1][1]='H'
            self.grid[1][3]='H'
            self.grid[2][3]='H'
            self.grid[3][0]='H'

    def possible_tiles_hole(self):
        # Function to see if the tiles with a hole i created are possible.
        for i in self.grid:
            # check rows
            if self.grid[i][0]!=' ' and self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == self.grid[i][3]:
                return False
            # check columns
            if self.grid[0][i]!=' ' and self.grid[1][i] == self.grid[2][i] == self.grid[3][i]:
                return False
            # check diagonals
        
        return True
            
    def display_board(self):
        for row in self.grid:
            print(row)

    def is_slippery(self,slippery):
        if slippery:
            pass
        else: 
            pass

    def set_move(self,row,col):
        pass


if __name__ == "__main__":
    environment = GridWorld()
    environment.display_board()
