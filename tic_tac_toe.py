def print_grid(grid):
    for row in range(3):
        print(" | ".join(grid[row]))
        if(row<2):
            print('--+---+--')

def takeMoves(grid,player):
    while True:
        try:
            row=int(input('Enter the row: '))
            col=int(input('Enter the coloum: '))
            row-=1
            col-=1
            if(row not in range(3) or col not in range(3)):
                print('Enter valid position. Number between 1 and 3.')
                continue
            elif(grid[row][col]!=' '):
                print('Already filled.')
                continue
            grid[row][col]=player
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

def checkWins(grid,current_player):
    lines=[
           #rows
           [grid[r][0] for r in range(3)],
           [grid[r][1] for r in range(3)],
           [grid[r][2] for r in range(3)],
           #column
           [grid[0][col] for col in range(3)],
           [grid[1][col] for col in range(3)],
           [grid[2][col] for col in range(3)],
           #diagonal
           [grid[i][i] for i in range(3)],
           [grid[i][2-i] for i in range(3)]]
    return any(all(cell == current_player for cell in line) for line in lines)
def playGame():
    grid=[[' ' for _ in range(3) ] for _ in range(3)]
    current_player='X'
    print("Current Player: X")
    for move in range(9):
        print_grid(grid)
        takeMoves(grid,current_player)
        if checkWins(grid,current_player):
            print_grid(grid)
            print(f'Player {current_player} wins.')
            return
        current_player='O' if current_player=='X' else 'X'
        print(f"Current Player: {current_player}")
    print('Tie.')
while True:
    playGame()
    again = input("Play again? (y/n) ").lower()
    if again != "y":
        break
