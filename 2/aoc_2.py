# A - X = rock
# A - X = rock
# B - Y = paper
# C - Z = scissors
# X = lose
# Y = draw
# Z = win

cnt = 0

def played(me, _1_2):
    if _1_2 == 1:
        if me == 'X':
            return 1
        elif me == 'Y':
            return 2
        elif me == 'Z':
            return 3
    else:
        if me == 'X':
            return 0
        elif me == 'Y':
            return 3
        elif me == 'Z':
            return 6
        
def ret_win_lose(state, _1_2):
    if _1_2 == 1:
        if state == 'lose':
            return 0
        elif state == 'draw':
            return 3
        elif state == 'win':
            return 6
    else:
        if state == 'rock':
            return 1
        elif state == 'paper':
            return 2
        elif state == 'scissors':
            return 3
        
def get_points(opponent, me):
    if opponent == 'A':
        if me == 'Z':
            return ret_win_lose("paper", 2) + played(me, 2)
        elif me == 'Y':
            return ret_win_lose("rock", 2) + played(me, 2)
        elif me == 'X':
            return ret_win_lose("scissors", 2) + played(me, 2)
    elif opponent == 'B':
        if me == 'Z':
            return ret_win_lose("scissors", 2) + played(me, 2)
        elif me == 'Y':
            return ret_win_lose("paper", 2) + played(me, 2)
        elif me == 'X':
            return ret_win_lose("rock", 2) + played(me, 2)
    elif opponent == 'C':
        if me == 'Z':
            return ret_win_lose("rock", 2) + played(me, 2)
        elif me == 'Y':
            return ret_win_lose("scissors", 2) + played(me, 2)
        elif me == 'X':
            return ret_win_lose("paper", 2) + played(me, 2)

with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        cnt += get_points(line.split(" ")[0], line.split(" ")[1])
    
print(cnt)
    