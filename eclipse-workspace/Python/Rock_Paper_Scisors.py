import random as r
import time as t
from getpass import getpass
import sys

def RPS_Game():
    '''This is a program for the game of rock paper scissors and can be played
    singleplayer or against the computer
    '''
    game = input('Two player game or CPU?: ')
    List = ['Rock', 'Paper', 'Scissors']  # List of possibilities for the CPU
    Status = True
    Status2 = True

    while Status2:
        if game.lower() == 'cpu':
            Status2 = False
            # Presents a loading screen
            sys.stdout.write('Loading.')
            t.sleep(.7)
            for i in range(3):
                sys.stdout.write('.')
                t.sleep(.5)
            print('\n Welcome to Rock paper scissors!')
            while Status:
                player = input('Choose Rock, Paper, or scissors: ')
                cpu = r.choice(List)  # Picks a random sign from the list
                # Shows who won
                if player.lower() == 'rock' and cpu.lower() == 'paper':
                    Status = False
                    print('Cpu chose paper!')
                    print('You lost!')
                    # Asks if the user wants to play again
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        # if the user says yes, the function repeats itself
                        RPS_Game()
                    else:
                        # if the user does not want to, the program terminates
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'rock' and cpu.lower() == 'scissors':
                    Status = False
                    print('Cpu chose scissors!')
                    print('You win!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'rock' and cpu.lower() == 'rock':
                    Status = False
                    print('Cpu chose rock!')
                    print("It's a tie!")
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'paper' and cpu.lower() == 'paper':
                    Status = False
                    print('Cpu chose paper!')
                    print("It's a tie!")
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'paper' and cpu.lower() == 'scissors':
                    Status = False
                    print('Cpu chose scissors!')
                    print('You lost!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'paper' and cpu.lower() == 'rock':
                    Status = False
                    print('Cpu chose rock!')
                    print('You win!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'scissors' and cpu.lower() == 'paper':
                    Status = False
                    print('Cpu chose paper!')
                    print("You win!")
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'scissors' and cpu.lower() == 'scissors':
                    Status = False
                    print('Cpu chose scissors!')
                    print("It's a tie!")
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player.lower() == 'scissors' and cpu.lower() == 'rock':
                    Status = False
                    print('Cpu chose rock!')
                    print('You lost!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                else:
                    Status = True
                    print('Something went wrong, Please try again!')
        elif game.lower() == 'two player':
            sys.stdout.write('Loading.')
            t.sleep(.7)
            for i in range(3):
                sys.stdout.write('.')
                t.sleep(.5)
            print('\n Welcome to Rock paper scissors!')
            player1 = getpass('Player 1: Choose Rock, Paper, or Scissors: ')
            player2 = getpass('Player 2: Choose Rock, Paper or Scissors: ')
            while Status:
                if player1.lower() == 'rock' and player2.lower() == 'paper':
                    Status = False
                    print('Player 2 wins!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'rock' and player2.lower() == 'scissors':
                    Status = False
                    print('Player 1 wins!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'rock' and player2.lower() == 'rock':
                    Status = False
                    print("It's a tie!, Both players chose rock!")
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'paper' and player2.lower() == 'paper':
                    Status = False
                    print("It's a tie!, Both players chose paper!")
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'paper' and player2.lower() == 'scissors':
                    Status = False
                    print('Player 2 wins!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'paper' and player2.lower() == 'rock':
                    Status = False
                    print('Player 1 wins!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'scissors' and player2.lower() == 'paper':
                    Status = False
                    print('Player 1 wins!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'scissors' and player2.lower() == 'scissors':
                    Status = False
                    print("It's a tie!, Both players chose scissors!")
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                elif player1.lower() == 'scissors' and player2.lower() == 'rock':
                    Status = False
                    print('Player 2 wins!')
                    again = input('Do you want to play again?: ')
                    if again.lower() == 'yes':
                        RPS_Game()
                    else:
                        print('Thank you for playing!')
                        sys.exit()
                else:
                    Status = True
                    print('Your spelling was wrong! Try again!')
                    player1 = getpass('Player 1: Choose Rock, Paper, or Scissors: ')
                    player2 = getpass('Player 2: Choose Rock, Paper or Scissors: ')

        else:
            Status2 = True
            game = input('Two player game or CPU?: ')



RPS_Game()




