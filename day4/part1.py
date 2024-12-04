import pandas as pd
import numpy as np
import itertools

testing = 0

if testing == 1:
    filename = "sample_input1.txt"
elif testing == 2:
    filename = "sample_input2.txt"
elif testing == 3:
    filename = "sample_input3.txt"
elif testing == 0:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

df = pd.read_csv(filename, names=['col0'])
df = df['col0'].apply(lambda x: pd.Series(list(x)))
x_length = len(df.columns)
y_length = len(df.index)

class number():
    def __init__(self, val, x, y, direction=[0,0]):
        self.val = val
        self.x = x
        self.y = y
        self.direction = direction
    def __str__(self):
        return f"Char:{self.val}, ({self.x}, {self.y}), direction: {self.direction}"
    def __repr__(self):
        return f"Char:{self.val}, ({self.x}, {self.y}), direction: {self.direction}"

def get_adjs(i, max):
    adjs = [i]
    if i == 0:
        adjs.append(i + 1)
    elif i == max:
        adjs.append(i - 1)
    else:
        adjs.append(i - 1)
        adjs.append(i + 1)
    return adjs

def direction(x_orig, y_orig, x_dest, y_dest):
    if x_dest == x_orig - 1 and y_dest == y_orig:
        return [-1,0]
    elif x_dest == x_orig + 1 and y_dest == y_orig:
        return [1,0]
    elif x_dest == x_orig - 1 and y_dest == y_orig - 1:
        return [-1,-1]
    elif x_dest == x_orig - 1 and y_dest == y_orig + 1:
        return [-1,1]
    elif x_dest == x_orig and y_dest == y_orig - 1:
        return [0,-1]
    elif x_dest == x_orig and y_dest == y_orig + 1:
        return [0,1]
    elif x_dest == x_orig + 1 and y_dest == y_orig + 1:
        return [1,1]
    elif x_dest == x_orig + 1 and y_dest == y_orig - 1:
        return [1,-1]

def find_next_chars(char, next_char, df):
    x_max = len(df.columns) - 1
    y_max = len(df.index) - 1
    x_adjs = get_adjs(char.x, x_max)
    y_adjs = get_adjs(char.y, y_max)
    all_adjs = list(itertools.product(x_adjs, y_adjs))
    all_adjs.remove((char.x, char.y))
    next_chars = []

    for x, y in all_adjs:
        if df[x][y] == next_char:
            next_chars.append(number(df[x][y], x, y, direction(char.x, char.y, x, y)))
        else:
            continue
    return next_chars

def find_next_chars_targeted(char, next_char, df):
    direction = char.direction
    next_x = char.x + direction[0]
    next_y = char.y + direction[1]
    x_max = len(df.columns) - 1
    y_max = len(df.index) - 1

    if 0 <= next_x <= x_max and 0 <= next_y <= y_max:
        if df[next_x][next_y] == next_char:
            return number(df[next_x][next_y], next_x, next_y, direction)
        else:
            return 0
    else:
        return 0

counter = 0
xs = df.mask(df != 'X', '.')
x_coords = [(df.columns[y], int(x)) for x, y in zip(*np.where(xs.values == 'X'))]
x_coords = [number(df[x][y], x, y) for x, y in x_coords]

for X in x_coords:
    x = X.x
    y = X.y
    X = number(df[x][y], x, y)
    for M in find_next_chars(X, 'M', df):
        x = M.x
        y = M.y
        M = number(df[x][y], x, y, M.direction)
        A = find_next_chars_targeted(M, 'A', df)
        if A != 0:
            S = find_next_chars_targeted(A, 'S', df)
            if S != 0:
                counter += 1
                continue
print(counter)