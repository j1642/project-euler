class Board:
    '''Holds current board'''
    def __init__(self):
        self.squares = [' '] * 64
        self.squares_occ_white = []
        self.squares_occ_black = []
        
        self.a_file = [i * 8 for i in range(8)]
        self.b_file = [i * 8 + 1 for i in range(8)]
        self.c_file = [i * 8 + 2 for i in range(8)]
        self.d_file = [i * 8 + 3 for i in range(8)]
        self.e_file = [i * 8 + 4 for i in range(8)]
        self.f_file = [i * 8 + 5 for i in range(8)]
        self.g_file = [i * 8 + 6 for i in range(8)]
        self.h_file = [i * 8 + 7 for i in range(8)]

        self.rank_1 = [i for i in range(8)]
        self.rank_2 = [i for i in range(8, 16)]
        self.rank_3 = [i for i in range(16, 24)]
        self.rank_4 = [i for i in range(24, 32)]
        self.rank_5 = [i for i in range(32, 40)]
        self.rank_6 = [i for i in range(40, 48)]
        self.rank_7 = [i for i in range(48, 56)]
        self.rank_8 = [i for i in range(56, 64)]
    
    def __repr__(self):
        '''Shows the current board. Useful for feedback to user before GUI is made.'''
        
        ranks_to_print = []
        for factor in range(7, -1, -1):
            rank_x = ['|']
            for square in range(factor * 8, factor * 8 + 8):
                rank_x.append(self.squares[square])
                rank_x.append('|')
            ranks_to_print.append(''.join(rank_x))
        ls = '\n'.join(ranks_to_print)  # Looks nice using print( <board_object> )
        
        return ls
        
        
    def set_initial_squares(self):
        '''Sets up the board for a new game.'''
        
        rows1_2 = ['R','N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', 'P', 'P',
                  'P', 'P', 'P', 'P', 'P']

        for i in range(16):
            self.squares[i] = rows1_2[i]
        rows1_2.reverse()
        for i in range(48, 64):
            self.squares[i] = rows1_2[(i - 48)].lower()
        self.squares[60] = 'k'
        self.squares[59] = 'q'
    
    # TODO: Does not work
    # TODO: Compare move list for all pieces to the occupied lists to cull illegal moves
    def find_occupied_squares(self):
        '''Gets lists of squares occupited by white and black pieces, respectively.
        
        These lists are used to prevent a white piece moving to a square occupied 
        by another white piece, for example.'''
        
        for square in self.squares:
            if square.isupper():
                self.squares_occ_white.append(self.squares.index(square))
                #print(self.squares.index(square))
            elif square.islower():
                self.squares_occ_black.append(self.squares.index(square))
