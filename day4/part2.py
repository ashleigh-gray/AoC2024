import pandas as pd
import numpy as np
import itertools

testing = 0

if testing == 4:
    filename = "sample_input4.txt"
elif testing == 5:
    filename = "sample_input5.txt"
elif testing == 0:
    filename = "input.txt"

input = open(filename, 'r')
lines = input.read().splitlines()

df = pd.read_csv(filename, names=['col0'])
df = df['col0'].apply(lambda x: pd.Series(list(x)))
x_length = len(df.columns)
y_length = len(df.index)

class number():
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y

    def __str__(self):
        return f"Char:{self.val}, ({self.x}, {self.y})"
    def __repr__(self):
        return f"Char:{self.val}, ({self.x}, {self.y})"

def get_adjs(i, max):
    adjs = []
    if i == 0:
        adjs.append(i + 1)
    elif i == max:
        adjs.append(i - 1)
    else:
        adjs.append(i - 1)
        adjs.append(i + 1)
    return adjs

def get_corners(char,df):
    x_max = len(df.columns) - 1
    y_max = len(df.index) - 1
    x_corners = get_adjs(char.x, x_max)
    y_corners = get_adjs(char.y, y_max)
    return list(itertools.product(x_corners, y_corners))

counter = 0
centres = df.mask(df != 'A', '.')
a_coords = [(df.columns[y], int(x)) for x, y in zip(*np.where(centres.values == 'A'))]
a_coords = [number(df[x][y], x, y) for x, y in a_coords]
for A in a_coords:
    x = A.x
    y = A.y
    corners = get_corners(A,df)
    if len(corners) < 4:
        continue
    if df[corners[0][0]][corners[0][1]] == df[corners[1][0]][corners[1][1]] == 'M' and df[corners[2][0]][corners[2][1]] == df[corners[3][0]][corners[3][1]] == 'S':
        counter += 1
    elif df[corners[0][0]][corners[0][1]] == df[corners[1][0]][corners[1][1]] == 'S' and df[corners[2][0]][corners[2][1]] == df[corners[3][0]][corners[3][1]] == 'M':
        counter += 1
    elif df[corners[0][0]][corners[0][1]] == df[corners[2][0]][corners[2][1]] == 'M' and df[corners[1][0]][corners[1][1]] == df[corners[3][0]][corners[3][1]] == 'S':
        counter += 1
    elif df[corners[0][0]][corners[0][1]] == df[corners[2][0]][corners[2][1]] == 'S' and df[corners[1][0]][corners[1][1]] == df[corners[3][0]][corners[3][1]] == 'M':
        counter += 1
print(counter)
