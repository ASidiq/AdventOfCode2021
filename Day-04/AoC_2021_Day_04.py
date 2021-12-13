import numpy as np
#import copy

class AdventOfCodeDayFour():

    def __init__(self, numbers, boards):
        self.numbers = [int(x) for x in numbers.split(",")]
        self.boards = boards
        self.boards_won = []

    def boards_remove_spaces(self):
        self.boards = [x.split(" ") for x in boards.split("\n") if x != ""]
        for index, value in enumerate(self.boards):
            self.boards[index] = [int(x) for x in self.boards[index] if x != "" ]

    def shape_boards(self):
        self.boards = np.array(self.boards).reshape(100,5,5)
        #self.boards = np.array(self.boards).reshape(3,5,5)
        #print([self.boards.shape, self.boards.ndim, self.boards.dtype.name, self.boards.itemsize, self.boards.size])
    
    def tracker_boards(self):
        self.tracker_boards = np.zeros((100, 5, 5), dtype=np.int16)
        #self.tracker_boards = np.zeros((3, 5, 5), dtype=np.int16)

    def check_row(self, board):
        win_row = np.sum(board, axis=1)
        return np.where(win_row==5)

    def check_column(self, board):
        win_column = np.sum(board, axis=0)
        return np.where(win_column==5)
        
    def game(self):
        for x in self.numbers:
            result = self.play_number(x)
            if result:
                winning_board = result[0]
                tracking_board = result[1]
                position_zero_values = np.where(tracking_board==0)
                location = list(zip(position_zero_values[0], position_zero_values[1]))
                values = [winning_board[x][y] for (x,y) in location ]
                return sum(values) * x

    def game2(self):
        winning_board = None
        tracking_board = None
        final_number = None
        for x in self.numbers:
            result = self.play_number_v2(x)
            if result:
                winning_board = result[0]
                tracking_board = result[1]
                final_number = result[2]
        position_zero_values = np.where(tracking_board==0)
        location = list(zip(position_zero_values[0], position_zero_values[1]))
        values = [winning_board[x][y] for (x,y) in location ]
        return sum(values) * final_number

    
    def play_number(self, value):
        for index, board in enumerate(self.boards):
            positions = np.where(board==value)
            if positions[0].size == 0:
                continue
            coordinates = list(zip(positions[0], positions[1]))
            self.update_tracker(index, coordinates)
            row_result = self.check_row(self.tracker_boards[index])
            column_result = self.check_column(self.tracker_boards[index])

            if row_result[0].size != 0:
                tracker = self.tracker_boards[index]
                return (board, tracker, value)

            if column_result[0].size != 0:
                tracker = self.tracker_boards[index]
                return (board, tracker, value)

    def play_number_v2(self, value):
        wins = []
        for index, board in enumerate(self.boards):
            if index in self.boards_won:
                continue
            positions = np.where(board==value)
            if positions[0].size == 0:
                continue
            coordinates = list(zip(positions[0], positions[1]))
            self.update_tracker(index, coordinates)
            row_result = self.check_row(self.tracker_boards[index])
            column_result = self.check_column(self.tracker_boards[index])

            if row_result[0].size != 0:
                tracker = self.tracker_boards[index]
                self.boards_won.append(index)
                wins.append((board, tracker, value))

            if column_result[0].size != 0:
                tracker = self.tracker_boards[index]
                self.boards_won.append(index)
                wins.append((board, tracker, value))

        if len(wins) > 0:
            win_info = wins[-1]
            return (win_info[0], win_info[1], win_info[2])
        

    def update_tracker(self, board_position, coordinates):
        for (x,y) in coordinates:
            current_board = self.tracker_boards[board_position]
            current_board[x][y] = 1


            
 
if "__main__"==__name__:

    numbers = None
    boards = None

    with open(file="./Numbers.txt",mode='r') as numbers_input:
        numbers = numbers_input.read()
    
    with open(file="./Boards.txt",mode='r') as boards_input:
        boards = boards_input.read()
 
    problem = AdventOfCodeDayFour(numbers, boards)
    problem.boards_remove_spaces()
    problem.shape_boards()
    problem.tracker_boards()
    print(problem.game())
    print(problem.game2())