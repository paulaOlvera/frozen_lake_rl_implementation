import numpy as np

class GridWorld:
    def __init__(self,random):
        self.grid = [['P',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','G']]
        # self.is_slippery = False
        self.goal_position = (3,3)
        self.random = random
        self.create_frozen_tiles(self.random)
        
    def create_frozen_tiles(self,random):
        
        if random:
            while True:
                count = 0
                while count<4:
                    row = np.random.randint(0,4)
                    col = np.random.randint(0,4)
                    if self.grid[row][col]==' ':
                        count+=1
                        # print(f"row {row} and col {col}")
                        self.grid[row][col]='H'
                # self.render()
                if self.possible_tiles_hole():
                    break
                else:
                    self.grid = [['P',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','G']]
        

        else: 
            self.grid[1][1]='H'
            self.grid[1][3]='H'
            self.grid[2][3]='H'
            self.grid[3][0]='H'

    def possible_tiles_hole(self):
        # Function to see if i can reach the goal from the start point. 
        to_visit_cells = []
        visited_cells = []

        start_position = (0,0)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        to_visit_cells.append(start_position)
        visited_cells.append(to_visit_cells[0])
        while to_visit_cells:
            current_cell = to_visit_cells.pop(0)
            for possible_direction in directions:
                
                new_cell = (current_cell[0]+possible_direction[0],current_cell[1]+possible_direction[1])
                if 0<=new_cell[0]<4 and 0<=new_cell[1]<4 and self.grid[new_cell[0]][new_cell[1]]!='H':
                    count = 0
                    if new_cell not in visited_cells:
                        to_visit_cells.append(new_cell)
                        
                    if self.grid[new_cell[0]][new_cell[1]]=='G':
                        return True
                
            visited_cells.append(current_cell)
        return False
            
    def render(self):
        for row in self.grid:
            print(row)

    def is_slippery(self,slippery):
        if slippery:
            pass
        else: 
            pass

    def reset(self):
        self.grid = [['P',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ','G']]
        self.create_frozen_tiles(self.random)

    def step(self,action):
        moves = [
            (-1,0), # move up
            (1,0),  # move down
            (0,-1), # move left
            (0,1)  # move right
        ]
        move = moves[action]
        current_step = self.get_state()
        next_possible_step = (current_step[0]+move[0],current_step[1]+move[1])
        # check if this next_possible_step is not outside the gridworld.
        if 0<=next_possible_step[0]<4 and 0<=next_possible_step[1]<4:
            next_step = next_possible_step
            if next_step == self.goal_position: # goal position
                self.grid[current_step[0]][current_step[1]]=' '
                self.grid[next_step[0]][next_step[1]]='P'
                reward=1
                done=True
            elif self.grid[next_step[0]][next_step[1]]=='H':
                reward = -1 # the next step has fall in a hole tile. 
                done =True
            else:
                self.grid[current_step[0]][current_step[1]]=' '
                self.grid[next_step[0]][next_step[1]]='P'
                reward = 0
                done = False

        else:
            next_step =current_step
            reward = -0.1
            done = False
        
        return next_step, reward, done

    def get_state(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col]=='P':
                    state = (row,col)
                    return state

        


        
         


