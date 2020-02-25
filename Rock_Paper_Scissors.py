from R_P_S_Play_First import Get_Player_Name
from R_P_S_Play_First import Pick_First_Player
import getpass
first_p_name = Get_Player_Name()
second_p_name = Get_Player_Name()
print("Hello ", first_p_name, " and ", second_p_name, " welcome to rock paper scissors!")
p1, p2 = Pick_First_Player(first_p_name, second_p_name)
def Play_Game():
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
        Player_Win(p1_r_win, p2_r_win)
def Player_Win(p1win, p2win):
        #Determine who wins the game
        if p1win > p2win:
                print(p1 + ' wins the game!')
        elif p1win < p2win:
                print(p2 + ' wins the game!')
        elif p1win == p2win:
                print('The game is a draw!')
Play_Game()