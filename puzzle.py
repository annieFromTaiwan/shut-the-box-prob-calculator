#  http://www.ptt.cc/bbs/puzzle/M.1408711282.A.D75.html
#  #1Jzpforr (puzzle) 

import numpy as np
import itertools

# initialize probability array
dice_prob = np.array([0.0]*13)
for dice_a in range(1,7):
    for dice_b in range(1,7):
        dice_prob[dice_a + dice_b] += 1
dice_prob /= 36
#print dice_prob/36

# 
def afterwards_boards(orig_board, dice):
    afterwards_boards = []
    # one digit
    if dice in orig_board:
        board = list(orig_board)
        board.remove(dice)
        afterwards_boards.append(tuple(board))
    # two digits
    for idx in range(len(orig_board)):
        digit_a = orig_board[idx]
        digit_b = dice - digit_a
        if digit_b in orig_board[idx+1:]:
            board = list(orig_board)
            board.remove(digit_a)
            board.remove(digit_b)
            afterwards_boards.append(tuple(board))
    return afterwards_boards

prob = {}
prob[()] = 1

def get_prob(board):
    if board in prob:
        return prob[board]
    p = 0.0
    for dice in range(2,13):
        possiblities = afterwards_boards(board, dice)
        if len(possiblities) == 0:
            continue
        res = [get_prob(possible_board) for possible_board in possiblities]
        p += dice_prob[dice] * max(res)
    return p
        

for cnt_available_place in range(1,10):
    for board in itertools.combinations(range(1,10), cnt_available_place):
        prob[board] = get_prob(board)

keys = sorted(prob.keys(), key=lambda x: (len(x), x) )
for k in keys:
    print k, prob[k]

def available_choices(board, dice):
    available_choices = afterwards_boards(board, dice)
    for b in available_choices:
        print b, prob[b]
    return available_choices
