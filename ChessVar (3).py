
# Author: Matthew Holmstrom
# GitHub username: matthewholmstrom
# Date: 12/6/2023
# Description: This program creates a ChessVar class, which is used for playing a variant of the game chess.
# The program allows two players to play the game. In this game, each of the chess pieces moves and captures
# the same way it does in regular chess, except that there is no castling, en passant, or pawn promotion.
# The winner of the game is the first player to capture all the opponent's pieces of one type. For example,
# a player would win the game if they captured the opponent's two rooks, 1 king, or 8 pawns. As in
# standard chess, the two players are black and white. The starting position is the same as in standard chess,
# and the white player moves first.


class ChessVar:
    """A class representing a ChassVar variable. The Chessvar class contains methods for creating
    a chessboard, and implementing a variation of the game of chess. In this variation of chess, the winner
    is (black or white) the player who captures all opponent's pieces of one type. For example capturing
    the opponents 1 king or 8 pawns. The ChessVar class keeps track of which player's turn it is and the number (of each type)
    of pieces that have been captured for both players. One of ChessVar class's methods (make_move) is a method which allows the
    current player to try and move their chosen piece, from a starting square to an ending square, if the move
    is a valid move."""
    def __init__(self):
        """A method that takes no parameters, and initializes data members of the ChessVar
        object. The initialized data members include the game board, the current player,
        the turn count of each player, and the count of each player's pieces that have been captured."""
        self.__game_board = [
            ['r','n','b','q','k','b','n','r'], # The white pieces are lower case and the black pieces are upper cased.
            ['p','p','p','p','p','p','p','p'], # - signs represent vacant squares.
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']
        ]

        self.__current_player = 'White'
        self.__game_state = 'UNFINISHED'
        self.__white_turn_count = 0
        self.__black_turn_count = 0

        self.__w_pawn_count = 0
        self.__w_bishop_count = 0
        self.__w_rook_count = 0
        self.__w_queen_count = 0
        self.__w_king_count = 0
        self.__w_knight_count = 0

        self.__b_pawn_count = 0
        self.__b_bishop_count = 0
        self.__b_rook_count = 0
        self.__b_queen_count = 0
        self.__b_king_count = 0
        self.__b_knight_count = 0



    def get_game_state(self):
        """Takes no parameters and returns the game_state data member, which is
        the data member representing the current state of the game (either UNFINISHED, WHITE_WON,
        or  BLACK_WON.)"""
        return self.__game_state

    def get_game_board(self):
        """Takes no parameters and returns the game_board data member."""

        return self.__game_board

    def print_game_board(self):
        """Takes no parameters and prints out the chessboard."""

        for row in (self.__game_board):
            for i in row:
                print(i, end = ' ')
            print(' ', sep = '\n')

    def get_w_pawn_count(self):
        """Takes no parameters and returns the w_pawn data member."""
        return self.__w_pawn_count

    def get_b_pawn_count(self):
        """Takes no parameters and returns the b_pawn data member."""
        return self.__b_pawn_count

    def get_current_player(self):
        """Takes no parameters and returns the current_player data member."""
        return self.__current_player


    def make_move(self, start_square, end_square):
        """Takes as parameters the start_square and end_square, which are string variables containing
        the algebraic notation for the squares that the current player wants their piece to move from and
        to. The make_move method returns false if the square being moved from does not contain a piece
        belonging to the player whose turn it is, or if the indicated move is not legal, or if the
        game has already been won. Otherwise, the method makes the indicated move, removes any captured piece,
        updates the game state if necessary, update whose turn it is, and return True."""

        if self.__game_state == 'WHITE_WON' or self.__game_state == 'BLACK_WON': # The game has already been won so make_move returns false.
            return False

        start_row, start_col = self.convert_to_indices(start_square) # Gets the list indices corresponding to the algebraic notation of the square.
        end_row, end_col = self.convert_to_indices(end_square)


        game_piece = self.__game_board[start_row][start_col] # Gets the game piece of the starting square

        if not self.is_in_game_board(start_row, start_col) or not self.is_in_game_board(end_row, end_col): # Checks to see if the squares are in the game board.
            return False


        if game_piece == '-': # The starting square contains none of the player's pieces.
            return False
        if game_piece.isupper() and self.__current_player == 'White': # The white player is attempting to move the black player's piece
            return False
        if game_piece.islower() and self.__current_player == 'Black': # The black player is attempting to move the white player's piece
            return False


        if self.is_valid_move(start_row, start_col, end_row, end_col): # Checks to see if the intended move is a legal move.
            self.__game_board[end_row][end_col]= self.__game_board[start_row][start_col]
            self.__game_board[start_row][start_col] = '-'


            self.update_game_state()

            if self.__current_player == 'White':
                self.update_white_turn_count() # Updates the number of turns the white player has made
                self.__current_player = 'Black'
            else:
                self.update_black_turn_count()
                self.__current_player = 'White'

            return True # The move is valid

        return False # The move is not valid
    def convert_to_indices(self, square):
        """Takes as parameters a square of the chessboard in algebraic notation. The method
        converts the algebraic notation of the game board square into list indices of the game board.
        The method returns the row and column in the game board corresponding to the algebraic notation of the
        game board square from the parameter."""
        row = int(square[1]) - 1
        col = ord(square[0]) - ord('a')

        return row, col

    def is_in_game_board(self, row, col):
        """Takes as parameters the row and column indices of a game board square
        and returns true if row and column indices are within the game board's valid
        indices."""
        return 0 <= row < 8 and 0 <= col < 8


    def is_valid_move(self, start_row, start_col, end_row, end_col):
        """Takes as parameters the row and column of the starting square and the ending square.
        The method gets the game piece corresponding to the row and column of the starting square.
        The method then determines what type of chess piece the game piece is and determines if the
        type of chess piece can make a valid move from the starting square to the ending square. If the
        type of chess piece is able to move from the starting square to the ending square, then the method
        returns True. It returns false if otherwise. The method also determines if the move captures the opponent's
        piece. If so, the method calls the update_captured_piece method, and passes to it the captured piece.
        """

        game_piece = self.__game_board[start_row][start_col]
        if game_piece == '-' : # The game piece contains none of the current player's pieces
            return False

        if game_piece == 'p': # The game piece is a white pawn

            # The pawn can move up two squares if it's the players first turn
            if end_row - start_row == 2 and start_row == 1 and \
                    self.__game_board[end_row][end_col] == '-' and start_col == end_col:

                return True


            possible_end_squares = [] # list of possible ending squares

            if self.__game_board[start_row + 1][start_col] == '-': # Checking if the row in front of the start row equals '-'
                dest_end_row = start_row + 1
                dest_end_col = start_col
                dest_tuple1 = (dest_end_row, dest_end_col)
                possible_end_squares.append(dest_tuple1) # Adding this square to the possible ending squares

                if self.__game_board[start_row + 2][start_col] == '-' and start_row == '1': # Moving up two square is possible on player's first turn
                    dest_tuple3 = (start_row + 2, start_col)
                    possible_end_squares.append(dest_tuple3) # Adding this square to the possible ending squares

            if start_col - 1 >= 0 and start_row + 1 <= 7: # Capturing diagonally on the left is possible for the Pawn
                ending_piece = self.__game_board[start_row + 1][start_col - 1]

                if ending_piece.isupper(): # Checking if the ending piece belongs to the other player, if so the ending square is valid.
                    dest_tuple4 = (start_row + 1, start_col - 1)
                    possible_end_squares.append(dest_tuple4) # Adding this square to the possible ending squares.

            if start_col + 1 <= 7 and start_row + 1 <= 7: # Capturing diagonally on the right is possible for the pawn.
                ending_piece2 = self.__game_board[start_row + 1][start_col + 1]

                if ending_piece2.isupper(): # Checking if the  ending piece belongs to the other player.
                    dest_tuple5 = (start_row + 1, start_col + 1)
                    possible_end_squares.append(dest_tuple5)


            end_destination = (end_row, end_col)
            if end_destination not in possible_end_squares:
                return False

            # Capturing the opponent's piece
            if abs(end_col - start_col) == 1 and end_row - start_row == 1 and self.__game_board[end_row][end_col] != '-' :

                if self.__game_board[end_row][end_col].isupper():
                    captured_piece = self.__game_board[end_row][ end_col]
                    self.update_captured_piece(captured_piece)
                else:
                    return False
                return True

                # The pawn can only move up one square, on any turn other than its first turn
            if end_row - start_row == 1 and self.__game_board[end_row][end_col] == '-':
                return True
            if start_col != end_col: # The pawn can't move sideways
                return False


        if game_piece == 'P': # The game piece is a black pawn

            possible_end_squares = []

            # The pawn can move down two squares if it's the players first turn
            if end_row - start_row == -2 and start_row == 6 and  \
                    self.__game_board[end_row][end_col] == '-' and start_col == end_col:

                return True

            if self.__game_board[start_row-1][start_col] == '-': # Checking if the row below the start row equals '-', if so we add it to possible landing squares.
                dest_end_row = start_row -1
                dest_end_col = start_col
                dest_tuple1 = (dest_end_row,dest_end_col)
                possible_end_squares.append(dest_tuple1) # Adding the square to the possible landing squares.

                if self.__game_board[start_row -2][start_col] == '-' and start_row == '6': # The square two squares below is a possible landing square on the player's first move.
                    dest_tuple3 = (start_row -2, start_col)
                    possible_end_squares.append(dest_tuple3)


            if start_col-1 >=0 and start_row -1 >=0: # Checking if there is a left capture, if so that ending square is a possible landing square.
                ending_piece = self.__game_board[start_row-1][start_col-1]

                if ending_piece.islower() :
                    dest_tuple4 = (start_row-1,start_col-1)
                    possible_end_squares.append(dest_tuple4)


            if start_col+1 <=7 and start_row -1 >=0: # Checking if there is a right capture, if so that ending square is a possible landing square.
                ending_piece2 = self.__game_board[start_row-1][start_col+1]

                if ending_piece2.islower() :
                    dest_tuple5 = (start_row-1,start_col+1)
                    possible_end_squares.append(dest_tuple5)


            end_destination = (end_row, end_col)
            if end_destination not in possible_end_squares:
                return False


            # The pawn can only move up one square, on any turn other than its first turn
            if end_row - start_row == -1 and self.__game_board[end_row][end_col] == '-':
                return True

            # Capturing the piece
            if abs(end_col - start_col) == 1 and end_row - start_row == -1 and self.__game_board[end_row][end_col] != '-' :

                if self.__game_board[end_row][end_col].islower():
                    captured_piece = self.__game_board[end_row][ end_col]
                    self.update_captured_piece(captured_piece)
                else:
                    return False
                return True
            if start_col != end_col:
                return False

        if game_piece == 'r':  # The game piece is a rook.

            if start_row == end_row or start_col == end_col:  # The rook can move forwards, backwards, and side to side, but can't move diagonally.
                possible_end_squares = []
                courses = ((-1, 0), (1, 0), (0, -1), (0, 1))
                for c in courses:
                    for j in range(1, 8):
                        dest_end_row =  c[0] * j + start_row
                        dest_end_col =  c[1] * j + start_col
                        dest_tuple = (dest_end_row, dest_end_col)
                        if 0 <= dest_end_row < 8 and 0 <= dest_end_col < 8:
                            ending_piece = self.__game_board[dest_end_row][dest_end_col]
                            if ending_piece == '-':
                                possible_end_squares.append(dest_tuple)
                            elif ending_piece[0].isupper():
                                possible_end_squares.append(dest_tuple)
                                break
                            else:
                                break
                        else:
                            break

                end_destination = (end_row, end_col)
                if end_destination not in possible_end_squares:
                    return False

                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].isupper():
                        captured_piece = self.__game_board[end_row][end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True

        if game_piece == 'R':  # The game piece is a rook.

            if start_row == end_row or start_col == end_col:  # The rook can move forwards, backwards, and side to side, but can't move diagonally.
                possible_end_squares = []
                courses = ((-1, 0), (1, 0), (0, -1), (0, 1))
                for c in courses:
                    for j in range(1, 8):
                        dest_end_row =  c[0] * j + start_row
                        dest_end_col =  c[1] * j + start_col
                        dest_tuple = (dest_end_row, dest_end_col)
                        if 0 <= dest_end_row < 8 and 0 <= dest_end_col < 8:
                            ending_piece = self.__game_board[dest_end_row][dest_end_col]
                            if ending_piece == '-':
                                possible_end_squares.append(dest_tuple)
                            elif ending_piece[0].islower():
                                possible_end_squares.append(dest_tuple)
                                break
                            else:
                                break
                        else:
                            break

                end_destination = (end_row, end_col)
                if end_destination not in possible_end_squares:
                    return False

                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].islower():
                        captured_piece = self.__game_board[end_row][end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True


        # The knight moves in an L shape, first 2 squares in one direction, and the one square in another direction.
        if game_piece == 'n': # The game piece is a knight
            if (abs(end_col - start_col) == 1 and abs(end_row - start_row) == 2) or \
                        (abs(end_row - start_row)==1 and abs(end_col- start_col)==2):

                if self.__game_board[end_row][end_col] != '-':

                    if self.__game_board[end_row][end_col].isupper():
                        captured_piece = self.__game_board[end_row][ end_col]
                        self.update_captured_piece(captured_piece)

                    else:
                        return False
                return True

        if game_piece == 'N':  # The game piece is a knight
            if (abs(end_col - start_col) == 1 and abs(end_row - start_row) == 2) or \
                    (abs(end_row - start_row) == 1 and abs(end_col - start_col) == 2):

                if self.__game_board[end_row][end_col] != '-':

                    if self.__game_board[end_row][end_col].islower():
                        captured_piece = self.__game_board[end_row][ end_col]
                        self.update_captured_piece(captured_piece)

                    else:
                        return False
                return True
        # Bishops move diagonally in any direction, and can move as many squares diagonally as is desired.
        if game_piece == 'b': # The game piece is a bishop.
            if abs(end_row - start_row) == abs(end_col - start_col):

                possible_end_squares = []
                courses = ((-1, -1), (1, 1), (1, -1), (-1, 1))
                for c in courses:
                    for j in range(1, 8):
                        dest_end_row =  c[0] * j + start_row
                        dest_end_col =  c[1] * j + start_col
                        dest_tuple = (dest_end_row, dest_end_col)
                        if 0 <= dest_end_row < 8 and 0 <= dest_end_col < 8:
                            ending_piece = self.__game_board[dest_end_row][dest_end_col]
                            if ending_piece == '-':
                                possible_end_squares.append(dest_tuple)
                            elif ending_piece[0].isupper():
                                possible_end_squares.append(dest_tuple)
                                break
                            else:
                                break
                        else:
                            break

                end_destination = (end_row, end_col)
                if end_destination not in possible_end_squares:
                    return False


                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].isupper():
                        captured_piece = self.__game_board[end_row][ end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True

        if game_piece == 'B':  # The game piece is a bishop.

            if abs(end_row - start_row) == abs(end_col - start_col):

                possible_end_squares = []
                courses = ((-1, -1), (1, 1), (1, -1), (-1, 1))
                for c in courses:
                    for j in range(1, 8):
                        dest_end_row =  c[0] * j + start_row
                        dest_end_col =  c[1] * j + start_col
                        dest_tuple = (dest_end_row, dest_end_col)
                        if 0 <= dest_end_row < 8 and 0 <= dest_end_col < 8:
                            ending_piece = self.__game_board[dest_end_row][dest_end_col]
                            if ending_piece == '-':
                                possible_end_squares.append(dest_tuple)
                            elif ending_piece[0].islower():
                                possible_end_squares.append(dest_tuple)
                                break
                            else:
                                break
                        else:
                            break

                end_destination = (end_row, end_col)
                if end_destination not in possible_end_squares:
                    return False

                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].islower():
                        captured_piece = self.__game_board[end_row][ end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True

        # The queen can move forward, down, side to side, and diagonally any direction, as many squares as desired.
        if game_piece == 'q': # The game piece is a queen.
            if (abs(end_row - start_row) == abs(end_col - start_col) or
                        end_col == start_col or end_row == start_row):

                possbile_end_squares = []
                courses = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (-1,1), (1,1), (1, -1))
                for c in courses:
                    for j in range(1, 8):
                        dest_end_row =  c[0] * j + start_row
                        dest_end_col =  c[1] * j + start_col
                        dest_tuple = (dest_end_row, dest_end_col)
                        if 0 <= dest_end_row < 8 and 0 <= dest_end_col < 8:
                            ending_piece = self.__game_board[dest_end_row][dest_end_col]
                            if ending_piece == '-':
                                possbile_end_squares.append(dest_tuple)
                            elif ending_piece[0].isupper():
                                possbile_end_squares.append(dest_tuple)
                                break
                            else:
                                break
                        else:
                            break

                end_destination = (end_row, end_col)
                if end_destination not in possbile_end_squares:
                    return False



                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].isupper():
                        captured_piece = self.__game_board[end_row][ end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True

        if game_piece == 'Q':  # The game piece is a queen.
            if (abs(end_row - start_row) == abs(end_col - start_col) or
                    end_col == start_col or end_row == start_row):


                possible_end_squares = []
                courses = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (-1,1), (1,1), (1, -1))
                for c in courses:
                    for j in range(1, 8):
                        dest_end_row =  c[0] * j + start_row
                        dest_end_col =  c[1] * j + start_col
                        dest_tuple = (dest_end_row, dest_end_col)
                        if 0 <= dest_end_row < 8 and 0 <= dest_end_col < 8:
                            ending_piece = self.__game_board[dest_end_row][dest_end_col]
                            if ending_piece == '-':
                                possible_end_squares.append(dest_tuple)
                            elif ending_piece[0].islower():
                                possible_end_squares.append(dest_tuple)
                                break
                            else:
                                break
                        else:
                            break

                end_destination = (end_row, end_col)
                if end_destination not in possible_end_squares:
                    return False



                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].islower():
                        captured_piece = self.__game_board[end_row][ end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True

        # The king moves one square, and either forwards, backwards, side to side, or diagonally in any direction.
        if game_piece == 'k': # The game piece is a king.
            if abs(end_row - start_row) <=1 and abs(end_col - start_col)<=1 :
                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].isupper():
                        captured_piece = self.__game_board[end_row][ end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True

        if game_piece == 'K': # The game piece is a king.
            if abs(end_row - start_row) <=1 and abs(end_col - start_col)<=1 :
                if self.__game_board[end_row][end_col] != '-':
                    if self.__game_board[end_row][end_col].islower():
                        captured_piece = self.__game_board[end_row][end_col]
                        self.update_captured_piece(captured_piece)
                    else:
                        return False
                return True

        return False # The game piece cannot make the desired move

    def update_white_turn_count(self):
        """Takes no parameters and updates the number of turns that the white player has moved."""
        self.__white_turn_count +=1

    def update_black_turn_count(self):
        """Takes no parameters and updates the number of turns that the black player has moved."""
        self.__black_turn_count +=1

    def update_game_state(self):
        """Takes no parameters and updates the state of the game. The player wins if the count of an
        opponent's piece is the number of total pieces of that type that the opponent has. For example
        if the white pawn count = 8 or the white bishop count = 2, then the black player wins.
        The method also updates the game_state data member to reflect the outcome of the game.
        ."""
        if  self.__w_pawn_count == 8 or self.__w_bishop_count == 2:
            self.__game_state = 'BLACK_WON'
        if  self.__w_rook_count == 2 or self.__w_queen_count == 1:
            self.__game_state = 'BLACK_WON'
        if  self.__w_king_count == 1 or self.__w_knight_count == 2:
            self.__game_state = 'BLACK_WON'


        if  self.__b_pawn_count == 8 or self.__b_bishop_count == 2:
            self.__game_state = 'WHITE_WON'
        if  self.__b_rook_count == 2 or self.__b_queen_count == 1:
            self.__game_state = 'WHITE_WON'
        if  self.__b_king_count == 1 or self.__b_knight_count == 2:
            self.__game_state = 'WHITE_WON'
        return

    def update_captured_piece(self, captured_piece):
        """Takes as parameters the type of opponent's piece the current player has captured.
        The method checks what type of piece was captured and updates the count of the
        opponent's piece of that type that was captured. For example, if the captured piece
        is a black pawn, then the black pawn count is incremented by 1.
        """
        if captured_piece == 'P':
            self.__b_pawn_count +=1
        if captured_piece == 'R':
            self.__b_rook_count +=1
        if captured_piece == 'K':
            self.__b_king_count += 1
        if captured_piece == 'B':
            self.__b_bishop_count += 1
        if captured_piece == 'Q':
            self.__b_queen_count +=1
        if captured_piece == 'N':
            self.__b_knight_count +=1


        if captured_piece == 'p':
            self.__w_pawn_count += 1
        if captured_piece == 'r':
            self.__w_rook_count += 1
        if captured_piece == 'k':
            self.__w_king_count += 1
        if captured_piece == 'b':
            self.__w_bishop_count += 1
        if captured_piece == 'q':
            self.__w_queen_count += 1
        if captured_piece == 'n':
            self.__w_knight_count += 1

        return



#Testing the code
#game = ChessVar()

#move_result = game.make_move('a2', 'a4')
#game.make_move('g1', 'f1')
#state = game.get_game_state()


#print(state)

#game.print_game_board()

#print()

#print(game.get_game_board()[1][1])
#print(game.get_game_board()[7][2])

#print()
#print(game.print_game_board())










