import random
import os
import time

def random_state(height: int, width: int):
  """
  Function takes in 2 args (height and width) and returns a board_state (list) in which every cell has been randomly 
  initalized to either alive (1) or dead (0).  These boards are known as 'soups'
  """
  random_board = []
  for _ in range(height):
    sub = []
    for _ in range(width):
      sub.append(random.randint(0,1))
    random_board.append(sub)
  return random_board
      
def dead_state(height: int, width: int):
  #same as random_state only initializes to completely dead
  dead_board = []
  for _ in range(height):
    sub = []
    for _ in range(width):
      sub.append(0)
    dead_board.append(sub)
  return dead_board

def next_board_state(board: list):
  #determine width/height of board to set up nexted loop
  next_board_height = len(board)
  next_board_width = len(board[0])
  #generate a dead_state board to build new state from
  next_board = dead_state(next_board_height, next_board_width)
  #build nested loop to analyze board
  for i in range(next_board_height):
    for j in range(next_board_width):
      neighbors = walk_and_tally(board, next_board_height, next_board_width, i, j)
      if(board[i][j] == 1): #alive
        if(neighbors >= 2 and neighbors < 4):
          next_board[i][j] = 1
      else: #dead
        if(neighbors == 3):
          next_board[i][j] = 1
  return next_board


def walk_and_tally(board: list, h: int, w: int, i: int, j: int):
  #check for corner
  neighbors = 0
  tlcorner = (i == 0 and j == 0)
  if(tlcorner):
    #up/left (wrap)
    if(board[h - 1][w - 1] == 1):
      neighbors += 1
    #up (wrap)
    if(board[h - 1][j] == 1):
      neighbors += 1
    #up/right (wrap)
    if(board[h - 1][j + 1] == 1):
      neighbors += 1
    #right
    if(board[i][j + 1] == 1):
      neighbors += 1
    #right/down
    if(board[i + 1][j + 1] == 1):
      neighbors += 1
    #down
    if(board[i + 1][j] == 1):
      neighbors += 1
    #down/left (wrap)
    if(board[i + 1][w - 1] == 1):
      neighbors += 1
    #left (wrap)
    if(board[i][w - 1] == 1):
      neighbors += 1
    return neighbors

  trcorner = (i == 0 and j == w - 1)
  if(trcorner):
    #up/left (wrap)
    if(board[h - 1][j - 1] == 1):
      neighbors += 1
    #up (wrap)
    if(board[h - 1][j] == 1):
      neighbors += 1
    #up/right (wrap)
    if(board[h - 1][0] == 1):
      neighbors += 1
    #right (wrap)
    if(board[i][0] == 1):
      neighbors += 1
    #down/right (wrap)
    if(board[i + 1][0] == 1):
      neighbors += 1
    #down
    if(board[i + 1][j] == 1):
      neighbors += 1
    #down/left
    if(board[i + 1][j - 1] == 1):
      neighbors += 1
    #left
    if(board[i][j - 1] == 1):
      neighbors += 1
    return neighbors

  blcorner = (i == h - 1 and j == 0)
  if(blcorner):
    #up/left (wrap)
    if(board[i - 1][w - 1] == 1):
      neighbors += 1
    #up
    if(board[i - 1][j] == 1):
      neighbors += 1
    #up/right
    if(board[i - 1][j + 1] == 1):
      neighbors += 1
    #right
    if(board[i][j + 1] == 1):
      neighbors += 1
    #down/right (wrap)
    if(board[0][j + 1] == 1):
      neighbors += 1
    #down (wrap)
    if(board[0][j] == 1):
      neighbors += 1
    #down/left (wrap)
    if(board[0][w - 1] == 1):
      neighbors += 1
    #left (wrap)
    if(board[i][w - 1] == 1):
      neighbors += 1
    return neighbors

  brcorner = (i == h - 1 and j == w - 1)
  if(brcorner):
    #up/left
    if(board[i - 1][j - 1] == 1):
      neighbors += 1
    #up
    if(board[i - 1][j] == 1):
      neighbors += 1
    #up/right (wrap)
    if(board[i - 1][0] == 1):
      neighbors += 1
    #right (wrap)
    if(board[i][0] == 1):
      neighbors += 1
    #down/right (wrap)
    if(board[0][0] == 1):
      neighbors += 1
    #down (wrap)
    if(board[0][j] == 1):
      neighbors += 1
    #down/left (wrap)
    if(board[0][j - 1] == 1):
      neighbors += 1
    #left
    if(board[i][j - 1] == 1):
      neighbors += 1
    return neighbors

  #check for edge
  tedge = (i == 0)
  if(tedge):
    #up/left (wrap)
    if(board[h - 1][j - 1] == 1):
      neighbors += 1
    #up (wrap)
    if(board[h - 1][j] == 1):
      neighbors += 1
    #up/right (wrap)
    if(board[h - 1][j + 1] == 1):
      neighbors += 1
    #right
    if(board[i][j + 1] == 1):
      neighbors += 1
    #down/right
    if(board[i + 1][j + 1] == 1):
      neighbors += 1
    #down
    if(board[i + 1][j] == 1):
      neighbors += 1
    #down/left
    if(board[i + 1][j - 1] == 1):
      neighbors += 1
    #left
    if(board[i][j - 1] == 1):
      neighbors += 1
    return neighbors
    
  redge = (j == w - 1)
  if(redge):
    #up/left
    if(board[i - 1][j - 1] == 1):
      neighbors += 1
    #up
    if(board[i - 1][j] == 1):
      neighbors += 1
    #up/right (wrap)
    if(board[i - 1][0] == 1):
      neighbors += 1
    #right (wrap)
    if(board[i][0] == 1):
      neighbors += 1
    #down/right (wrap)
    if(board[i + 1][0] == 1):
      neighbors += 1
    #down
    if(board[i + 1][j] == 1):
      neighbors += 1
    #down/left
    if(board[i + 1][j - 1] == 1):
      neighbors += 1
    #left
    if(board[i][j -1] == 1):
      neighbors += 1
    return neighbors

  bedge = (i == h - 1)
  if(bedge):
    #up/left
    if(board[i - 1][j - 1] == 1):
      neighbors += 1
    #up
    if(board[i - 1][j] == 1):
      neighbors += 1
    #up/right
    if(board[i - 1][j + 1] == 1):
      neighbors += 1
    #right
    if(board[i][j + 1] == 1):
      neighbors += 1
    #down/right (wrap)
    if(board[0][j + 1] == 1):
      neighbors += 1
    #down (wrap)
    if(board[0][j] == 1):
      neighbors += 1
    #down/left (wrap)
    if(board[0][j - 1] == 1):
      neighbors += 1
    #left
    if(board[i][j - 1] == 1):
      neighbors += 1
    return neighbors

  ledge = (j == 0)
  if(ledge):
    #up/left (wrap)
    if(board[i - 1][w - 1] == 1):
      neighbors += 1
    #up
    if(board[i - 1][j] == 1):
      neighbors += 1
    #up/right
    if(board[i - 1][j + 1] == 1):
      neighbors += 1
    #right
    if(board[i][j + 1] == 1):
      neighbors += 1
    #down/right
    if(board[i + 1][j + 1] == 1):
      neighbors += 1
    #down
    if(board[i + 1][j] == 1):
      neighbors += 1
    #down/left (wrap)
    if(board[i + 1][w - 1] == 1):
      neighbors += 1
    #left (wrap)
    if(board[i][w - 1] == 1):
      neighbors += 1
    return neighbors

  #handle central
  #up/left
  if(board[i - 1][j - 1] == 1):
    neighbors += 1
  #up
  if(board[i - 1][j] == 1):
    neighbors += 1
  #up/right
  if(board[i - 1][j + 1] == 1):
    neighbors += 1
  #right
  if(board[i][j + 1] == 1):
    neighbors += 1
  #down/right
  if(board[i + 1][j + 1] == 1):
    neighbors += 1
  #down
  if(board[i + 1][j] == 1):
    neighbors += 1
  #down/left
  if(board[i + 1][j - 1] == 1):
    neighbors += 1
  #left
  if(board[i][j - 1] == 1):
    neighbors += 1
  return neighbors
  

def pretty_print(board: list):
  def print_horiz_border(board_width: int):
    for _ in range(board_width + 2):
      print('-', end='')
    print()

  board_height = len(board)
  board_width = len(board[0])
  #print top of board
  print_horiz_border(board_width)
  #print interior rows of board
  for i in range(board_height):
    print('|', end='')
    for j in range(board_width):
      if board[i][j] == 1:
        print('*', end='')
      else:
        print(' ', end='')
    print('|')
  #print bottom of board
  print_horiz_border(board_width)

def main():
  """ height = int(input("Enter board height: "))
  width = int(input("Enter board width: "))
  time_between_frames = input("Number of seconds between frames (float): ")
  win_height = 3 * height
  win_width = 3 * width """

  """ soup = random_state(int(height), int(width))
  while(1):
    pretty_print(soup)
    soup = next_board_state(soup)
    time.sleep(float(time_between_frames))
    os.system('clear') """

main()
