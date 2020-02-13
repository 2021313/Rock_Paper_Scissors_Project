import getpass
from random import randint
#Get players names
first_p_name = input('Please enter your name: ')
second_p_name = input('Please enter your name: ')
#Pick who plays first
first_player = randint(1,2)
if first_player == 1:
        print(first_p_name + ' goes first!')
        p1 = first_p_name
        p2 = second_p_name
elif first_player == 2:
        print(second_p_name + ' goes first!')
        p1 = second_p_name
        p2 = first_p_name
#Select how many rounds there are
r_count = 1
r_num = int(input('Please specify how many rounds you want to play: '))
for r_count in range(r_num):
        #Get players choices
        p1_choice = getpass.getpass(p1 + ' please choose between Rock(1), Paper(2) and Scissors(3): ')
        print('Player 1 has chosen')
        p2_choice = getpass.getpass(p2 + ' please choose between Rock, Paper and Scissors: ')
        print('Player 2 has chosen')
        p1_r_win = 0
        p2_r_win = 0
        #Determine who wins round
        if p1_choice == '1' and p2_choice == '2':
                p2_r_win += 1
                print(p2 + ' wins!')
        elif p1_choice == '2' and p2_choice == '3':
                p2_r_win += 1
                print(p2 + ' wins!')
        elif p1_choice == '3' and p2_choice == '1':
                p2_r_win += 1
                print(p2 + ' wins!')
        elif p2_choice == '1' and p1_choice == '2':
                p1_r_win += 1
                print(p1 + ' wins!')
        elif p2_choice == '2' and p1_choice == '3':
                p1_r_win += 1
                print(p1 + ' wins!')
        elif p2_choice == '3' and p1_choice == '1':
                p1_r_win += 1
                print(p1 + ' wins!')
        elif p1_choice == '1' and p2_choice == '1':
                print('It\'s a draw!')
        elif p1_choice == '2' and p2_choice == '2':
                print('It\'s a draw!')
        elif p1_choice == '3' and p2_choice == '3':
                print('It\'s a draw!')
#Determine who wins the game
if p1_r_win > p2_r_win:
        print(p1 + ' wins the game!')
elif p1_r_win < p2_r_win:
        print(p2 + ' wins the game!')
elif p1_r_win == p2_r_win:
        print('The game is a draw!')