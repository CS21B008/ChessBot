# Description: Test the environment by running it for a few steps
from gym_chess import ChessEnvV2
import random
import numpy as np

def opponent_move(env):
    return env.minimax(depth=3)

env = ChessEnvV2(player_color='white', opponent=opponent_move,log=True)

done = False
while(not done):
    env.render()
    moves = env.get_possible_moves(env.state, env.current_player)
    if(done == True or len(moves) == 0):
        print("Game Over")
        exit()
    input_move = random.randint(0, len(moves)-1)
    move = moves[input_move]
    action = env.move_to_action(move)
    new_state, reward, done, info = env.step(action)
    
print("Game Over")