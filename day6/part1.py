import pandas as pd
import numpy as np

testing = False

if testing:
    filename = "sample_input.txt"
elif not testing:
    filename = "input.txt"

def get_next_loc(x,y,guard):
    if guard == '^':
        return x, y-1
    elif guard == '>':
        return x+1, y
    elif guard == '<':
        return x-1, y
    elif guard == 'V':
        return x, y+1

def check_next_loc(x,y,df):
    x_length = len(df.columns) - 1
    y_length = len(df.index) - 1
    if x < 0 or y < 0 or x > x_length or y > y_length:
        return 'leaving'
    if df[x][y] == '#':
        return 'obstacle'
    elif df[x][y] in ['.', '^']:
        return 'clear'

def turn_guard(guard):
    if guard == '^':
        return '>'
    elif guard == '>':
        return 'V'
    elif guard == 'V':
        return '<'
    elif guard == '<':
        return '^'

input = open(filename, 'r')
lines = input.read().splitlines()
df = pd.read_csv(filename, names=['col0'])
df = df['col0'].apply(lambda x: pd.Series(list(x)))
map = df.copy()

guard_in_room = True
guard_starting_loc = [[df.columns[y], int(x)] for x, y in zip(*np.where(df.values == '^'))][0]
guard_loc_x = guard_starting_loc[0]
guard_loc_y = guard_starting_loc[1]
guard_direction = '^'
map.loc[guard_loc_y,guard_loc_x] = 'X'

# print(f"Guard is starting at {guard_starting_loc}")

count = 0
while guard_in_room:
    # print(f"Guard is at {guard_loc_x}, {guard_loc_y}")
    map.loc[guard_loc_y,guard_loc_x] = 'X'
    next_loc_x, next_loc_y = get_next_loc(guard_loc_x, guard_loc_y, guard_direction)
    outcome = check_next_loc(next_loc_x, next_loc_y, df)
    if outcome == 'clear':
        guard_loc_x = next_loc_x
        guard_loc_y = next_loc_y
        count += 1
        continue
    elif outcome == 'obstacle':
        guard_direction = turn_guard(guard_direction)
    elif outcome == 'leaving':
        guard_in_room = False

locs = len([[df.columns[y], int(x)] for x, y in zip(*np.where(map.values == 'X'))])
print(map)
print(locs)