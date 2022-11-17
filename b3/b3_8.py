# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
#
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()
#
# print('---')
#
# ROWS = 3
# COLS = 2
#
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
#
# for i in range(ROWS):
#     for j in range(COLS):
#         print(matrix[i][j], end=" ")
#     print()
#
#
# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
#
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)


#
# test_list = [109, 58, 43, 234]
# max_value = test_list[0]
# for el in test_list:
#     if el > max_value:
#         max_value = el
# print(max_value)

# b3.8.1
test_matrix = [
    [-3, 435, -3],
    [7987, -3, -67],
    [-123, 2908, -1]
]
max_value = test_matrix[0][0]
for row in test_matrix:
    for el in row:
        if el > max_value:
            max_value = el
print(max_value)

# b3.8.1
# test_matrix = [
#     [-3, -435, 4],
#     [-7, -3, 7],
#     [-123, -2908, 4]
# ]
#
# row_len = len(test_matrix)
# col_count = 0
# for row in test_matrix:
#     if len(row) == row_len:
#         col_count += 1
# print(row_len == col_count)


