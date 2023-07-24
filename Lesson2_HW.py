# Dưới đây là ba bài tập về xử lý dữ liệu (Data Processing) sử dụng thư viện Pandas và lời giải đi kèm. Bạn có thể sử dụng môi trường Python và cài đặt thư viện Pandas để thực hiện các bài tập này.

# Bài tập 1:
# Hãy tạo DataFrame từ dict dưới đây và thực hiện các yêu cầu sau:

# ```python
# import pandas as pd

# # Tạo DataFrame từ dict
# data = {
#     'Tên': ['John', 'Alice', 'Bob', 'Emily', 'David'],
#     'Tuổi': [28, 24, 22, 25, 30],
#     'Giới tính': ['Nam', 'Nữ', 'Nam', 'Nữ', 'Nam'],
#     'Điểm số': [85, 78, 92, 88, 90]
# }

# df = pd.DataFrame(data)

# # Yêu cầu 1: In ra 5 dòng đầu tiên của DataFrame
# print("5 dòng đầu tiên của DataFrame:")
# print(df.head())

# # Yêu cầu 2: Thêm cột 'Quốc tịch' với giá trị mặc định là 'Việt Nam'
# df['Quốc tịch'] = 'Việt Nam'
# print("\nDataFrame sau khi thêm cột 'Quốc tịch':")
# print(df)

# # Yêu cầu 3: Tính trung bình điểm số của các học sinh
# mean_diem_so = df['Điểm số'].mean()
# print("\nTrung bình điểm số của các học sinh:", mean_diem_so)
# ```

# Bài tập 2:
# Hãy đọc dữ liệu từ tập tin CSV có định dạng như sau và thực hiện các yêu cầu:

# ```csv
# STT,Tên,Môn học,Điểm
# 1,John,Toán,8.5
# 2,Alice,Lý,7.8
# 3,Bob,Hóa,6.9
# 4,Emily,Toán,9.0
# 5,David,Lý,8.2
# ```

# ```python
# import pandas as pd

# # Yêu cầu 1: Đọc dữ liệu từ tập tin CSV
# df = pd.read_csv('du_lieu.csv')

# # Yêu cầu 2: In thông tin các cột của DataFrame
# print("Thông tin các cột của DataFrame:")
# print(df.info())

# # Yêu cầu 3: Tính điểm trung bình theo môn học
# diem_trung_binh_mon_hoc = df.groupby('Môn học')['Điểm'].mean()
# print("\nĐiểm trung bình theo môn học:")
# print(diem_trung_binh_mon_hoc)
# ```

# Bài tập 3:
# Hãy đọc dữ liệu từ tập tin Excel có định dạng như sau và thực hiện các yêu cầu:

# ```python
# # Tập tin Excel: du_lieu.xlsx
# # Sheet: Sheet1
# # Dữ liệu:
# #   STT  Tên  Điểm
# #    1  John  8.5
# #    2  Alice 7.8
# #    3  Bob   6.9
# #    4  Emily 9.0
# #    5  David 8.2
# ```

# ```python
# import pandas as pd

# # Yêu cầu 1: Đọc dữ liệu từ tập tin Excel
# df = pd.read_excel('du_lieu.xlsx', sheet_name='Sheet1')

# # Yêu cầu 2: Thêm cột 'Xếp loại' với điều kiện: Điểm >= 8.0 là 'Giỏi', ngược lại là 'Trung bình'
# df['Xếp loại'] = df['Điểm'].apply(lambda x: 'Giỏi' if x >= 8.0 else 'Trung bình')
# print(df)

# # Yêu cầu 3: Lưu DataFrame vào tập tin Excel mới có tên 'du_lieu_moi.xlsx' trên Sheet 'Kết quả'
# df.to_excel('du_lieu_moi.xlsx', sheet_name='Kết quả', index=False)
# print("\nLưu thành công.")
# ```

# Lưu ý: Đảm bảo có tập tin `du_lieu.csv` và `du_lieu.xlsx` chứa dữ liệu như yêu cầu trong cùng thư mục với script Python để chạy các bài tập này thành công.