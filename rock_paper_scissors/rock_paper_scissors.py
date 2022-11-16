import random 

def play():
    user = input('What is your choice, r for Rock, p for Paper and s for Scissors?')

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    # r > s, s > p, p > r

    if is_win(user, computer):
        return('You won!')
    
    return ('You lost!')

def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
        
play()