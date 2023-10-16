import pandas as pd

def dda(x1, x2, y1, y2):
    length = max(abs(x2 - x1), abs(y2 - y1))

    x_inc = (x2 - x1) / float(length)
    y_inc = (y2 - y1) / float(length)
    x, y = (x1, y1)

    data = []  # Create a list to store the data
    x_values = [] # Create a list to store the x values

    for i in range(1, length, 1):
        x_round = round(x)
        x_truncate = int(x)
        y_value = round(y)

        data.append((x_round, x_truncate, y_value, y1))
        x_values.append(x) # Append the x value to the list
        x += x_inc
        y += y_inc

    return data, x_values

import pandas as pd

data, x_values = dda(11, 4, 2, 25)

X_round, X_truncate, Y_values, Y1 = zip(*data)

df = pd.DataFrame({'x_values': x_values, 'X_round': X_round, 'X_truncate': X_truncate, 'Y_values': Y_values})

# df = df.style.format({'x': '{:.4f}', 'y': '{:.2f}', 'x_values': '{:.4f}'}).hide(axis='index')
print(df)
