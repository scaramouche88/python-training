from tabulate import tabulate
import numpy

####################################################################
# verify that the move is of 2 numbers, that it is in the board and
# that it do not erase an already occupied position
# in all cases it quits!
####################################################################

def valid_input(move,game):
 if len(move) != 2:
  print("Wrong format!")
  return False 
 for i in move:
  if i > 3:
   print("Out of the board!")
   return False
 x=move[0]
 y=move[1]
 if game[x-1][y-1] != 0:
  print("Wrong move! - I quit since my Master do not want to code this case...")
  print("(Everybody knows the rules of Tic-tac-toe!)")
  return False

###############################################
# function that prints the board game each time
###############################################
 
def display_board(table):
 graph_table=[(['-']*3) for i in range(3)]
 for i in [0,1,2]:
  for j in [0,1,2]:
   if table[i][j] == 1:
    graph_table[i][j] = "X"
   elif table[i][j] == 2:
    graph_table[i][j] = "O"
 print(tabulate(graph_table,tablefmt="fancy_grid"))

###############################################
# function that check for winners by line
###############################################
 
def check_line(game):
 for i in range(3):
  set_line=set(game[i])
  if len(set_line) == 1 and game[i][0] != 0:
   return 1
  return 0

###############################################
# function that check for winners by diagonal
###############################################
 
def check_diag(game):
 if game[1][1] != 0:
  diag1=set([game[0][0],game[1][1],game[2][2]])
  diag2=set([game[0][2],game[1][1],game[2][0]])
  if len(diag1) == 1 or len(diag2) == 1:
   return 1
  else:
   return 0
 else:
  return 0


###############################
# intro and printing the board
###############################

print("TIC-TAC-TOE")
print("")

board = [([0]*3) for i in range(3)]

display_board(board)

print("")
print("Player 1 is X and starts first, player 2 is O and starts second")
print("The move as given in the form of “row,col” - a number, then a comma, then a number")


##############################
# start to play
##############################

counter = 2

valid = True

winner = 0
win_list=[]

while counter <= 11:

 if counter % 2 == 0:

  print("PLAYER 1: give me you move!")

  move=list(input())
  move.remove(",")
  move=list(map(int, move))

  valid=valid_input(move,board)

  if valid == False:
   quit()

  board[move[0]-1][move[1]-1]=1

  display_board(board)

  trans = numpy.transpose(board)

  winner=check_line(board)
  win_list.append(winner)
  winner=check_line(trans)
  win_list.append(winner)
  winner=check_diag(board)
  win_list.append(winner)

  for el in win_list:
   if el == 1:
    print("WE HAVE A WINNER!:")
    print("Player 1 wins!")
    quit()

 else: 

  print("PLAYER 2: give me you move!")

  move=list(input())
  move.remove(",")
  move=list(map(int, move))

  valid=valid_input(move,board)

  if valid == False:
   quit()

  board[move[0]-1][move[1]-1]=2

  display_board(board)

  trans = numpy.transpose(board)

  winner=check_line(board)
  win_list.append(winner)
  winner=check_line(trans)
  win_list.append(winner)
  winner=check_diag(board)
  win_list.append(winner)

  for el in win_list:
   if el == 1:
    print("WE HAVE A WINNER!:")
    print("Player 2 wins!")
    quit()

 counter+=1

