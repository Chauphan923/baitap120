import numpy as np

N = int(input("Nhap vao so dong n:"))
M = int(input("Nhap vao so cot M:"))

matrix = np.random.randint(-100,101,(N,M))
print(matrix)

#dinh thuc vuong
if N == M:
    D = np.linalg.det(matrix)
    print("Dinh thuc ma tran:", round(D,3))
else:
    print("Ma tran khong vuong")

#Nghich dao ma tran (matrix vuong, kha nghich)

if N==M:
    matran_nghichdao = np.linalg.inv(matrix)
    print("Ma tran nghich dao:\n", matran_nghichdao)
else:
    print("Ma tran khong co nghich dao")

#Sap xep ma tran theo hang
sorted_rows =np.sort(matrix, axis=1)
print("Ma tran sap xep theo hang:\n",sorted_rows)

#Sap xep ma tran theo cot
sorted_cols = np.sort(matrix, axis =1)
print("Ma tran sap xep theo hang:\n", sorted_cols)

#Sapxep theo gt trung binh cua tung hang
row_mean= matrix.mean(axis=1)
sorted_indices = np.argsort(row_mean)
sorted_by_mean = matrix[sorted_indices]
print("Ma tran sap xep theo trung binh hang:\n", sorted_cols)
# (6) Sắp xếp ma trận theo giá trị trung bình của từng hàng
row_means = matrix.mean(axis=1)
sorted_indices = np.argsort(row_means)
sorted_by_mean = matrix[sorted_indices]
print("Ma trận sắp xếp theo trung bình hàng:\n", sorted_by_mean)

# (7) Thay đổi giá trị một phần tử trong ma trận
i = int(input("Nhập chỉ số dòng: "))
j = int(input("Nhập chỉ số cột: "))
new_value = int(input("Nhập giá trị mới: "))
matrix[i, j] = new_value
print("Ma trận sau khi thay đổi giá trị:\n", matrix)

# (8) Tăng giá trị một cột lên 2
col_index = int(input("Nhập cột muốn tăng giá trị: "))
matrix[:, col_index] += 2
print("Ma trận sau khi tăng giá trị cột:", matrix)

# (9) Cộng thêm một vector vào từng hàng của ma trận
vector = np.random.randint(-10, 11, M)
matrix_added = matrix + vector
print("Ma trận sau khi cộng vector:", matrix_added)

# (10) Tính hạng của ma trận
rank = np.linalg.matrix_rank(matrix)
print("Hạng của ma trận:", rank)

# (11) Phân tích SVD
U, S, V = np.linalg.svd(matrix)
print("Ma trận U:\n", U)
print("Giá trị kỳ dị S:\n", S)
print("Ma trận V:\n", V)



