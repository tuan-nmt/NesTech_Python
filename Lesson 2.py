import numpy as np

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



