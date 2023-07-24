import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[5, 12, 17, 9, 3], [13, 4, 8, 14, 1], [9, 6, 3, 7, 21]])
arr1 = np.array([3, 4, 7, 8, 1, 2, 3])
arr2 = np.array(3)

# print(arr)
# print(arr1)
# print(arr2)

# print(arr.shape)

# print(arr.dtype)

# arr_reshape53 = arr.reshape(5,3)
# print(arr)
# print(arr_reshape53)

# print(arr1[3])
# print(arr[1,3])
# print(arr[2][1])
# print(arr[2, 1])

# print(arr1[2:5])
# print(arr[:, 1:3])



# 1. Addition: Phép cộng `+` (Thực hiện phép cộng từng phần tử giữa hai mảng hoặc một mảng và một số vô hướng).

# 2. Subtraction: Phép trừ `-` (Thực hiện phép trừ từng phần tử giữa hai mảng hoặc một mảng và một số vô hướng).

# 3. Multiplication: Phép nhân `*` (Thực hiện phép nhân từng phần tử giữa hai mảng hoặc một mảng và một số vô hướng).

# 4. Division: Phép chia `/` (Thực hiện phép chia từng phần tử giữa hai mảng hoặc một mảng và một số vô hướng).

# 5. Floor Division: Phép chia lấy phần nguyên `//` (Thực hiện phép chia lấy phần nguyên từng phần tử giữa hai mảng hoặc một mảng và một số vô hướng).

# 6. Exponentiation: Phép luỹ thừa `**` (Thực hiện phép luỹ thừa từng phần tử giữa hai mảng hoặc một mảng và một số vô hướng).

# 7. Modulus: Phép chia lấy phần dư `%` (Thực hiện phép chia lấy phần dư từng phần tử giữa hai mảng hoặc một mảng và một số vô hướng).

# Những phép toán này được thực hiện trên các mảng NumPy và tuân theo các quy tắc broadcasting của NumPy để thực hiện phép toán từng phần tử khi các mảng có kích thước khác nhau. 
# Hãy nhớ nhập thư viện NumPy (`import numpy as np`) trước khi sử dụng các toán tử này trong mã của bạn.


# ======================================================================================================================================
# Quy tắc broadcasting của NumPy cho phép thực hiện các phép toán giữa các mảng có kích thước khác nhau một cách linh hoạt. 
# Khi bạn thực hiện phép toán giữa hai mảng, NumPy sẽ tự động mở rộng kích thước của các mảng để chúng có cùng kích thước hoặc có kích thước tương thích để thực hiện phép toán từng phần tử.

# Quy tắc broadcasting của NumPy tuân theo các nguyên tắc sau:
# 1. Nếu hai mảng có số chiều (số trục) khác nhau, thêm các chiều có kích thước 1 vào phía trước của mảng có số chiều nhỏ hơn cho đến khi số chiều của cả hai mảng bằng nhau.
# 2. Nếu kích thước của các chiều tương ứng của các mảng không giống nhau, nhưng một trong số chúng có kích thước là 1, 
# NumPy sẽ tự động sao chép dữ liệu để mở rộng kích thước của mảng có kích thước 1 để tạo các mảng có kích thước tương thích cho phép thực hiện phép toán từng phần tử.
# 3. Nếu các kích thước của các chiều tương ứng của các mảng không giống nhau và không có một trong số chúng có kích thước là 1, 
# thì quá trình broadcasting sẽ không thể thực hiện và sẽ gây ra lỗi.

# Dưới đây là ví dụ để minh họa quy tắc broadcasting:

# ```python
# import numpy as np

# # Mảng có kích thước (3, 1)
# arr1 = np.array([[1], [2], [3]])

# # Mảng có kích thước (3,)
# arr2 = np.array([10, 20, 30])

# # Sử dụng broadcasting để thực hiện phép cộng từng phần tử
# result = arr1 + arr2

# # Kết quả:
# # array([[11, 21, 31],
# #        [12, 22, 32],
# #        [13, 23, 33]])
# ```

# Trong ví dụ trên, mảng `arr1` có kích thước (3, 1) và mảng `arr2` có kích thước (3,). Theo quy tắc broadcasting, mảng `arr2` sẽ được mở rộng thêm một chiều có kích thước 1 để trở thành mảng có kích thước (3, 1), sau đó, phép cộng từng phần tử được thực hiện giữa hai mảng này.


# In NumPy, a powerful library for numerical computing in Python, you can perform various arithmetic operations on arrays and numerical data. 
# Here are some of the common arithmetic operators you can use in NumPy:

# 1. Addition: `+`
#    It performs element-wise addition between two arrays or an array and a scalar.

#    ```python
#    import numpy as np

#    arr1 = np.array([1, 2, 3])
#    arr2 = np.array([4, 5, 6])

#    result = arr1 + arr2
#    # Output: array([5, 7, 9])
#    ```

# 2. Subtraction: `-`
#    It performs element-wise subtraction between two arrays or an array and a scalar.

#    ```python
#    import numpy as np

#    arr1 = np.array([10, 20, 30])
#    arr2 = np.array([2, 4, 6])

#    result = arr1 - arr2
#    # Output: array([ 8, 16, 24])
#    ```

# 3. Multiplication: `*`
#    It performs element-wise multiplication between two arrays or an array and a scalar.

#    ```python
#    import numpy as np

#    arr1 = np.array([1, 2, 3])
#    arr2 = np.array([4, 5, 6])

#    result = arr1 * arr2
#    # Output: array([ 4, 10, 18])
#    ```

# 4. Division: `/`
#    It performs element-wise division between two arrays or an array and a scalar.

#    ```python
#    import numpy as np

#    arr1 = np.array([10, 20, 30])
#    arr2 = np.array([2, 4, 6])

#    result = arr1 / arr2
#    # Output: array([ 5.,  5.,  5.])
#    ```

# 5. Floor Division: `//`
#    It performs element-wise floor division between two arrays or an array and a scalar. The result will be the quotient with the fractional part truncated.

#    ```python
#    import numpy as np

#    arr1 = np.array([10, 20, 30])
#    arr2 = np.array([2, 4, 6])

#    result = arr1 // arr2
#    # Output: array([5, 5, 5])
#    ```

# 6. Exponentiation: `**`
#    It performs element-wise exponentiation between two arrays or an array and a scalar.

#    ```python
#    import numpy as np

#    arr = np.array([2, 3, 4])

#    result = arr ** 3
#    # Output: array([ 8, 27, 64])
#    ```

# 7. Modulus: `%`
#    It performs element-wise modulus between two arrays or an array and a scalar.

#    ```python
#    import numpy as np

#    arr1 = np.array([10, 20, 30])
#    arr2 = np.array([3, 6, 9])

#    result = arr1 % arr2
#    # Output: array([1, 2, 3])
#    ```

# These arithmetic operators work on NumPy arrays, and they follow the broadcasting rules of NumPy to perform element-wise operations when arrays have different shapes. 
# Remember to import NumPy (`import numpy as np`) before using these operators in your code.

# import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4])
# arr3 = np.array([4, 2])
# arr4 = np.array(4)

# result = arr1 + arr2
# print(result)

# Error
# result1 = arr1 + arr3
# print(result1)

# Error
# result2 = arr1 + arr3
# print(result)

# result = arr1 * arr2
# print(result)

# Error
# result1 = arr1 * arr3
# print(result1)

# Error
# result2 = arr1 * arr3
# print(result)

# a = np.array([1, 2, 3])
# b = np.array([0, 3, 2])

# result = a > b
# print(result)

# result1 = np.where(b > a, 1, 2)
# print(result1)

# np.save('arr_save.npy', arr)
# arr = np.load('arr_save.npy')
# print(arr)

# np.savetxt('array_text.txt', arr, delimiter=",")
# arr = np.loadtxt('array_text.txt', delimiter=",")
# print(arr)


# # Hàm mô phỏng việc tung đồng xu và đi trên đường
# def simulate():
#     position = 0
#     for i in range(100):
#         if np.random.random() < 0.5:
#             position += 1
#         else:
#             position -= 1
#     return position

# # Hàm tính xác suất anh ta tiến được 30 bước
# def calculate_probability(n_trials):
#     count = 0
#     for i in range(n_trials):
#         if simulate() >= 30:
#             count += 1
#     return count / n_trials

# # Thực hiện tính xác suất
# print("Xác suất anh ta tiến được 30 bước:", calculate_probability(10000))



# ---------------Pandas---------------
import pandas as pd 

# ser = pd.Series(['A', 'B', 'C', 'D', 'E'], index=[1, 2, 3, 4 , 5])
# print(ser)

# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# ser2 = pd.Series(sdata)
# print(ser2)

# ser2 = pd.Series(sdata, index=["Ohio", "Texas", "Cali"])
# print(ser2)

# print(ser[1])
# print(ser[[1, 2, 3]])
# print(ser[ser == 'A'])

# # DataFrame
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year':  [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = pd.DataFrame(data)
# print(frame)

# frame_1 = pd.DataFrame(data, columns = ['year', 'state', 'pop', 'debt'], index = ['one', 'two', 'three', 'four', 'five'])
# print(frame_1)


# # Tạo ndarray 2 chiều với 3 dòng và 4 cột
# data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# # Tạo DataFrame từ ndarray
# df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
# # In ra DataFrame
# print(df)

# data_1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# # Tạo DataFrame từ ndarray
# df_1 = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
# # In ra DataFrame
# print(df_1)


# # tạo một từ điển chứa các arrays để tạo Dataframe
# data = {'name': ['John', 'Tom', 'Marry', 'David'],
#         'age': [25, 28, 31, 35],
#         'salary': [35000, 42000, 50000, 55000]}

# # tạo Dataframe từ từ điển
# df = pd.DataFrame(data)

# # in ra Dataframe
# print(df)


# # tạo mảng cấu trúc Numpy với tên cột và kiểu dữ liệu
# data = np.array([(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)],
#                 dtype=[('id', int), ('name', 'U10'), ('age', int)])
# # tạo DataFrame từ mảng cấu trúc Numpy
# df = pd.DataFrame(data)
# # in ra DataFrame
# print(df)


# data = {'Name': pd.Series(['Alice', 'Bob', 'Charlie']),
#         'Age': pd.Series([25, 30, 35]),
#         'Nationality': pd.Series(['US', 'UK', 'Canada'])}
# df = pd.DataFrame(data)
# print(df)


# data = {'fruit': {'apple': 3, 'banana': 2, 'orange': 5},
#         'color': {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}}
# df = pd.DataFrame(data)
# print(df)


# data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}]
# df = pd.DataFrame(data)
# print(df)


# data = [['John', 28, 'Engineer'],
#         ['Alice', 25, 'Doctor'],
#         ['Bob', 32, 'Lawyer']]
# df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
# print(df)


# # Tạo DataFrame gốc
# df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
# # Tạo DataFrame mới từ DataFrame gốc
# df2 = pd.DataFrame(df1, columns=['a', 'c'])
# print(df2)


# data = np.array([[1, 2, 3], [4, np.nan, 6], [7, 8, np.nan]])
# mask = np.ma.masked_invalid(data)
# print(mask)
# df = pd.DataFrame(mask)
# print(df)


# data = np.array([[1, 2, 3], [4, np.nan, 6], [7, 8, np.nan]])
# mask = np.ma.masked_invalid(data)
# print(mask)
# df = pd.DataFrame(mask)
# print(df)


# print(frame_1['year'])
# print(frame_1[['year', 'pop']])
# print(frame_1.loc["three"])
# print(frame_1.loc[["three", "two"]])


# print("Before")
# print(frame)
# frame['year'] = 1996 
# print("After")
# print(frame)

# print("Before")
# print(frame)
# frame['year'] = [1996, 1997, 1998, 1999, 2000] 
# print("After")
# print(frame)

# print("Before")
# print(frame)
# frame['year'] = pd.Series([1996, 1998, 2001], index = [0, 1, 3])
# print("After")
# print(frame)

# print(ser2.index)
# print(frame_1.index)


# data = {'name': ['John', 'Alice', 'Bob'],
#         'age': [25, 30, 35],
#         'city': ['New York', 'London', 'Paris']}
# df = pd.DataFrame(data)
# print("----------------------------")
# print(df)
# df[['name', 'age']] = pd.DataFrame({'name': ['Mike', 'Eve', 'Steve'], 'age': [20, 27, 32]})
# print("----------------------------")
# print(df)
# print("-------------name---------------")
# print(df['name'])


# data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#         'age': [25, 32, 18, 47, 22],
#         'country': ['USA', 'Canada', 'UK', 'USA', 'Australia']}
# df = pd.DataFrame(data)


# data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#         'age': [25, 32, 18, 47, 22],
#         'country': ['USA', 'Canada', 'UK', 'USA', 'Australia']}
# df = pd.DataFrame(data)
# print( df.loc[[1,3], ['name', 'age']])


# data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#         'age': [25, 30, 35, 40, 45],
#         'city': ['NY', 'LA', 'SF', 'NY', 'SF']}
# df = pd.DataFrame(data)
# print(df.loc[:, ['name', 'age']])


# data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#         'age': [25, 32, 18, 47, 22],
#         'city': ['New York', 'Paris', 'London', 'Berlin', 'Sydney']}
# df = pd.DataFrame(data)
# print(df.iloc[:, [0, 2]])


# data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'age': [25, 32, 18, 47],
#         'city': ['New York', 'Paris', 'Berlin', 'London'],
#         'salary': [50000, 80000, 20000, 120000]}
# df = pd.DataFrame(data)
# print(df.iloc[[1,3], [1,2]])


# print(df.at[2, 'age'])


# # Tạo DataFrame
# data = {'name': ['John', 'Emma', 'Peter', 'Lauren'],
#         'age': [25, 27, 22, 30],
#         'country': ['USA', 'Canada', 'Australia', 'UK']}
# df = pd.DataFrame(data) 
# # Truy cập giá trị tại dòng 1 (Emma) và cột 'age'
# value = df.iat[1, 1]
# print(value)  # Output: 27


# data = {'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [25, 30, 35],
#         'salary': [50000, 70000, 90000]}
# # Tạo DataFrame từ dictionary
# df = pd.DataFrame(data)
# # In ra DataFrame gốc
# print("Original DataFrame:\n", df)
# # Tạo một danh sách chỉ số mới
# new_index = [0, 1, 2, 3]
# # Áp dụng phương thức reindex để tạo DataFrame mới với chỉ số mới
# new_df = df.reindex(new_index)
# # In ra DataFrame mới
# print("\nNew DataFrame with reindexed index:\n", new_df)


# data = {'state': ['Ohio', 'Nevada', 'California'],
#         'year': [2000, 2001, 2002],
#         'pop': [1.5, 2.4, 3.0]}
# df = pd.DataFrame(data)
# print("Origin")
# print(df)
# # Tạo lại index mới
# new_index = ['a', 'b', 'c']
# df_reindexed = df.reindex(new_index)
# print(df_reindexed)
# # Tạo lại cả index và columns mới
# new_index = ['a', 'b', 'c']
# new_columns = ['state', 'year', 'pop', 'debt']
# df_reindexed = df.reindex(new_index, columns=new_columns)
# print(df_reindexed)
# # Tạo lại index mới và điền giá trị bị thiếu bằng 0
# new_index = ['a', 'b', 'c', 'd']
# df_reindexed = df.reindex(new_index, fill_value=0)
# print(df_reindexed)


# data = {'name': ['John', 'Paul', 'George', 'Ringo'],
#         'age': [40, 38, 36, 34],
#         'instrument': ['guitar', 'bass', 'guitar', 'drums']}  
# df = pd.DataFrame(data)
# # loại bỏ cột instrument
# df = df.drop(columns=['instrument'])
# print(df)


# data = {'name': ['John', 'Mary', 'Peter', 'Jane', 'Tom'],
#         'age': [30, np.nan, 25, 40, 35],
#         'gender': ['M', 'F', np.nan, 'F', 'M'],
#         'income': [50000, 60000, np.nan, 70000, 80000]}

# df = pd.DataFrame(data)

# # Loại bỏ các hàng có ít nhất một giá trị NaN
# df_dropped = df.dropna()
# print(df_dropped)

# # Loại bỏ các cột có ít nhất một giá trị NaN
# df_dropped_cols = df.dropna(axis=1)
# print(df_dropped_cols)

# # Chỉ giữ lại các hàng có ít nhất 3 giá trị không phải NaN
# df_threshold = df.dropna(thresh=3)
# print(df_threshold)


# data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'age': [20, np.nan, 25, 30],
#         'gender': ['F', 'M', np.nan, 'M']}

# df = pd.DataFrame(data)

# # điền giá trị vào ô dữ liệu bị thiếu bằng 0
# df_filled = df.fillna(0)
# print(df_filled)

# # điền giá trị vào ô dữ liệu bị thiếu bằng giá trị trước đó
# df_ffill = df.fillna(method='ffill')
# print(df_ffill)

# # điền giá trị vào ô dữ liệu bị thiếu bằng giá trị sau đó
# df_bfill = df.fillna(method='bfill')
# print(df_bfill)


# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# def square(x):
#     return x ** 2
# # Áp dụng hàm square cho mỗi phần tử trong DataFrame
# df_squared = df.apply(square)
# print(df_squared)
# # Áp dụng hàm sum cho mỗi cột trong DataFrame
# df_sum = df.apply(sum, axis=0)
# print(df_sum)
# # Áp dụng hàm mean cho mỗi hàng trong DataFrame
# df_mean = df.apply(lambda x: x.mean(), axis=1)
# print(df_mean)


# df = pd.DataFrame(np.random.randint(0, 10, (5,5)), index=[4,2,1,5,3], columns=['a','d','c','b','e'])
# print("Before")
# print(df)
# print("After")
# df.sort_index(inplace=True)
# print(df)


# Multiple Linear Regression là một phương pháp trong thống kê và học máy, 
# được sử dụng để dự đoán giá trị của một biến phụ thuộc dựa trên nhiều biến độc lập (đặc trưng). 
# Nó mở rộng ý tưởng của Linear Regression (phương trình đường thẳng) để mô hình hóa mối quan hệ tuyến tính giữa biến phụ thuộc và 
# nhiều biến độc lập. Khi chúng ta có nhiều biến đầu vào trong dự đoán, việc sử dụng Multiple Linear Regression có thể giúp cải thiện hiệu suất mô hình.

# Ví dụ, giả sử chúng ta muốn dự đoán giá nhà dựa trên diện tích, số phòng ngủ và khoảng cách đến trung tâm thành phố. 
# Trong trường hợp này, diện tích, số phòng ngủ và khoảng cách là ba biến độc lập và giá nhà là biến phụ thuộc.

# # Dữ liệu mẫu
# # Diện tích (đơn vị: m2)
# X1 = np.array([70, 85, 120, 100, 90, 75, 60, 110, 95, 80])

# # Số phòng ngủ
# X2 = np.array([2, 3, 4, 3, 2, 2, 1, 3, 3, 2])

# # Khoảng cách đến trung tâm thành phố (đơn vị: km)
# X3 = np.array([5, 3, 10, 8, 7, 6, 12, 9, 4, 6])

# # Giá nhà (đơn vị: tỷ VND)
# Y = np.array([3, 4, 5, 4.5, 4, 3.5, 2.5, 5, 4.5, 3.8])

# # Hợp nhất các biến độc lập thành một ma trận dữ liệu
# X = np.column_stack((X1, X2, X3))

# # Thêm cột bias vào ma trận X
# X = np.column_stack((np.ones(len(X)), X))

# # Tính toán tham số w (weights)
# w = np.linalg.inv(X.T @ X) @ X.T @ Y

# print("Tham số w (weights):", w)
# # Giá trị mới của các biến độc lập cho việc dự đoán
# new_X1 = 95
# new_X2 = 3
# new_X3 = 6

# # Thêm cột bias vào giá trị mới của biến độc lập
# new_X = np.array([1, new_X1, new_X2, new_X3])

# # Dự đoán giá nhà mới
# predicted_price = np.dot(new_X, w)

# print("Giá nhà dự đoán cho các giá trị mới:")
# print("Diện tích:", new_X1, "m2")
# print("Số phòng ngủ:", new_X2)
# print("Khoảng cách đến trung tâm thành phố:", new_X3, "km")
# print("Dự đoán giá nhà:", predicted_price, "tỷ VND")

# # Dữ liệu mẫu thực tế về giá nhà
# actual_prices = np.array([3, 4, 5, 4.5, 4, 3.5, 2.5, 5, 4.5, 3.8])

# # Giá nhà dự đoán cho các giá trị mới
# predicted_prices = np.dot(X, w)

# # Vẽ biểu đồ
# plt.figure(figsize=(8, 6))
# plt.scatter(np.arange(len(actual_prices)), actual_prices, label='Thực tế', color='blue', marker='o')
# plt.plot(np.arange(len(predicted_prices)), predicted_prices, label='Dự đoán', color='red', linestyle='dashed', marker='x')
# plt.xticks(np.arange(len(actual_prices)), np.arange(1, len(actual_prices) + 1))
# plt.xlabel('Mẫu dữ liệu')
# plt.ylabel('Giá nhà (tỷ VND)')
# plt.legend()
# plt.title('Biểu đồ dự đoán giá nhà bằng Multiple Linear Regression')
# plt.grid(True)
# plt.show()


#======Sử dụng sklearn =========
# pip install scikit-learn

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Dữ liệu mẫu
# X1 = np.array([70, 85, 120, 100, 90, 75, 60, 110, 95, 80])
# X2 = np.array([2, 3, 4, 3, 2, 2, 1, 3, 3, 2])
# X3 = np.array([5, 3, 10, 8, 7, 6, 12, 9, 4, 6])
# Y = np.array([3, 4, 5, 4.5, 4, 3.5, 2.5, 5, 4.5, 3.8])

# # Biến đổi dữ liệu thành ma trận đặc trưng
# X = np.column_stack((X1, X2, X3))
# print("column_stack")
# print(X)

# # Tạo mô hình Linear Regression
# model = LinearRegression()

# # Huấn luyện mô hình trên dữ liệu
# model.fit(X, Y)

# # Giá trị mới của các biến độc lập cho việc dự đoán
# new_X = np.array([[95, 3, 6]])

# # Dự đoán giá nhà mới
# predicted_price = model.predict(new_X)

# print("Giá nhà dự đoán cho các giá trị mới:")
# print("Diện tích:", new_X[0, 0], "m2")
# print("Số phòng ngủ:", new_X[0, 1])
# print("Khoảng cách đến trung tâm thành phố:", new_X[0, 2], "km")
# print("Dự đoán giá nhà:", predicted_price[0], "tỷ VND")

# # Vẽ biểu đồ
# predicted_prices = model.predict(X)
# plt.figure(figsize=(8, 6))
# plt.scatter(np.arange(len(Y)), Y, label='Thực tế', color='blue', marker='o')
# plt.plot(np.arange(len(predicted_prices)), predicted_prices, label='Dự đoán', color='red', linestyle='dashed', marker='x')
# plt.xticks(np.arange(len(Y)), np.arange(1, len(Y) + 1))
# plt.xlabel('Mẫu dữ liệu')
# plt.ylabel('Giá nhà (tỷ VND)')
# plt.legend()
# plt.title('Biểu đồ dự đoán giá nhà bằng Multiple Linear Regression')
# plt.grid(True)
# plt.show()



# from sklearn.datasets import load_breast_cancer
# data = load_breast_cancer()
# # print(data)
# data_df = pd.DataFrame(data = data.data, columns = data.feature_names)
# # print(data_df.head().T)
# print(data_df.dtypes)
# print(data_df.describe())
# print(data_df.groupby(by=['class', 'doctor_name']).size())

# filename = 'breast-cancer-wisconsin.csv'
# df = pd.read_csv(filename)
# print(df)
# print(df.dtypes)
# print(df.describe())
# print(df.groupby(by=['class', ]))
# print(df.isna().sum())
# print(df.nunique())
# print(df[df.duplicated(subset='id', keep=False)].sort_values('id'))
# Mã `df[df.duplicated(subset='id', keep=False)].sort_values('id')` có ý nghĩa là:
# 1. `df`: Đây là tên của DataFrame, trong đó DataFrame là một kiểu dữ liệu bảng hai chiều trong thư viện Pandas của Python.
# 2. `df.duplicated(subset='id', keep=False)`: Đây là một phương thức của DataFrame dùng để tạo một Series boolean chỉ ra xem mỗi hàng có bị trùng lặp theo cột 'id' hay không. 
# Nếu hàng đó là một bản sao (duplicate) của hàng trước đó, thì nó được đánh dấu là True, ngược lại nó là False. Tham số `subset='id'` xác định rằng chỉ cột 'id' được sử dụng để xác định trùng lặp.
# 3. `keep=False`: Đối số này nói cho phương thức biết không giữ giá trị đầu tiên của hàng trùng lặp, nghĩa là đánh dấu tất cả các bản sao sau đó (cùng giá trị 'id') là True. 
# Nếu `keep=True`, thì chỉ có hàng đầu tiên trong các bản sao được đánh dấu là True.
# 4. `sort_values('id')`: Sau khi có Series boolean chỉ ra các hàng trùng lặp dựa trên cột 'id', ta tiến hành sắp xếp các hàng theo cột 'id'.
# Vì vậy, mã trên sẽ trả về một DataFrame mới chứa các hàng bị trùng lặp dựa trên cột 'id', sắp xếp theo thứ tự của cột 'id'. Các hàng bị trùng lặp này có thể là các bản sao hoặc nhiều bản sao của nhau trong DataFrame gốc.

# repeat_patients = df.groupby(by='id').size().sort_values(ascending=False)
# print(repeat_patients)
# filtered_patients = repeat_patients[repeat_patients > 2].to_frame().reindex()
# print(filtered_patients)
# filtered_df = df[~df.id.isin(filtered_patients.id)]



# KHÁM PHÁ DỮ LIỆU VÀ ĐỔI TÊN CỘT
# Trước hết, hãy xem các hàng đầu tiên trong tập dữ liệu để xem nó trông như thế nào:
df = pd.read_csv('titanic.csv')
print(df.head(3))
# Lưu ý:
# Bằng cách nhập một số vào trong ngoặc, chẳng hạn như df.head(3), bạn chỉ định số lượng cột sẽ được hiển thị.
# Nếu bạn để trống, nó sẽ hiển thị năm hàng đầu tiên theo mặc định.

# KIỂM TRA VÀ CHỌN CỘT
# Tiếp theo, hãy kiểm tra xem chúng ta có những cột nào.
print(df.columns)

# Sau đó, chúng ta có thể chỉ định cột nào sẽ sử dụng. Để làm điều đó, chúng tôi chọn các cột. Ví dụ
select_cols = ['Survived', 'Pclass', 'Name', 'Sex', 'Fare']
df_with_select_cols = df[select_cols]

# Sau đó, chúng ta có thể in năm hàng và kiểu dữ liệu cuối cùng để xem khung dữ liệu mới trông như thế nào.
print(df_with_select_cols.tail())
print(df_with_select_cols.dtypes)


# THAY ĐỔI TÊN CỘT
# Hãy thay đổi tên của các cột. Chúng tôi sẽ làm việc trên dữ liệu gốc của mình với tám cột.
new_columns_names = {'Survived': 'SURVIVED', 'Pclass': 'PCLASS', 'Name': 'NAME', 'Sex': 'SEX', 'Age': 'AGE', 'Siblings/Spouses Aboard': 'SIBSA', 'Parents/Children Aboard': 'PARCA', 'Fare': 'FARE'}
print(new_columns_names)

# Như có thể thấy ở trên, chúng ta đã tạo từ điển thành công. 
# Bây giờ, chúng ta có thể thay đổi tên của các cột, bằng cách chuyển dict đó vào các cột tham số trong rename().

df = df.rename(columns=new_columns_names)
print(df.columns)

# MÔ TẢ DỮ LIỆU
print(df.describe())

# Hãy kiểm tra một số thống kê cơ bản để hiểu rõ hơn về dữ liệu của chúng tôi.
# Các chức năng mô tả cung cấp cho chúng tôi số liệu thống kê mô tả tóm tắt số lượng, giá trị trung bình, độ lệch chuẩn, tối thiểu. giá trị cực đại và lượng tử. 
# Giá trị NaN được bỏ qua theo mặc định.

# GIÁ TRỊ BỊ MÂT
# Pandas treat None and NaN để chỉ ra các giá trị bị thiếu hoặc rỗng trong dữ liệu. 
# Có nhiều chức năng khác nhau để phát hiện các giá trị bị thiếu trong Pandas DataFrame, chẳng hạn như:
# isnull()
# notnull()

print(df.isnull())

# Lưu ý:
# hàm df.isnull() hiển thị tất cả các giá trị trong dữ liệu là Đúng hoặc Sai. Các giá trị True đại diện cho các giá trị null.
# df.notnull() làm ngược lại chức năng này.

# Sử dụng any(), chúng ta có thể xem tóm tắt của từng cột về việc liệu có bất kỳ giá trị nào bị thiếu hay không.

print(df.isnull().any())
print(df.isnull().any(axis=1))

# Tuy nhiên, nếu chúng ta muốn sử dụng hàm “isnull()” để hiển thị tất cả các hàng trong đó df có giá trị null thì sao? 
# Nói cách khác, điều gì sẽ xảy ra nếu chúng ta muốn hiển thị các hàng thực tế có giá trị null thay vì df này với các ô Đúng hoặc Sai. 
# Để làm điều đó, chúng tôi viết mã sau đây:

print(df[df.isnull().any(axis=1)].head())


# LẶP QUA CÁC HÀNG VÀ CỘT
# Hãy bắt đầu với việc lặp lại các hàng và sử dụng các hàm tự tạo. 
# Để lặp lại các hàng ném, chúng ta sử dụng hàm iterrows(). Xem ví dụ dưới đây.

count = 0 
for x, row in df.iterrows():
    print('Index', x)
    print(row)
    count += 1
    if count == 3:
        break

# Để lặp lại các cột ném, chúng ta sử dụng hàm iteritems(). Xem ví dụ dưới đây
count = 0 
for x, col in df.items():
    print('Index', x)
    print(col.head())
    count += 1
    if count == 3:
        break


# NHÓM
# Hàm pandas groupby() được sử dụng để chia dữ liệu thành các nhóm dựa trên tiêu chí. 
# Nói cách khác, phân nhóm được sử dụng để cung cấp ánh xạ nhãn tới tên nhóm.
# Hãy nhóm dữ liệu của chúng tôi theo PCLASS.

# print(df.groupby('PCLASS').mean()) #warning 
print(df.groupby('PCLASS').mean(numeric_only=True))

# Để tiếp tục PCLASS dưới dạng một cột, hãy sử dụng reset_index.
print(df.groupby('PCLASS').sum().reset_index().head())
# Chúng ta có thể vẽ biểu đồ khung dữ liệu được trả về.
df.groupby('PCLASS').mean(numeric_only=True).plot(kind='bar')
plt.show()


# NỐI
# Pandas cung cấp một số chức năng để dễ dàng kết hợp DataFrame. Một trong những chức năng này là concat().
# Có tám cột trong khung dữ liệu của chúng tôi là SURVIVED, PCLASS, NAME, SEX, AGE, SIBSA, PARCA và FARE. 
# Hãy tạo ba khung dữ liệu khác nhau từ khung dữ liệu (df) của chúng ta, sau đó nối chúng với hàm concat().

print(df.columns)
df1 = df[['SURVIVED', 'PCLASS', 'NAME']]
df2 = df[['SEX', 'AGE', 'SIBSA']]
df3 = df[['PARCA', 'FARE']]

print(df1.head(2))
print(df2.head(2))
print(df3.head(2))

# Bây giờ, chúng tôi có ba khung dữ liệu khác nhau.
frames = [df1, df2, df3]
combined_df = pd.concat(frames, axis=1)
print(combined_df.head(5))

# Một cách khác để kết hợp DataFrame là sử dụng các phương thức cá thể append(). Chúng nối dọc theo trục = 0.

