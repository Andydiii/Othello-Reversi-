# Othello-Reversi in Python
Othello (or Reversi) is a two player game played on an 8 by 8 board where players alternate by placing a white or black disc onto the playing field and flipping over colours of the opposing player. The object of the game is to end up with the most pieces in your colour. You can find a version of the game to play against a computer player here: https://cardgames.io/reversi/.

We are concerned about valid moves. If you are playing White, a valid move is the placement of a White disc on an empty square that forms a sequence of at least three adjacent discs (either horizontal, vertical or diagonal) where only the first and last disc is White. If you are playing Black, a valid move is the placement of a Black disc on an empty square that forms a sequence of at least three adjacent discs (either horizontal, vertical or diagonal) where only the first and last disc is Black. Consider the board below where it is Black's turn. They have 13 possible places to move as indicated by the faded circles. Notice in each spot, if a Black piece is placed, it will form a sequence consisting of a Black piece, at least one White piece, and another Black piece (perhaps in multiple directions).

othello(board, turn, row, col) is the function 
         
that consumes a board of type Board , turn which is one of 'B' or 'W' and two parameters row and col, natural numbers between 0 and 7 inclusive, which represents the square location in the Board where we are trying to put a piece and returns True if the piece of colour turn can be played at the given location as a valid move and False otherwise. Assume the locations start with (0, 0) as the top left and increasing down and to the right to the bottom right corner at location (7, 7).

Sample:

board = [[ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '', 'B', 'B', 'B',  '',  '',  ''],
         [ '', 'W', 'B', 'W', 'W',  '', 'B',  ''],
         [ '', 'W', 'B', 'W', 'W', 'W', 'W',  ''],
         [ '',  '', 'W', 'W', 'W',  '',  '',  ''],
         [ '',  '',  '', 'W',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  '']]
othello(board, 'B', 3, 0) => True
othello(board, 'W', 3, 0) => False

board2 = [[ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'B', 'W', 'B', 'W', 'W', 'W'],
          [ 'B', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
          [ 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
          [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]
othello(board2, 'W', 1, 2) => False
