class Game:
    '''Should this stuff stay as a class or become the main program?'''
    def __init__(self):
        self.player_color = ''
        self.computer_color = ''
        self.turn = ''
        self.pieces_on_board = []
        
        Game.select_color(self)
        
        # May Use elif, not else, to help avoid weird inputs
        if self.player_color == 'white':
            self.turn = 'player'
        elif self.computer_color == 'white':
            self.turn = 'computer'
            
    def __repr__(self):
        return f'''Playing as {self.player_color}.\nTurn: {self.turn}\nThere are
        {len(self.pieces_on_board)} pieces on the board.'''
        
    # TODO: Test what happens if there is a weird input
    def select_color(self):
        selected_color = input('Pick your color: white or black?\n')
        if selected_color.lower() == 'white':
            self.player_color, self.comupter_color = 'white', 'black'
        elif selected_color.lower() == 'black':
            self.player_color, self.comupter_color = 'black', 'white'
        else:
            return 'Input <white> or <black>.'
    
    # Algorithms for the computer to make a move
    def computer_move():
        pass
        # .....
        self.turn = 'player'
        self.between_moves()
        
    def player_move():
        pass
        #.........
        self.turn = 'computer'
        self.between_moves()

    def between_moves():
        self.in_check()
        #update_moves for all pieces in pieces_on_board
    
    # TODO: finish
    def in_check(self):
        # if square[king_black] in Queen_white.moves, Pawn1_white.moves, etc:
            # 
    
    # TODO: finish
    # Should this be merged with initializing squares in the Board class?
    #***** Maybe move this into the initialize board Board method
    #           b.white_q style objects******
    # Are these decent variable names?
    def initialize_pieces(self):
        white_rq = Rook('rook a1', 'white', 0)
        white_nq = Knight('knight b1', 'white', 1)
        white_bq = Bishop('bishop c1', 'white', 2)
        white_q = Queen('queen d1', 'white', 3)
        white_k = King('king e1', 'white', 4)
        white_bk = Bishop('bishop f1', 'white', 5)
        white_nk = Knight('knight g1', 'white', 6)
        white_rk = Rook('rook h1', 'white', 7)
        
        white_pa = Pawn('pawn a2', 'white', 8)
        white_pb = Pawn('pawn b2', 'white', 9)
        white_pc = Pawn('pawn c2', 'white', 10)
        white_pd = Pawn('pawn d2', 'white', 11)
        white_pe = Pawn('pawn e2', 'white', 12)
        white_pf = Pawn('pawn f2', 'white', 13)
        white_pg = Pawn('pawn g2', 'white', 14)
        white_ph = Pawn('pawn h2', 'white', 15)
        
        black_rq = Rook('rook a8', 'black', 56)
        black_nq = Knight('knight b8', 'black', 57)
        black_bq = Bishop('bishop c8', 'black', 58)
        black_q = Queen('queen d8', 'black', 59)
        black_k = King('king e8', 'black', 60)
        black_bk = Bishop('bishop f8', 'black', 61)
        black_nk = Knight('knight g8', 'black', 62)
        black_rk = Rook('rook h8', 'black', 63)
        
        black_pa = Pawn('pawn a7', 'black', 48)
        black_pb = Pawn('pawn b7', 'black', 49)
        black_pc = Pawn('pawn c7', 'black', 50)
        black_pd = Pawn('pawn d7', 'black', 51)
        black_pe = Pawn('pawn e7', 'black', 52)
        black_pf = Pawn('pawn f7', 'black', 53)
        black_pg = Pawn('pawn g7', 'black', 54)
        black_ph = Pawn('pawn h7', 'black', 55)
