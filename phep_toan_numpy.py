import numpy as np

N = int(input("Nhập vào số dòng N: "))
M = int(input("Nhập vào số cột M: "))

matrix = np.random.randint(-100, 101, (N, M))
print("Ma trận ban đầu:")
print(matrix)

# Định thức ma trận
if N == M:
    det_value = round(np.linalg.det(matrix), 3)
    print("Định thức ma trận:", det_value)
else:
    print("Ma trận không vuông, không thể tính định thức.")

# Ma trận nghịch đảo
if N == M and np.linalg.det(matrix) != 0:
    inverse_matrix = np.linalg.inv(matrix)
    print("Ma trận nghịch đảo:\n", inverse_matrix)
else:
    print("Ma trận không có nghịch đảo.")

# Sắp xếp ma trận theo hàng
sorted_rows = np.sort(matrix, axis=1)
print("Ma trận sắp xếp theo hàng:\n", sorted_rows)

# Sắp xếp ma trận theo cột
sorted_cols = np.sort(matrix, axis=0)
print("Ma trận sắp xếp theo cột:\n", sorted_cols)

# Sắp xếp theo giá trị trung bình của từng hàng
row_means = matrix.mean(axis=1)
sorted_indices = np.argsort(row_means)
sorted_by_mean = matrix[sorted_indices]
print("Ma trận sắp xếp theo giá trị trung bình hàng:\n", sorted_by_mean)

# Thay đổi giá trị một phần tử trong ma trận
i = int(input("Nhập chỉ số dòng: "))
j = int(input("Nhập chỉ số cột: "))
new_value = int(input("Nhập giá trị mới: "))
matrix[i, j] = new_value
print("Ma trận sau khi thay đổi giá trị:\n", matrix)

# Tăng giá trị một cột lên 2
col_index = int(input("Nhập cột muốn tăng giá trị: "))
matrix[:, col_index] += 2
print("Ma trận sau khi tăng giá trị cột:\n", matrix)

# Cộng thêm một vector vào từng hàng của ma trận
vector = np.random.randint(-10, 11, M)
matrix_added = matrix + vector
print("Ma trận sau khi cộng vector:\n", matrix_added)

# Tính hạng của ma trận
rank = np.linalg.matrix_rank(matrix)
print("Hạng của ma trận:", rank)

# Phân tích SVD
U, S, V = np.linalg.svd(matrix)
print("Ma trận U:\n", U)
print("Giá trị kỳ dị S:\n", S)
print("Ma trận V:\n", V)
