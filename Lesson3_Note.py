# Dưới đây là các ví dụ minh họa về cách sử dụng các phương thức đọc dữ liệu trong Pandas:

# 1. Đọc dữ liệu từ file CSV sử dụng `pd.read_csv()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ file CSV và tạo DataFrame
# df_csv = pd.read_csv('data.csv')
# ```

# 2. Đọc dữ liệu từ file Excel sử dụng `pd.read_excel()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ file Excel và tạo DataFrame
# df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
# ```

# 3. Đọc dữ liệu từ file JSON sử dụng `pd.read_json()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ file JSON và tạo DataFrame
# df_json = pd.read_json('data.json')
# ```

# 4. Đọc dữ liệu từ trang web có bảng HTML sử dụng `pd.read_html()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ trang web có bảng HTML và tạo danh sách các DataFrame
# dfs_html = pd.read_html('https://example.com/table')
# df_html = dfs_html[0]  # Chọn DataFrame thích hợp nếu có nhiều bảng trên trang
# ```

# 5. Đọc dữ liệu từ clipboard (sao chép và dán) sử dụng `pd.read_clipboard()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ clipboard và tạo DataFrame
# df_clipboard = pd.read_clipboard()
# ```

# 6. Đọc dữ liệu từ cơ sở dữ liệu SQL sử dụng `pd.read_sql()`:

# ```python
# import pandas as pd
# import sqlite3

# # Kết nối cơ sở dữ liệu SQL
# conn = sqlite3.connect('example.db')

# # Đọc dữ liệu từ cơ sở dữ liệu SQL và tạo DataFrame
# query = 'SELECT * FROM table_name'
# df_sql = pd.read_sql(query, conn)
# ```

# 7. Đọc dữ liệu từ BigQuery (Google BigQuery) sử dụng `pd.read_gbq()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ BigQuery và tạo DataFrame
# project_id = 'your_project_id'
# query = 'SELECT * FROM dataset.table'
# df_gbq = pd.read_gbq(query, project_id=project_id)
# ```

# 8. Đọc dữ liệu từ file Parquet sử dụng `pd.read_parquet()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ file Parquet và tạo DataFrame
# df_parquet = pd.read_parquet('data.parquet')
# ```

# 9. Đọc dữ liệu từ file Feather sử dụng `pd.read_feather()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ file Feather và tạo DataFrame
# df_feather = pd.read_feather('data.feather')
# ```

# 10. Đọc dữ liệu từ file pickle sử dụng `pd.read_pickle()`:

# ```python
# import pandas as pd

# # Đọc dữ liệu từ file pickle và tạo DataFrame hoặc Series
# df_pickle = pd.read_pickle('data.pickle')
# ```

# Lưu ý rằng các tùy chọn thêm có thể được sử dụng với mỗi phương thức này để điều chỉnh cách dữ liệu được đọc và xử lý.


# Trong thư viện Pandas, các phương thức `dropna()`, `fillna()`, `isnull()` và `notnull()` liên quan đến việc làm việc với giá trị null (NaN) trong DataFrame hoặc Series. Dưới đây là ý nghĩa của từng phương thức:

# 1. `dropna()`: Phương thức `dropna()` được sử dụng để loại bỏ các hàng hoặc cột có chứa giá trị null (NaN) từ DataFrame. Điều này giúp làm sạch và chuẩn hóa dữ liệu trước khi tiến hành phân tích. Phương thức này trả về một DataFrame mới với các giá trị null bị loại bỏ.

# ```python
# import pandas as pd

# # Tạo DataFrame có giá trị null
# data = {'A': [1, 2, None, 4],
#         'B': [5, None, 7, 8]}
# df = pd.DataFrame(data)

# # Loại bỏ các hàng có giá trị null
# df_cleaned = df.dropna()

# print(df_cleaned)
# ```

# 2. `fillna()`: Phương thức `fillna()` được sử dụng để điền các giá trị null (NaN) bằng giá trị khác trong DataFrame hoặc Series. Điều này giúp điền các khoảng trống dữ liệu bằng giá trị mặc định hoặc giá trị được tính toán từ dữ liệu hiện có.

# ```python
# import pandas as pd

# # Tạo DataFrame có giá trị null
# data = {'A': [1, 2, None, 4],
#         'B': [5, None, 7, 8]}
# df = pd.DataFrame(data)

# # Điền các giá trị null bằng giá trị mặc định là 0
# df_filled = df.fillna(0)

# print(df_filled)
# ```

# 3. `isnull()`: Phương thức `isnull()` trả về một DataFrame hoặc Series có cùng kích thước với đối tượng gốc, nhưng các phần tử sẽ là giá trị boolean (True hoặc False) tương ứng với việc có giá trị null (NaN) hoặc không.

# ```python
# import pandas as pd

# # Tạo Series có giá trị null
# data = pd.Series([1, None, 3, None, 5])

# # Kiểm tra các phần tử có giá trị null
# is_null = data.isnull()

# print(is_null)
# ```

# 4. `notnull()`: Phương thức `notnull()` tương tự như `isnull()`, nhưng trả về các giá trị boolean tương ứng với việc có giá trị (không phải null) hoặc không.

# ```python
# import pandas as pd

# # Tạo Series có giá trị null
# data = pd.Series([1, None, 3, None, 5])

# # Kiểm tra các phần tử có giá trị (không phải null)
# not_null = data.notnull()

# print(not_null)
# ```

# Các phương thức này giúp bạn dễ dàng kiểm tra và xử lý các giá trị null trong dữ liệu và làm cho quá trình xử lý và phân tích dữ liệu trở nên dễ dàng hơn.


# Trong thư viện Pandas, `pd.cut()` là một phương thức được sử dụng để chia các giá trị dữ liệu thành các nhóm rời rạc dựa trên các khoảng giá trị đã xác định trước. Phương thức này thường được sử dụng để biến đổi dữ liệu liên tục thành các dữ liệu rời rạc, giúp bạn phân loại dữ liệu và thực hiện các phân tích thống kê dựa trên các nhóm đó.

# Cú pháp của `pd.cut()` như sau:

# ```python
# pd.cut(x, bins, labels=None, right=True, include_lowest=False)
# ```

# Các tham số chính:

# - `x`: Dữ liệu đầu vào, có thể là một Series hoặc một list chứa dữ liệu cần phân loại.
# - `bins`: Các khoảng giá trị sẽ được sử dụng để chia dữ liệu thành các nhóm. Có thể là một số nguyên (số lượng khoảng), hoặc một list chứa các giá trị cắt nhau tạo thành các khoảng giá trị.
# - `labels`: (Tùy chọn) Nhãn cho các khoảng giá trị. Nếu không được chỉ định, các nhãn mặc định là số thứ tự của các khoảng.
# - `right`: (Mặc định là True) Xác định liệu khoảng cuối cùng là bao gồm giá trị cuối cùng (True) hay không bao gồm (False).
# - `include_lowest`: (Mặc định là False) Nếu là True, thì khoảng đầu tiên sẽ bao gồm giá trị thấp nhất, nếu là False thì không bao gồm.

# Phương thức `pd.cut()` trả về một Categorical object (đối tượng phân loại) chứa các nhãn cho từng phần tử dữ liệu tương ứng với nhóm tương ứng của nó. Điều này cho phép bạn thực hiện các phân tích dựa trên các nhóm dữ liệu đã phân loại.

# Dưới đây là một ví dụ về cách sử dụng `pd.cut()`:

# ```python
# import pandas as pd

# # Dữ liệu đầu vào
# ages = [25, 30, 35, 22, 40, 28, 32, 19, 37]

# # Chia dữ liệu thành các nhóm tuổi (khoảng giá trị)
# bins = [18, 25, 30, 35, 40]

# # Phân loại dữ liệu sử dụng pd.cut()
# age_groups = pd.cut(ages, bins)

# # In kết quả
# print(age_groups)
# ```

# Kết quả:

# ```
# [(18, 25], (25, 30], (30, 35], (18, 25], (35, 40], (25, 30], (30, 35], (18, 25], (35, 40]]
# Categories (4, interval[int64]): [(18, 25] < (25, 30] < (30, 35] < (35, 40]]
# ```

# Trong ví dụ trên, dữ liệu đã được phân loại thành 4 nhóm tuổi sử dụng `pd.cut()`, mỗi phần tử trong `age_groups` đại diện cho nhóm tương ứng của tuổi.