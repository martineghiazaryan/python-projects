board = [' ', ' ', ' ', 'x', ' ', 'x', ' ',' ', 'x']


# def print_board():
#         for row in [board[i*3: (i+1)*3] for i in range(3)]:
#             print('| ' + ' | '.join(row) + ' |')

# print_board()

result = [i for i, spot in enumerate(board) if spot == ' ']

print(result)

