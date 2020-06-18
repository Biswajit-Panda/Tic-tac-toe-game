from random import randint as RI
from time import sleep
from sys import exit
board = []
def create_board():
     global board
     print('\n\nGame Start...')
     board = ['-','-','-',
              '-','-','-',
              '-','-','-']
     display()

#Displaying the Board
def display():
     print(board[0] + '|' + board[1] + '|' + board[2])
     print(board[3] + '|' + board[4] + '|' + board[5])
     print(board[6] + '|' + board[7] + '|' + board[8])



#Choosing the board position
def choose():
     c = input('Your turn:(choose between 1-9): ')
     if c == 'q':
          exit(0)
     c = int(c)
     if c in range(1,10):
          global board
          if board[c-1] != '-':
               print('choose again...')
               choose()
          else:     
               board[c-1] = 'X'
               display()
     else :
          print('Enter a valid number or if you want to quit press "q"')
          choose()



#generating random number
def computer_entry():
     global board
     r = RI(0,8)
     if board[r] != '-':
          computer_entry()
     else:
          print('Computer turn...',end=' ')
          sleep(1)
          print('it choose : '+ str(r))
          board[r] = 'O'
          display()


def check():
     #for rows
     row1 = (board[0] == board[1] == board[2] != '-')
     row2 = (board[3] == board[4] == board[5] != '-')
     row3 = (board[6] == board[7] == board[8] != '-')

     #for columns
     col1 = (board[0] == board[3] == board[6] != '-')
     col2 = (board[1] == board[4] == board[7] != '-')
     col3 = (board[2] == board[5] == board[8] != '-')

     #for diagonals
     dia1 = (board[0] == board[4] == board[8] != '-')
     dia2 = (board[2] == board[4] == board[6] != '-')

     win = ''
     if row1 or col1:
          win = board[0]
     elif row2 or col2 or dia1 or dia2:
          win = board[4]
     elif row3 or col3:
          win = board[8]


     if win == 'X':
          print('You Wins....')
          exit_game()
     elif win == 'O':
          print('Computer wins...')
          exit_game()

def draw():
     global board
     if '-' not in board:
          print('Match Draw...')
          exit_game()

def exit_game():
     s = input('Do you wanna play? (Press y/n): ')
     if s == 'y' or s == 'Y':
          create_board()
     else :
          exit(0)

#main function
if __name__ == '__main__':
     create_board()
     while True:
          choose()
          check()
          draw()
          computer_entry()
          check()
          draw()
