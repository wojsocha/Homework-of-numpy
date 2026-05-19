import numpy as np

array = np.load('ex3_data.npy')
count_rows_with_nan = 0
for row in array:
    if np.any(np.isnan(row)):
        print(row)
        count_rows_with_nan += 1
print(f'Totally we have {count_rows_with_nan} rows with nan values.')

column_index = 1
for nan_in_columns in np.sum(np.isnan(array), axis=0):
    print(f'We have {nan_in_columns} nan value(s) in column number {column_index}.')
    column_index += 1