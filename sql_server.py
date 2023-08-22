import pyodbc

# Thay đổi các thông tin kết nối tương ứng với cơ sở dữ liệu của bạn
# server = 'ten_server'
# database = 'ten_database'
# username = 'ten_nguoidung'
# password = 'mat_khau'

server = 'L170068'
database = 'QLBH'
username = 'sa'
password = '123456'

# Chuỗi kết nối
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Kết nối tới cơ sở dữ liệu
connection = pyodbc.connect(connection_string)

# Tạo đối tượng cursor để thực hiện các truy vấn
cursor = connection.cursor()

# Ví dụ truy vấn: lấy tất cả dữ liệu từ một bảng
table_name = 'HOADON'
query = f'SELECT * FROM {table_name}'
cursor.execute(query)

# Lấy kết quả truy vấn
rows = cursor.fetchall()
for row in rows:
    print(row)

# # Truy vấn tạo bảng mới
# create_table_query = '''
# CREATE TABLE SV (
#     ID INT PRIMARY KEY,
#     Ten NVARCHAR(50),
#     Tuoi INT
# )
# '''
# cursor.execute(create_table_query)
# connection.commit()  # Cần commit để thực hiện tạo bảng

# # Thêm dữ liệu vào bảng
# insert_query = "INSERT INTO SV (ID, Ten, Tuoi) VALUES (?, ?, ?)"
# values_to_insert = (1, 'Tuan', 12)
# cursor.execute(insert_query, values_to_insert)
# connection.commit()  # Cần commit để lưu thay đổi vào cơ sở dữ liệu

# # Thêm dữ liệu vào bảng
# insert_query = "INSERT INTO SV (ID, Ten, Tuoi) VALUES (2, 'A', 12)"
# cursor.execute(insert_query)
# connection.commit()  # Cần commit để lưu thay đổi vào cơ sở dữ liệu

# Sửa dữ liệu trong bảng
# update_query = "UPDATE SV SET Ten = ? WHERE ID = ?"
# new_value = 'B'
# target_value = '1'
# cursor.execute(update_query, (new_value, target_value))
# connection.commit()

# # Sửa dữ liệu trong bảng
# update_query = "UPDATE SV SET Ten = 'C' WHERE ID = 2"
# # new_value = 'B'
# # target_value = '1'
# cursor.execute(update_query)
# connection.commit()

# Xóa dữ liệu khỏi bảng
# delete_query = "DELETE FROM SV WHERE ID = ?"
# value_to_delete = '1'
# cursor.execute(delete_query, (value_to_delete,))
# connection.commit()

# Đóng kết nối và cursor khi đã hoàn thành
cursor.close()
connection.close()
