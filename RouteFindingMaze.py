class Maze:
    def __init__(self, start_row, start_col, end_row, end_col):
        # self.maze_dict = {'S': 0, 'G': -2, 'B': -1, 'X': -9}

        self.maze = [['X', 'X', 'X', 'X', 'X', 'G', 'X', 'X'],
                     ['X', 'B', 'B', 'B', 'B', 'B', 'B', 'X'],
                     ['X', 'B', 'X', 'X', 'X', 'X', 'B', 'X'],
                     ['X', 'B', 'X', '0', 'X', 'B', 'B', 'X'],
                     ['X', 'B', 'X', 'B', 'X', 'X', 'B', 'X'],
                     ['X', 'B', 'X', 'B', 'X', 'B', 'B', 'X'],
                     ['X', 'B', 'B', 'B', 'B', 'B', 'B', 'X'],
                     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

        # self.maze = [[-1, -1, -1, -1, -1, -9, -1, -1],
        #              [-1,  0,  0,  0,  0,  0,  0, -1],
        #              [-1,  0, -1, -1, -1, -1,  0, -1],
        #              [-1,  0, -1, -5, -1,  0,  0, -1],
        #              [-1,  0, -1,  0, -1, -1,  0, -1],
        #              [-1,  0, -1,  0, -1,  0,  0, -1],
        #              [-1,  0,  0,  0,  0,  0,  0, -1],
        #              [-1, -1, -1, -1, -1, -1, -1, -1]]

    def find_shortest_path(self, row, col):
        step = 0
        while True:
            for i in range(8):
                for j in range(8):
                    # dict_key = str(self.maze[i][j])
                    if self.maze[i][j] == str(step):
                        row = i
                        col = j
                        # move nortth
                        row -= 1
                        if row > -1:
                            if self.maze[row][col] == 'B':
                                self.maze[row][col] = str(step + 1)
                            elif self.maze[row][col] == 'G':
                                return

                        row = i
                        # move south
                        row += 1
                        if row < 8:
                            if self.maze[row][col] == 'B':
                                self.maze[row][col] = str(step + 1)
                            elif self.maze[row][col] == 'G':
                                return

                        row = i
                        # move east
                        col += 1
                        if col < 8:
                            if self.maze[row][col] == 'B':
                                self.maze[row][col] = str(step + 1)
                            elif self.maze[row][col] == 'G':
                                return

                        col = j
                        # move west
                        col -= 1
                        if col > -1:
                            if self.maze[row][col] == 'B':
                                self.maze[row][col] = str(step + 1)
                            elif self.maze[row][col] == 'G':
                                return
            step += 1

    def print_maze(self):
        for i in range(8):
            print(' ')
            for j in range(8):
                if self.maze[i][j] == 'B':
                    print('    ', end=' ')
                else:
                    print(self.maze[i][j] + '   ', end=' ')


m = Maze(3, 3, 0, 5)
m.print_maze()
m.find_shortest_path(3, 3)
print(' ')
m.print_maze()
