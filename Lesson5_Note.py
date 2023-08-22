# Ordinary Least Squares (OLS) là một phương pháp thống kê phổ biến được sử dụng trong mô hình hóa quan hệ giữa một biến phụ thuộc (còn gọi là biến mục tiêu) và 
# một hoặc nhiều biến độc lập (còn gọi là biến dự đoán). 
# OLS thường được sử dụng trong bài toán hồi quy (regression) để tìm một đường cong (thường là đường thẳng trong trường hợp hồi quy tuyến tính) 
# tốt nhất để tiên đoán giá trị của biến phụ thuộc dựa trên các giá trị của các biến độc lập.

# Cách thức hoạt động của OLS là tìm đường cong (thông qua các hệ số hồi quy) sao cho tổng bình phương sai số giữa các điểm dữ liệu thực tế và các điểm dự đoán trên đường cong là nhỏ nhất. 
# Bình phương sai số là sự chênh lệch giữa giá trị thực tế và giá trị dự đoán và việc bình phương giá trị này giúp tránh các giá trị dương và âm hủy nhau.

# Công thức tổng quát của mô hình hồi quy tuyến tính OLS là:

# Y = β₀ + β₁*X₁ + β₂*X₂ + ... + βᵣ*Xᵣ + ε

# Trong đó:
# - Y là biến phụ thuộc (biến mục tiêu) mà chúng ta muốn dự đoán.
# - X₁, X₂, ..., Xᵣ là các biến độc lập được sử dụng để dự đoán Y.
# - β₀, β₁, β₂, ..., βᵣ là các hệ số hồi quy, thể hiện mức độ ảnh hưởng của từng biến độc lập tới biến phụ thuộc.
# - ε là sai số ngẫu nhiên (error) trong mô hình.

# Trong quá trình xây dựng mô hình OLS, chúng ta tìm các giá trị của các hệ số hồi quy sao cho tổng bình phương sai số ε là nhỏ nhất. Điều này thường được thực hiện thông qua các phương pháp tối ưu hóa như phương pháp bình phương tối thiểu (least squares method).



# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Dữ liệu mẫu (giả sử có mối quan hệ tuyến tính giữa X và y)
# X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
# y = np.array([2, 4, 6, 8, 10, 12])

# # Tạo mô hình hồi quy tuyến tính
# model = LinearRegression()
# model.fit(X, y)

# # Lấy các hệ số hồi quy
# coef = model.coef_[0]
# intercept = model.intercept_

# # In các hệ số hồi quy
# print("Hệ số hồi quy:", coef)
# print("Hệ số chặn:", intercept)

# # Dự đoán giá trị mới
# new_X = np.array([[7], [8]])
# predicted_values = model.predict(new_X)

# # In các giá trị dự đoán
# print("Giá trị dự đoán cho X =", new_X[0][0], "là", predicted_values[0])
# print("Giá trị dự đoán cho X =", new_X[1][0], "là", predicted_values[1])

# # Vẽ biểu đồ
# plt.scatter(X, y, color='blue', label='Dữ liệu')
# plt.plot(X, model.predict(X), color='red', linewidth=2, label='Mô hình hồi quy')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.legend()
# plt.show()



