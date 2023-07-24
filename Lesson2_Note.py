# Trong Python, `np.linalg.inv` là một hàm trong thư viện NumPy (`np`) dùng để tính ma trận nghịch đảo. 
# Nghịch đảo của một ma trận A được ký hiệu là A^(-1) và có tính chất sau: 
# nếu nhân ma trận A với nghịch đảo của nó, ta sẽ thu được ma trận đơn vị (ma trận có đường chéo chính bằng 1 và các phần tử khác bằng 0). 
# Tức là A * A^(-1) = I, với I là ma trận đơn vị.
# Để sử dụng `np.linalg.inv`, bạn cần chắc chắn rằng ma trận đầu vào là vuông và không suy biến (không khả nghịch). 
# Nếu ma trận không khả nghịch, hàm `np.linalg.inv` sẽ gây ra lỗi.

# Dưới đây là một ví dụ về việc sử dụng `np.linalg.inv` để tính nghịch đảo của một ma trận vuông:

# ```python
# import numpy as np

# # Ma trận vuông 3x3
# A = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# # Tính ma trận nghịch đảo của A
# A_inv = np.linalg.inv(A)

# print("Ma trận A:")
# print(A)

# print("Ma trận nghịch đảo của A:")
# print(A_inv)
# ```
# Khi chạy đoạn mã trên, bạn sẽ nhận được kết quả là ma trận nghịch đảo của ma trận A, giúp bạn hiểu hơn về cách `np.linalg.inv` hoạt động trong NumPy.


# Trong np.linalg.inv(X.T @ X) @ X.T @ Y, dấu @ là toán tử nhân ma trận trong Python (từ Python 3.5 trở đi). 
# Nó được sử dụng để thực hiện phép nhân giữa các ma trận và/hoặc vector.
# Để hiểu ý nghĩa của biểu thức này, chúng ta cần phân tích từng phần:
# X.T: Đây là ma trận chuyển vị (transpose) của ma trận X. Nó là ma trận mà các hàng của X trở thành các cột và ngược lại.
# X.T @ X: Đây là kết quả của phép nhân ma trận giữa ma trận chuyển vị của X và X ban đầu. Kết quả là một ma trận vuông.
# np.linalg.inv(X.T @ X): Đây là hàm np.linalg.inv của NumPy dùng để tính ma trận nghịch đảo của X.T @ X. 
# Kết quả của biểu thức này là ma trận nghịch đảo của ma trận X.T @ X.
# X.T @ X) @ X.T @ Y: Sau khi tính được ma trận nghịch đảo của X.T @ X, chúng ta thực hiện phép nhân giữa nghịch đảo này và X.T @ Y. 
# Kết quả là một vector có kích thước tương ứng với số cột của ma trận X.
# Cuối cùng, biểu thức trên đại diện cho phép tính tham số w (weights) trong bài toán Multiple Linear Regression. 
# Nó sẽ cung cấp các tham số tối ưu cho mô hình, để ta có thể sử dụng chúng để dự đoán giá trị của biến phụ thuộc dựa trên các biến độc lập.


# Ma trận chuyển vị (transpose matrix) của một ma trận là một ma trận mới mà các hàng của ma trận gốc trở thành các cột và 
# các cột của ma trận gốc trở thành các hàng. Để chuyển vị một ma trận A, ta đơn giản là hoán đổi vị trí các phần tử của A qua đường chéo chính. 
# Chúng ta ký hiệu ma trận chuyển vị của A là A^T.
# Ví dụ, giả sử chúng ta có ma trận sau đây:
# ```
# A = [1 2 3]
#     [4 5 6]
# ```
# Ma trận chuyển vị của A (A^T) sẽ là:
# ```
# A^T = [1 4]
#       [2 5]
#       [3 6]
# ```
# Chúng ta đã chuyển các hàng của ma trận A thành các cột của ma trận A^T và ngược lại.
# Python cung cấp hàm `T` để tính ma trận chuyển vị của một mảng (bao gồm cả mảng một chiều là vector và mảng đa chiều là ma trận). 
# Dưới đây là một ví dụ minh họa:
# ```python
# import numpy as np
# # Một ma trận 2x3
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])
# # Tính ma trận chuyển vị của A
# A_transpose = A.T
# print("Ma trận A:")
# print(A)
# print("Ma trận chuyển vị của A:")
# print(A_transpose)
# ```
# Kết quả sẽ là:
# ```
# Ma trận A:
# [[1 2 3]
#  [4 5 6]]
# Ma trận chuyển vị của A:
# [[1 4]
#  [2 5]
#  [3 6]]
# ```
# Như bạn có thể thấy, chúng ta đã chuyển các hàng của ma trận A thành các cột của ma trận chuyển vị A.



# Phương thức `.reindex()` trong thư viện Pandas của Python được sử dụng để chỉnh lại chỉ mục (index) của một đối tượng Pandas, chẳng hạn như Series hoặc DataFrame. Điều này cho phép bạn tạo lại, thay đổi hoặc điền giá trị cho các chỉ mục mới hoặc đã tồn tại. Nếu chỉ mục mới không tồn tại trong đối tượng ban đầu, `.reindex()` sẽ điền giá trị NaN (hoặc giá trị được chỉ định bởi tham số `fill_value`) vào chỗ đó.

# Ví dụ:

# Giả sử chúng ta có một Series như sau:

# ```python
# import pandas as pd

# data = {'A': [1, 2, 3, 4, 5]}
# original_series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
# ```

# Series `original_series` có các chỉ mục là ['a', 'b', 'c', 'd', 'e'] và giá trị tương ứng là [1, 2, 3, 4, 5].

# Bây giờ, chúng ta muốn chỉnh lại chỉ mục của Series này và thêm một chỉ mục mới là 'f'. Chúng ta sẽ sử dụng `.reindex()` để làm điều đó:

# ```python
# new_index = ['a', 'b', 'c', 'd', 'e', 'f']
# reindexed_series = original_series.reindex(new_index)
# ```

# Kết quả của `reindexed_series` sẽ là:

# ```
# a    1.0
# b    2.0
# c    3.0
# d    4.0
# e    5.0
# f    NaN
# dtype: float64
# ```

# Như bạn có thể thấy, chỉ mục 'f' là mới và không tồn tại trong Series ban đầu. Vì vậy, khi sử dụng `.reindex()`, chúng ta có một chỉ mục mới và giá trị NaN được điền vào chỗ đó.

# Ngoài ra, bạn cũng có thể sử dụng tham số `fill_value` để xác định giá trị muốn điền vào các chỉ mục mới không tồn tại trong Series ban đầu:

# ```python
# reindexed_series = original_series.reindex(new_index, fill_value=0)
# ```

# Với tham số `fill_value=0`, Series `reindexed_series` sẽ trở thành:

# ```
# a    1
# b    2
# c    3
# d    4
# e    5
# f    0
# dtype: int64
# ```

# Như bạn thấy, giờ giá trị của chỉ mục 'f' là 0 thay vì NaN.



# Data Processing with Pandas là quá trình sử dụng thư viện Pandas của Python để làm sạch, biến đổi và xử lý dữ liệu trong dạng DataFrame hoặc Series. Pandas cung cấp nhiều công cụ và chức năng mạnh mẽ giúp thực hiện các tác vụ phức tạp như lọc dữ liệu, thay thế giá trị thiếu, tính toán thống kê, ghép nối các bảng dữ liệu, và nhiều tác vụ khác.

# Dưới đây là một ví dụ về Data Processing với Pandas:

# Giả sử chúng ta có một tập dữ liệu chứa thông tin về các sinh viên, gồm tên, điểm toán và điểm văn như sau:

# ```python
# import pandas as pd

# data = {
#     'Tên': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Điểm Toán': [8.5, 7.2, 6.9, 9.0, 5.5],
#     'Điểm Văn': [7.8, 6.5, 8.0, 9.2, 6.0]
# }

# df = pd.DataFrame(data)
# ```

# DataFrame `df` sẽ có dạng như sau:

# ```
#        Tên  Điểm Toán  Điểm Văn
# 0    Alice        8.5       7.8
# 1      Bob        7.2       6.5
# 2  Charlie        6.9       8.0
# 3    David        9.0       9.2
# 4      Eva        5.5       6.0
# ```

# Trong ví dụ này, chúng ta sẽ thực hiện các tác vụ Data Processing cơ bản:

# 1. Tính điểm trung bình của mỗi sinh viên:

# ```python
# df['Điểm Trung Bình'] = (df['Điểm Toán'] + df['Điểm Văn']) / 2
# ```

# Kết quả:

# ```
#        Tên  Điểm Toán  Điểm Văn  Điểm Trung Bình
# 0    Alice        8.5       7.8             8.15
# 1      Bob        7.2       6.5             6.85
# 2  Charlie        6.9       8.0             7.45
# 3    David        9.0       9.2             9.10
# 4      Eva        5.5       6.0             5.75
# ```

# 2. Lọc ra các sinh viên có điểm trung bình lớn hơn 8.0:

# ```python
# high_achievers = df[df['Điểm Trung Bình'] > 8.0]
# ```

# Kết quả:

# ```
#      Tên  Điểm Toán  Điểm Văn  Điểm Trung Bình
# 0  Alice        8.5       7.8             8.15
# 3  David        9.0       9.2             9.10
# ```

# 3. Thay đổi tên của cột 'Tên' thành 'Họ Tên':

# ```python
# df.rename(columns={'Tên': 'Họ Tên'}, inplace=True)
# ```

# Kết quả:

# ```
#    Họ Tên  Điểm Toán  Điểm Văn  Điểm Trung Bình
# 0   Alice        8.5       7.8             8.15
# 1     Bob        7.2       6.5             6.85
# 2 Charlie        6.9       8.0             7.45
# 3   David        9.0       9.2             9.10
# 4     Eva        5.5       6.0             5.75
# ```

# Đó là một số ví dụ cơ bản về Data Processing với Pandas. Thư viện Pandas còn rất nhiều tính năng và chức năng mạnh mẽ khác để thao tác với dữ liệu, giúp bạn xử lý và phân tích dữ liệu một cách dễ dàng và hiệu quả.


# Được rồi, dưới đây là một ví dụ phức tạp hơn về Data Processing với Pandas. Giả sử chúng ta có một tập dữ liệu chứa thông tin về các sản phẩm bán hàng trực tuyến, bao gồm tên sản phẩm, số lượng bán, giá tiền và ngày bán:

# ```python
# import pandas as pd

# data = {
#     'Tên Sản Phẩm': ['Áo thun', 'Quần jeans', 'Váy hoa', 'Túi xách', 'Áo sơ mi'],
#     'Số Lượng Bán': [50, 30, 25, 40, 20],
#     'Giá Tiền': [200000, 350000, 150000, 180000, 250000],
#     'Ngày Bán': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05']
# }

# df = pd.DataFrame(data)
# ```

# DataFrame `df` sẽ có dạng như sau:

# ```
#    Tên Sản Phẩm  Số Lượng Bán  Giá Tiền    Ngày Bán
# 0       Áo thun            50    200000  2023-07-01
# 1    Quần jeans            30    350000  2023-07-02
# 2        Váy hoa            25    150000  2023-07-03
# 3      Túi xách            40    180000  2023-07-04
# 4      Áo sơ mi            20    250000  2023-07-05
# ```

# Ví dụ này sẽ thực hiện các tác vụ Data Processing phức tạp hơn:

# 1. Chuyển đổi cột 'Ngày Bán' thành kiểu dữ liệu datetime:

# ```python
# df['Ngày Bán'] = pd.to_datetime(df['Ngày Bán'])
# ```

# 2. Tính tổng doanh thu của mỗi sản phẩm bán được:

# ```python
# df['Doanh Thu'] = df['Số Lượng Bán'] * df['Giá Tiền']
# ```

# Kết quả:

# ```
#    Tên Sản Phẩm  Số Lượng Bán  Giá Tiền   Ngày Bán  Doanh Thu
# 0       Áo thun            50    200000 2023-07-01   10000000
# 1    Quần jeans            30    350000 2023-07-02   10500000
# 2        Váy hoa            25    150000 2023-07-03    3750000
# 3      Túi xách            40    180000 2023-07-04    7200000
# 4      Áo sơ mi            20    250000 2023-07-05    5000000
# ```

# 3. Lọc ra các sản phẩm có doanh thu lớn hơn 8.000.000:

# ```python
# high_revenue_products = df[df['Doanh Thu'] > 8000000]
# ```

# Kết quả:

# ```
#    Tên Sản Phẩm  Số Lượng Bán  Giá Tiền   Ngày Bán  Doanh Thu
# 0       Áo thun            50    200000 2023-07-01   10000000
# 1    Quần jeans            30    350000 2023-07-02   10500000
# 3      Túi xách            40    180000 2023-07-04    7200000
# ```

# 4. Tạo báo cáo doanh thu tổng hợp theo ngày:

# ```python
# daily_revenue_report = df.groupby('Ngày Bán')['Doanh Thu'].sum().reset_index()
# ```

# Kết quả:

# ```
#     Ngày Bán  Doanh Thu
# 0 2023-07-01   10000000
# 1 2023-07-02   10500000
# 2 2023-07-03    3750000
# 3 2023-07-04    7200000
# 4 2023-07-05    5000000
# ```

# Trong ví dụ này, chúng ta đã sử dụng Pandas để chuyển đổi kiểu dữ liệu, tính toán doanh thu, lọc dữ liệu và tạo báo cáo tổng hợp. Data Processing với Pandas cho phép bạn thực hiện nhiều tác vụ xử lý dữ liệu phức tạp một cách dễ dàng và hiệu quả.


#===GROUPBY
# Phương thức `groupby` trong thư viện Pandas của Python được sử dụng để nhóm dữ liệu trong DataFrame dựa trên một hoặc nhiều cột và 
# thực hiện các phép tính tổng hợp hoặc thống kê trên từng nhóm. Kết quả của `groupby` là một đối tượng `DataFrameGroupBy`, 
# cho phép bạn áp dụng các hàm tổng hợp như `sum`, `mean`, `count`, `max`, `min`, và nhiều hàm khác để tính toán trên từng nhóm.

# Dưới đây là một ví dụ minh họa về việc sử dụng `groupby`:

# ```python
# import pandas as pd

# # Tạo DataFrame
# data = {
#     'Phòng': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B'],
#     'Số Lượng Sinh Viên': [30, 25, 15, 20, 18, 22, 16, 28],
#     'Điểm Trung Bình': [8.5, 7.2, 6.9, 9.0, 5.5, 8.0, 7.8, 6.5]
# }

# df = pd.DataFrame(data)

# # Hiển thị DataFrame
# print("DataFrame gốc:")
# print(df)

# # Nhóm dữ liệu theo cột 'Phòng' và tính tổng số lượng sinh viên trong từng phòng
# grouped_data_sum = df.groupby('Phòng')['Số Lượng Sinh Viên'].sum()
# print("\nTổng số lượng sinh viên theo phòng:")
# print(grouped_data_sum)

# # Nhóm dữ liệu theo cột 'Phòng' và tính điểm trung bình trong từng phòng
# grouped_data_mean = df.groupby('Phòng')['Điểm Trung Bình'].mean()
# print("\nĐiểm trung bình theo phòng:")
# print(grouped_data_mean)
# ```

# Kết quả:

# ```
# DataFrame gốc:
#   Phòng  Số Lượng Sinh Viên  Điểm Trung Bình
# 0     A                   30              8.5
# 1     B                   25              7.2
# 2     A                   15              6.9
# 3     B                   20              9.0
# 4     C                   18              5.5
# 5     A                   22              8.0
# 6     C                   16              7.8
# 7     B                   28              6.5

# Tổng số lượng sinh viên theo phòng:
# Phòng
# A    67
# B    73
# C    34
# Name: Số Lượng Sinh Viên, dtype: int64

# Điểm trung bình theo phòng:
# Phòng
# A    7.800000
# B    7.566667
# C    6.650000
# Name: Điểm Trung Bình, dtype: float64
# ```

# Như bạn có thể thấy, chúng ta đã sử dụng `groupby` để nhóm dữ liệu trong DataFrame `df` theo cột 'Phòng'. Sau đó, chúng ta đã tính tổng số lượng sinh viên và điểm trung bình trong từng phòng bằng cách sử dụng các hàm tổng hợp `sum` và `mean`. Điều này giúp chúng ta hiểu rõ hơn về tổng quan của dữ liệu trong từng phòng và thực hiện các phân tích tiếp theo dựa trên từng nhóm riêng biệt.
