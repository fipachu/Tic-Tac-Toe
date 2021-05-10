# awesome stage 3, modified by me
# credit: https://hypers
# kill.org/projects/73/stages/401/implement#solutions-98086

def print_grid():
    print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*cells))


def compute_game_state():
    global keep_playing

    straights = [cells[:3], cells[3:6], cells[6:],  # horizontal
                 cells[0:9:3], cells[1:9:3], cells[2:9:3],  # vertical
                 cells[0:9:4], cells[2:7:2]]  # diagonal
    if abs(cells.count('X') - cells.count('O')) > 1 \
            or 'XXX' in straights and 'OOO' in straights:
        keep_playing = False
        return "How'd you even do that!? You broke the game, start again!"
    elif 'XXX' in straights:
        keep_playing = False
        return 'X wins'
    elif 'OOO' in straights:
        keep_playing = False
        return 'O wins'
    elif cells.count('_') > 0:
        return 'Game not finished'
    elif cells.count('_') == 0:
        keep_playing = False
        return 'Draw'


def get_cords():
    valid_list = [0, 1, 2]
    while True:
        try:
            row, column = [int(number) - 1 for number
                           in input("Enter the coordinates: ").split()]
            if row not in valid_list or column not in valid_list:
                print("Coordinates should be from 1 to 3!")
                continue
            elif cells[row * 3 + column] in ["X", "O"]:
                print("This cell is occupied! Choose another one!")
                continue
            else:
                break
        except ValueError:
            print("You should enter two numbers!")
    return [row, column]


def update_cells(row, column):
    global X_or_O
    global cells

    temp_list = list(cells)
    if X_or_O:
        temp_list[row * 3 + column] = "X"
    else:
        temp_list[row * 3 + column] = "O"

    X_or_O = not X_or_O
    cells = "".join(temp_list)


# globals:
keep_playing = True
X_or_O = True
cells = "_________"

print_grid()
while keep_playing:
    cord1, cord2 = get_cords()
    update_cells(cord1, cord2)
    print_grid()
    print(compute_game_state())
