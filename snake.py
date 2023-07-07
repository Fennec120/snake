import sys
import select
from inputimeout import inputimeout, TimeoutOccurred
from threading import Timer
from pytimedinput import timedInput
from pytimedinput import timedKey
import signal
import random
from resources import field_reset
from resources import opposites

def field_reset():
    global field
    field = [[' ']]
    for i in range(9):
        field.append(field[0] * 10)
    for i in range(9):
        field[0].append(field[0][0])

    pass
opposites = opposites
prev_input = None
snake = []
snake.append((5, 5))
movement = (0, -1)
apple = (None, None)
user_input = None
eaten = True
snake_extension_pending = None

while user_input != 'b':
    field_reset()

    # apple block

    if eaten == True:
        apple = (random.randint(0, 9), random.randint(0, 9))
        if apple in snake:
            while apple in snake:
                apple = (random.randint(0, 9), random.randint(0, 9))

        eaten = False

    # field printing
    try:
        field[apple[0]][apple[1]] = 'O'
    except IndexError:
        print(apple)

    try:
        for link in snake:
            field[link[0]][link[1]] = 'X'
    except IndexError:
        print(link[0], link[1])


    for sublist in field:
        print(sublist)

    # input movement direction
    user_input = input()
        # timeout = inputimeout(timeout=2)
    #except TimeoutOccurred:
        #pass

    if (prev_input, user_input) in opposites:
        user_input = prev_input
    else:
        if user_input == '8':
            movement = (-1, 0)
        if user_input == '4':
            movement = (0, -1)
        if user_input == '5' or user_input == '2':
            movement = (1, 0)
        if user_input == '6':
            movement = (0, 1)
        prev_input = user_input

    if apple in snake:
        eaten = True
        snake_extension_pending = True

    # snake movement display calculation
    if snake_extension_pending == True:

        snake.append((snake[-1][0] + movement[0], snake[-1][1] + movement[1]))
        snake_extension_pending = False
    else:
        snake.append((snake[-1][0] + movement[0], snake[-1][1] + movement[1]))
        snake.pop(0)
    if snake[-1] in snake[0:-1]:
        print('game over:(')
        break