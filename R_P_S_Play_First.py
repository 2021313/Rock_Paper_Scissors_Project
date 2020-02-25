from random import randint
def Pick_First_Player():
    #Get players names
    first_p_name = input('Please enter your name: ')
    second_p_name = input('Please enter your name: ')
    print("Hello ", first_p_name, " and ", second_p_name, " welcome to rock paper scissors!")
    #Pick who plays first
    first_player = randint(1,2)
    if first_player == 1:
        print(first_p_name + ' goes first!')
        p1 = first_p_name
        p2 = second_p_name
        return p1, p2
    elif first_player == 2:
        print(second_p_name + ' goes first!')
        p1 = second_p_name
        p2 = first_p_name
        return p1, p2