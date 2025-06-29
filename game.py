from turtle import *
from freegames import line

# Switching turns
turns = {'red': 'yellow', 'yellow': 'red'}

# Game state
state = {
    'player': 'yellow',
    'rows': [0] * 8,
    'board': [[''] * 8 for _ in range(8)],
    'game_over': False
}
def grid():
    bgcolor('lightblue')
    for x in range(-150, 201, 50):
        line(x, -200, x, 200)
    for x in range(-175, 201, 50):
        for y in range(-175, 201, 50):
            up()
            goto(x, y)
            dot(40, 'white')
    update()
    
def check_winner(board,  player):
    for row in range(8):
        for col in range(5):
            if all(board[row][col + i] == player for i in range(4)):
                return True
            
            
    for col in range(8):
        for row in range(5):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    
    for row in range(5):
        for col in range(5):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
                            
    for row in range(5):
        for col in range(3, 8):
            if all(board[row + i][col - i] == player for i in range(4)):
                return True
    return False
 
def show_winner(player):
    goto(0, 180)
    color('black')
    write(f'{player} wins!', align='center', font=('Arial', 24, 'bold'))
 
 
 
 
def tap(x, y):
    if state['game_over']:
        return

    player = state['player']
    rows = state['rows']
    board = state['board']

    # Get column number
    col = int((x + 200) // 50)
    if not (0 <= col < 8):
        return
    if rows[col] >= 8:
        return

    row = rows[col]
    rows[col] += 1
    board[row][col] = player

    # Draw the move
    px = col * 50 - 200 + 25
    py = row * 50 - 200 + 25
    up()
    goto(px, py)
    dot(40, player)
    update()

    # Check for a winner
    if check_winner(board, player):
        state['game_over'] = True
        show_winner(player)
        return
    
    # Switch players
    state['player'] = turns[player]
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(tap)
done()
# Press Ctrl-C to stop the game.    