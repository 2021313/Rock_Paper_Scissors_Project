from random import randint
def Get_Player_Name():
    #Get players names
    name = input('Please enter your name: ')
    return name
def Pick_First_Player(fpname, spname):
    #Pick who plays first
    first_player = randint(1,2)
    if first_player == 1:
        print(fpname + ' goes first!')
        p1 = fpname
        p2 = spname
        return p1, p2
    elif first_player == 2:
        print(spname + ' goes first!')
        p1 = spname
        p2 = fpname
        return p1, p2