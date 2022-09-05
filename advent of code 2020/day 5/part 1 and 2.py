import pandas as pd
import numpy as np

f = open('input.txt')
inp_ = f.readlines()

repl_ = {'F': '0', 'B': '1', 'R': '1', 'L': '0', '\n': ''}
df = pd.DataFrame(inp_)[0].replace(repl_, regex=True).str.split('', expand=True).iloc[:, 1:-1].apply(pd.to_numeric)
row = df.iloc[:, :7].values.dot(1 << np.arange(7)[::-1])
col = df.iloc[:, 7:].values.dot(1 << np.arange(3)[::-1])
seats = np.sort(row*8+col)

seat_diff = np.diff(np.sort(row*8+col))
missing_seat_index = np.argmax(seat_diff != 1)
missing_seat = seats[missing_seat_index]+1

pass