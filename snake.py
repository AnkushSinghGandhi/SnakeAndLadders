from random import randint 
import turtle

# Player 1 position variable
player1pos = 1

# Player 2 position variable
player2pos = 1

# Variable for game loop
gameloop = True

# creating a turtle screen object
s = turtle.Screen()
s.setup(600, 600)
s.bgpic('assets/bg.png')

# registering custom shapes for turtle(player 1, player 2)
s.register_shape('assets/bull.gif')
s.register_shape('assets/cow.gif')

# seting up turtle for player 1
t = turtle.Turtle()
t.shape('assets/bull.gif')
t.speed(0.1)
t.penup()
t.setposition(-245,-230)

# seting up turtle for player 2
t2 = turtle.Turtle()
t2.shape('assets/cow.gif')
t2.speed(0.2)
t2.penup()
t2.setposition(-245,-250)

# main game loop
while (gameloop):
    

    #player1

    # asking player for its turn
    input("Player 1: Press enter to roll a dice")

    # dice rolling
    diceroll = randint(1,6)

    # moving player 1
    player1pos = player1pos + diceroll
    if player1pos <= 25:


        # normal moves

        if ((5 < player1pos) and (5 > (player1pos - diceroll))):
            t.forward(120*(5 - (player1pos - diceroll)))
            t.left(90)
            t.forward(120)
            t.left(90)
            t.forward(120*(player1pos - 6))
            
        elif ((10 < player1pos) and (10 >= (player1pos - diceroll))):
            t.forward(120*(10 - (player1pos - diceroll)))
            t.right(90)
            t.forward(120)
            t.right(90)
            if((player1pos - 11) <= 4):
                t.forward(120*(player1pos - 11))
            else:
                t.forward(480)
                t.left(90)
                t.forward(120)
                t.left(90)

        elif ((15 < player1pos) and (15 >= (player1pos - diceroll))):
            t.forward(120*(15-(player1pos - diceroll)))
            t.left(90)
            t.forward(120)
            t.left(90)
            if((player1pos - 16) <= 4):
                t.forward(120*(player1pos - 16))
            else:
                t.forward(480)
                t.right(90)
                t.forward(120)
                t.right(90)

        elif ((20 < player1pos) and (20 > (player1pos - diceroll))):
            t.forward(120*(20-(player1pos - diceroll)))
            t.right(90)
            t.forward(120)
            t.right(90)
            t.forward(120*(player1pos - 21))

        else:
            t.forward(120*diceroll)

        # special moves (win, snake, ladder)

        if player1pos == 5:
            player1pos = 15
            print("Player 1: You got to climb a ladder")
            print("Player 1: You are on 15 Position")
            t.left(90)
            t.forward(240)
            t.right(90)

        elif player1pos == 8:
            player1pos = 3
            print("Player 1: You got bitten by a snake")
            print("Player 1: You are on 3 Position")
            t.left(90)
            t.forward(120)
            t.left(90)

        elif player1pos == 9:
            player1pos = 12
            print("Player 1: You got to climb a ladder")
            print("Player 1: You are on 12 Position")
            t.right(90)
            t.forward(120)
            t.right(90)

        elif player1pos == 18:
            player1pos = 23
            print("Player 1: You got to climb a ladder")
            print("Player 1: You are on 23 Position")
            t.right(90)
            t.forward(120)
            t.right(90)

        elif player1pos == 20:
            player1pos = 1
            print("Player 1: You got bitten by a snake")
            print("Player 1: You are on 1 Position")
            t.left(90)
            t.forward(360)
            t.left(90)

        elif player1pos == 24:
            player1pos = 14
            print("Player 1: You got bitten by a snake")
            print("Player 1: You are on 14 Position")
            t.right(90)
            t.forward(240)
            t.left(90)

        elif player1pos == 25:
            print("Player 1: You Won")
            s.update()
            s.bgpic('assets/win.png')
            gameloop = False
            break

        else:
            print(f"Player 1: You are on {player1pos} position")
            player1pos = player1pos

    else:
        player1pos = player1pos - diceroll
        print(f"Player 1: You are on {player1pos} position")

        
        
    #player2

    # asking player for its turn
    input("Player 2: Press enter to roll a dice")

    # dice rolling
    diceroll = randint(1,6)

    # moving player 2
    player2pos = player2pos + diceroll
    if player2pos <= 25:

        # normal moves

        if ((5 < player2pos) and (5 > (player2pos - diceroll))):
            t2.forward(120*(5 - (player2pos - diceroll)))
            t2.left(90)
            t2.forward(120)
            t2.left(90)
            t2.forward(120*(player2pos - 6))
            
        elif ((10 < player2pos) and (10 >= (player2pos - diceroll))):
            t2.forward(120*(10 - (player2pos - diceroll)))
            t2.right(90)
            t2.forward(120)
            t2.right(90)
            if((player2pos - 11) <= 4):
                t2.forward(120*(player2pos - 11))
            else:
                t2.forward(480)
                t2.left(90)
                t2.forward(120)
                t2.left(90)

        elif ((15 < player2pos) and (15 >= (player2pos - diceroll))):
            t2.forward(120*(15-(player2pos - diceroll)))
            t2.left(90)
            t2.forward(120)
            t2.left(90)
            if((player2pos - 16) <= 4):
                t2.forward(120*(player2pos - 16))
            else:
                t2.forward(480)
                t2.right(90)
                t2.forward(120)
                t2.right(90)

        elif ((20 < player2pos) and (20 > (player2pos - diceroll))):
            t2.forward(120*(20-(player2pos - diceroll)))
            t2.right(90)
            t2.forward(120)
            t2.right(90)
            t2.forward(120*(player2pos - 21))

        else:
            t2.forward(120*diceroll)

        # special moves (win, snake, ladder)

        if player2pos == 5:
            player2pos = 15
            print("Player 2: You got to climb a ladder")
            print("Player 2: You are on 15 Position")
            t2.left(90)
            t2.forward(240)
            t2.right(90)

        elif player2pos == 8:
            player2pos = 3
            print("Player 2: You got bitten by a snake")
            print("Player 2: You are on 3 Position")
            t2.left(90)
            t2.forward(120)
            t2.left(90)

        elif player2pos == 9:
            player2pos = 12
            print("Player 2: You got to climb a ladder")
            print("Player 2: You are on 12 Position")
            t2.right(90)
            t2.forward(120)
            t2.right(90)

        elif player2pos == 18:
            player2pos = 23
            print("Player 2: You got to climb a ladder")
            print("Player 2: You are on 23 Position")
            t2.right(90)
            t2.forward(120)
            t2.right(90)

        elif player2pos == 20:
            player2pos = 1
            print("Player 2: You got bitten by a snake")
            print("Player 2: You are on 1 Position")
            t2.left(90)
            t2.forward(360)
            t2.left(90)

        elif player2pos == 24:
            player2pos = 14
            print("Player 2: You got bitten by a snake")
            print("Player 2: You are on 14 Position")
            t2.right(90)
            t2.forward(240)
            t2.left(90)

        elif player2pos == 25:
            print("Player 2: You Won")
            s.update()
            s.bgpic('assets/win.png')
            gameloop = False
            break

        else:
            print(f"Player 2: You are on {player2pos} position")
            player2pos = player2pos


    else:
        player2pos = player2pos - diceroll
        print(f"Player 2: You are on {player2pos} position")
       

    
    
s.mainloop()