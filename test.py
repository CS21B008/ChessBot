# Description: Test the environment by running it for a few steps
from gym_chess import ChessEnvV2
import random
import numpy as np

def opponent_move(env):
    return env.minimax(depth=5)

env = ChessEnvV2(player_color='white', opponent=opponent_move,log=True)

while(not env.done):
    env.render()
    moves = env.possible_moves
    if(env.done == True or len(moves) == 0):
        print("Game Over")
        exit()
    print("Possible moves: ", moves)
    print("Enter move: ")
    input_move = int(input())
    move = moves[input_move]
    action = env.move_to_action(move)
    new_state, reward, done, info = env.step(action)
    