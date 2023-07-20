# mRow = int(input("Nhap so hang: "))

# if mRow < 2:
#     print("Sai roi")

# mResult = [[1,1], [1,2,1]]

# for mIndex in range(2, mRow):
#     mRowData = [1,1]
#     for mRowIndex in range(1, mIndex):
#         mValue = mResult[mIndex-1][mRowIndex-1] + mResult[mIndex-1][mRowIndex]
#         print(f"mRowIndex {mIndex}", mValue)
#         mRowData.insert(mRowIndex, mValue)
#     print(f"mIndex {mIndex}", mRowData)
#     mResult.append(mRowData)

# print(mResult)


# # Hàm lambda để tính số giây từ giờ, phút và giây
# calculate_seconds = lambda hours, minutes, seconds: hours * 3600 + minutes * 60 + seconds

# # Nhập giờ, phút và giây từ bàn phím
# try:
#     hours = int(input("Nhập số giờ: "))
#     minutes = int(input("Nhập số phút: "))
#     seconds = int(input("Nhập số giây: "))
# except ValueError:
#     print("Định dạng không hợp lệ. Vui lòng nhập số nguyên dương.")
# else:
#     if hours < 0 or minutes < 0 or seconds < 0:
#         print("Các giá trị không được nhỏ hơn 0.")
#     else:
#         total_seconds = calculate_seconds(hours, minutes, seconds)
#         print("Tổng số giây: ", total_seconds)

# def hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Di chuyển đĩa 1 từ {source} sang {target}")
#         return
#     hanoi(n-1, source, auxiliary, target)
#     print(f"Di chuyển đĩa {n} từ {source} sang {target}")
#     hanoi(n-1, auxiliary, target, source)

# if __name__ == "__main__":
#     try:
#         num_disks = int(input("Nhập số đĩa: "))
#     except ValueError:
#         print("Vui lòng nhập một số nguyên.")
#     else:
#         if num_disks <= 0:
#             print("Số đĩa phải lớn hơn 0.")
#         else:
#             hanoi(num_disks, 'A', 'C', 'B')


# Gợi ý:

# ```python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# class Student(Person):
#     def __init__(self, name, age, student_id, average_score):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.average_score = average_score

#     def display_info(self):
#         super().display_info()
#         print(f"Student ID: {self.student_id}")
#         print(f"Average Score: {self.average_score}")


# if __name__ == "__main__":
#     student = Student("John Doe", 16, "2023001", 85)
#     student.display_info()
# ```

# Lưu ý rằng trong lớp con `Student`, chúng ta đã sử dụng hàm `super()` để gọi phương thức `__init__()` của lớp cha `Person` để khởi tạo các thuộc tính `name` và `age`.
