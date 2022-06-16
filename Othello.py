
import check

## A Board is a (listof (listof Str))
## Requires:
##   The length of the outer list is 8.
##   The length of each inner list is 8.
##   Each string is '', 'B', or 'W'.

#Constants:
board = [[ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '', 'B', 'B', 'B',  '',  '',  ''],
         [ '', 'W', 'B', 'W', 'W',  '', 'B',  ''],
         [ '', 'W', 'B', 'W', 'W', 'W', 'W',  ''],
         [ '',  '', 'W', 'W', 'W',  '',  '',  ''],
         [ '',  '',  '', 'W',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  '']]
board2 = [[ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'B', 'W', 'B', 'W', 'W', 'W'],
          [ 'B', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
          [ 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
          [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]         
board3 = [[ 'W', 'W', 'B', 'B', 'B', 'B', 'B', 'B'],
          [ 'W', 'W', 'B', 'B', 'B', 'B', 'B', 'W'],
          [ 'W', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'W', '', 'W', 'W', 'W', 'W'],
          [ 'W', 'W', 'B', 'W', 'W', 'W', 'B', ''],
          [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]    
board4 = [[ 'W', 'W', 'B', 'B', 'B', 'B', 'B', 'B'],
          [ 'W', 'W', 'B', 'B', 'B', 'B', 'B', 'W'],
          [ 'W', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'W', '', 'W', 'W', 'W', 'W'],
          [ 'W', 'W', 'B', 'W', 'W', 'W', 'B', 'B'],
          [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]          
          
def vertical_line(board, col):
  '''
  Returns a new list which means the corresponding vertical line 
  in the column col by the given list board and the column col.
  
  vertical_line: (listof (listof Str)) Nat -> (listof Str)
  '''
  x = []
  for row in range(len(board)):
    x = x + [board[row][col]]
  return x
  
def diagonal_line(board, row, col):
  '''
  Returns the list which includes two corresponding diagonal lines by 
  the given list board, natural number row and col, representing
  the corresponding row and column in the board.
  
  diagonal_line: (listof (listof Str)) Nat Nat -> (listof Str)
  '''
  x = []
  x2 = []
  for r in range(len(board)):
    for c in range(len(board[r])):
      if r == row and c == col:
        x += [board[r][c]]
        x2 += [board[r][c]]
      elif (r - row) == (c - col):
        x += [board[r][c]]
      elif (r - row) == (col - c):
        x2 += [board[r][c]]
  return [x] + [x2]

def substitute(L, col):
  '''
  Returns a list which substitutes the element with 'spot' in the column col 
  of the list L by the given column col
  
  substitute: (listof Str) Nat -> (listof Str)
  '''
  x = []
  for pos in range(len(L)):
    if pos == col:
      x += ['spot']
    else:
      x += [L[pos]]
  return x

def substitute2(board, row, column):
  '''
  Returns a list which substitues the element with 'spot' in the row 'row' 
  and the column 'column' of the list board
  
  substitue2: (listof (listof Str)) Nat Nat -> (listof (listof Str))
  '''
  x = []
  for r in range(len(board)):
    if r != row:
      x += [board[r]]
    else:
      x += [substitute(board[r], column)]
  return x

def four_lines(board,row,col):
  '''
  Returns a list which contains four lists representing four lines 
  including the position that is in the row 'row' 
  and column col of the list board.
  
  four_lines: (listof (listof Str)) Nat Nat -> (listof (listof Str))
  '''
  new_board = substitute2(board, row, col)
  four_line = [new_board[row]] + [vertical_line(new_board, col)] + \
              diagonal_line(new_board,row,col)
  return four_line            
  
def break_lines(L):
  '''
  Returns the list which represents 8 different directions by 
  seperating all lists in the list L 
  by dividing each list into two parts. 
  Line1 is the part 1 of each list in L 
  and Line 2 is the part 2 of each list in L.
  '''
  x = []
  for pos1 in range(len(L)):
    for pos2 in range(len(L[pos1])):
      if L[pos1][pos2]== 'spot':
        line1 = L[pos1][:pos2]
        line2 = L[pos1][pos2+1:]
        line1.reverse()
        x = x + [line1] + [line2]
  return x

def eliminate(L):
  '''
  Returns the new list which eliminates all the empty list in the list L.
  
  eliminate: (listof (listof Str)) -> (listof (listof Str))
  ''' 
  x = []
  pos = 0
  while pos < len(L):
    if L[pos] == []:
      L.pop(pos)
    else:
      x += [L[pos]]
      pos += 1
  return x

def test(L, t):
  '''
  Returns a Bool by testing the list L. It returns true if 
  the list L is starting by not t which is 'B' or 'W' and not empty string, 
  and followed by t latter, returns False otherwise
  
  test: (listof (listof Str)) Str -> Bool
  
  Reqiures:
   1. turn which is one of 'B' or 'W'
   2. two parameters row and col, are natural numbers between 0 and 7 
   3. Assume the locations start with (0, 0) as the top left and 
      increasing down and to the right to the 
      bottom right corner at location (7, 7)  
  '''
  for pos1 in range(len(L)):
    if (L[pos1][0] != "") and (L[pos1][0] != t):
      for pos2 in range(len(L[pos1])):
        if (L[pos1][pos2] == t) and (L[pos1][pos2] != ""):
          return True
  return False
  
def othello(board, turn, row, col):
  '''
  Returns a Bool by the given list board, a string turn which is one of 
  'W' and 'B', row of the board 'row', and column col of the board. 
  It returns True if the position(board[row][col]) 
  is the valid place to go, False otherwise.
  
  othello: (listof (listof Str)) Str Nat Nat -> Bool
  
  Reqiures:
   1. turn which is one of 'B' or 'W'
   2. two parameters row and col, are natural numbers between 0 and 7 
   3. Assume the locations start with (0, 0) as the top left and 
      increasing down and to the right to the 
      bottom right corner at location (7, 7)  
  
  Examples:
    othello(board, 'B', 3, 0) => True
    othello(board, 'W', 3, 0) => False
    othello(board2, 'W', 1, 2) => False  
  '''
  if board[row][col] == '':
    all_lines = four_lines(board, row, col)
    all_direction = break_lines(all_lines)
    L = eliminate(all_direction)
    return test(L, turn)
  else:
    return False

#Examples:
check.expect('Example1',othello(board, 'B', 3, 0),True)
check.expect('Example2',othello(board, 'W', 3, 0),False)
check.expect('Example3',othello(board2, 'W', 1, 2),False)
#Tests
check.expect('all empty around the position', \
            othello(board, 'B', 0, 0), False)
check.expect('board[row][col]!='', position has already been taken', \
            othello(board, 'W', 4, 7),False)
check.expect('False case', othello(board3, 'B', 1, 3),False)            
check.expect('True case',othello(board3, 'W', 4, 7),True)            
check.expect('True case',othello(board3, 'W', 4, 7),True)
check.expect('True case',othello(board3, 'W', 4, 7),True)
check.expect('True case',othello(board3, 'B', 4, 7),True)
check.expect('True case',othello(board4, 'B', 3, 3),True)
