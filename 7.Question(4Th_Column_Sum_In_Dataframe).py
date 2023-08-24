import pandas as pd

dataframe = [
    [10, 20, 4, 66, 56, 6, 12],
    [1, 60, 64, 6, 5, 556, 612],
    [176, 623, 6545, 126, 521, 55, 62]
]

df = pd.DataFrame(dataframe, columns=['Column0', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6'])

sum_column4 = df['Column3'].sum()
print("Sum of the 4th column:", sum_column4)

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the dataframe.

# Space Complexity: O(m * n), considering the space required to store the dataframe itself.