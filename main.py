from random import choice

options = ['Rock','Paper','Scissors']


game_active = True

instruction = print("Enter R(rock), P(paper) or S(scissors):")
while game_active:
    computer_pick = choice(options)
    users_pick = input(">>> ").lower()
    
    if (users_pick!='r') and (users_pick!='s') and (users_pick!='p'):
        print('Invalid input, try again!\n')
        continue

    elif (users_pick == 'r') :
        r ='Rock'
        print(f"Player({r}):CPU({computer_pick})")

        if computer_pick == 'Scissors':
            print('You win\n')
            game_active = False
            break


        elif computer_pick=='Paper':
            print('Computer wins\n')
            game_active = False
            break

        else:
            print('Draw\n')
            game_active=True
            continue

    elif (users_pick == 's'):
        s = 'Scissors'
        print(f"Player({s}):CPU({computer_pick})")
        
        if computer_pick == 'Rock':
            print('Computer wins\n')
            game_active = False
            break

        elif computer_pick=='Paper':
            print('You win\n')
            game_active = False
            break

        else:
            print('Draw\n')
            game_active = True
            continue



    elif (users_pick == 'p'):
        p = 'Paper'
        print(f"Player({p}):CPU({computer_pick})")

        if computer_pick == 'Scissors':
            print('Computer wins\n')
            game_active = False
            break

        elif computer_pick=='Rock':
            print('You win\n')
            game_active = False
            break

        else:
            print('Draw\n')
            game_active = True
            continue

    
    
