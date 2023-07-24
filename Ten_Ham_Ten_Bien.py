# Trong Python, có một số quy tắc và hướng dẫn về cách đặt tên biến, tên hàm và các đối tượng khác nhau để làm mã của bạn dễ đọc và dễ hiểu. 
# Dưới đây là một số quy tắc thông thường:

# 1. Tên biến và tên hàm:
#    - Sử dụng chữ cái viết thường: Tên biến và tên hàm nên bắt đầu bằng chữ cái viết thường.
#    - Sử dụng chữ cái và số: Tên biến và tên hàm có thể chứa chữ cái và số, nhưng không được bắt đầu bằng số.
#    - Dùng dấu gạch dưới: Bạn có thể sử dụng dấu gạch dưới để tách các từ trong tên biến hoặc tên hàm, ví dụ: `ten_bien`, `ham_tinh_tong`.
#    - Tránh sử dụng từ khóa: Không đặt tên biến hoặc tên hàm trùng với từ khóa của Python (ví dụ: `if`, `else`, `for`, `while`,...).

# 2. Tên hàm:
#    - Mô tả ngắn gọn chức năng: Tên hàm nên mô tả ngắn gọn chức năng của nó.
#    - Sử dụng động từ: Thông thường, tên hàm được đặt bằng các động từ để chỉ ra hành động mà hàm thực hiện, ví dụ: `calculate_sum()`, `print_message()`.
   
# 3. Tên hằng số:
#    - Sử dụng chữ in hoa: Tên hằng số nên được viết bằng chữ in hoa.
#    - Sử dụng dấu gạch dưới: Bạn có thể sử dụng dấu gạch dưới để tách các từ trong tên hằng số, ví dụ: `MAX_VALUE`, `PI`.

# 4. Tên lớp:
#    - Sử dụng kiểu Pascale: Tên lớp nên sử dụng kiểu Pascal (chữ cái đầu tiên của mỗi từ được viết hoa), ví dụ: `MyClass`, `CustomerRecord`.

# 5. Biến toàn cục và cục bộ:
#    - Tránh sử dụng biến toàn cục nếu không cần thiết. Sử dụng hàm hoặc lớp để đóng gói và truyền dữ liệu thay vì sử dụng biến toàn cục.
#    - Biến cục bộ trong hàm chỉ tồn tại trong phạm vi của hàm và sẽ bị hủy khi hàm thực thi xong.

# Dưới đây là một ví dụ về các quy tắc trên:

# ```python
# # Tên biến
# age = 25
# name = "John"
# counter_variable = 0

# # Tên hàm
# def calculate_sum(a, b):
#     return a + b

# def print_message(message):
#     print(message)

# # Tên hằng số
# PI = 3.14159
# MAX_ATTEMPTS = 5

# # Tên lớp
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# ```

# Ngoài các quy tắc trên, quan trọng nhất là giữ cho tên biến và tên hàm có ý nghĩa và dễ hiểu để giúp bạn và người khác đọc và hiểu mã dễ dàng hơn.

#====================================================================================================================================================

# Có hai quy tắc phổ biến về đặt tên biến trong Python là Snake case và Camel case. Dưới đây là mô tả và ví dụ cụ thể về từng quy tắc:

# 1. Snake case:
#    - Snake case là quy tắc đặt tên biến bằng cách sử dụng các từ liền nhau, phân tách bằng dấu gạch dưới `_`.
#    - Tất cả các chữ cái được viết thường.
#    - Đây là quy tắc được sử dụng phổ biến trong Python.

# Ví dụ về snake case:

# ```python
# # Đặt tên biến sử dụng snake case
# first_name = "John"
# last_name = "Doe"
# age = 30
# is_student = True
# ```

# 2. Camel case:
#    - Camel case là quy tắc đặt tên biến bằng cách sử dụng các từ liền nhau, trong đó từ đầu tiên được viết thường và các từ sau được viết hoa chữ cái đầu tiên của mỗi từ.
#    - Đây là một quy tắc thường được sử dụng trong các ngôn ngữ lập trình khác nhau.

# Ví dụ về camel case:

# ```python
# # Đặt tên biến sử dụng camel case
# firstName = "John"
# lastName = "Doe"
# ageOfPerson = 30
# isStudent = True
# ```

# Lưu ý rằng quy tắc đặt tên biến không ảnh hưởng đến hoạt động của mã Python, tuy nhiên, nó giúp mã trở nên dễ đọc và dễ hiểu hơn. 
# Trong Python, quy ước thông thường là sử dụng Snake case cho tên biến và Camel case cho tên lớp (class).


#====================================================================================================================================================

# "The Zen of Python" là một tập hợp các nguyên tắc và triết lý lập trình được ghi lại trong Python Enhancement Proposal (PEP) 20. 
# Được viết bởi Tim Peters, "The Zen of Python" tập trung vào việc hướng dẫn cách viết mã Python dễ đọc, dễ hiểu và thú vị hơn. 
# Nó cũng thể hiện tinh thần cộng đồng Python về cách tiếp cận viết mã.

# Bạn có thể xem "The Zen of Python" bằng cách nhập lệnh sau trong Python:

# ```python
# import this
# ```

# Sau khi chạy lệnh trên, bạn sẽ nhận được một tập hợp các câu châm ngôn của "The Zen of Python". Dưới đây là các câu châm ngôn đó:

# ```
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# ```

# The Zen of Python, của Tim Peters

# Đẹp hơn là xấu.
# Rõ ràng hơn là mập mờ.
# Đơn giản hơn là phức tạp.
# Phức tạp hơn là rắc rối.
# Bằng phẳng hơn là lồi lõm.
# Thưa thớt hơn là đậm đặc.
# Khả đọc hơn.
# Không có trường hợp đặc biệt đủ đặc biệt để phá vỡ quy tắc.
# Mặc dù tính thực dụng vượt trội.
# Lỗi không nên bao giờ bị lờ đi.
# Trừ khi được rõ ràng lựa chọn.
# Trong trường hợp mơ hồ, từ chối cám dỗ đoán định.
# Phải có một -- và tốt nhất là chỉ một -- cách rõ ràng để thực hiện điều đó.
# Mặc dù cách đó có thể không rõ ràng từ đầu, trừ khi bạn là người Hà Lan.
# Bây giờ hơn không bao giờ.
# Mặc dù thường thì không bằng *ngay lúc này*.
# Nếu việc thực hiện khó giải thích, đó là ý tưởng tồi.
# Nếu việc thực hiện dễ giải thích, đó có thể là ý tưởng tốt.
# Không gian tên là một ý tưởng vĩ đại -- hãy làm nhiều hơn những cái đó!


# Mỗi câu châm ngôn thể hiện một nguyên tắc quan trọng về viết mã Python, chẳng hạn như ưu tiên sự đơn giản, dễ đọc và rõ ràng, tránh những tình huống đặc biệt và lỗi không nên được lờ đi. 
# Các câu châm ngôn này thường được sử dụng như hướng dẫn khi phát triển mã Python để tạo ra mã chất lượng và dễ bảo trì.

#====================================================================================================================================================

# "Scalar types" trong Python là các kiểu dữ liệu đơn giản và không có khả năng lưu trữ nhiều giá trị hoặc các thành phần phức tạp. Các kiểu dữ liệu scalar chỉ có thể chứa một giá trị duy nhất mỗi lần và được coi là không thể thay đổi (immutable). Các scalar types trong Python bao gồm:

# 1. **int (số nguyên)**: Kiểu dữ liệu int đại diện cho các số nguyên, ví dụ:

# ```python
# age = 25
# ```

# 2. **float (số thực)**: Kiểu dữ liệu float đại diện cho các số thực, ví dụ:

# ```python
# pi = 3.14159
# ```

# 3. **bool (giá trị logic)**: Kiểu dữ liệu bool đại diện cho các giá trị logic True hoặc False, ví dụ:

# ```python
# is_student = True
# ```

# 4. **str (chuỗi)**: Kiểu dữ liệu str đại diện cho các chuỗi ký tự, ví dụ:

# ```python
# name = "John Doe"
# ```

# 5. **NoneType (kiểu dữ liệu None)**: Kiểu dữ liệu NoneType chỉ có giá trị duy nhất là None, thể hiện sự thiếu vắng dữ liệu, ví dụ:

# ```python
# result = None
# ```

# Các scalar types là các kiểu dữ liệu đơn giản và thường được sử dụng trong các phép tính, điều kiện và xử lý dữ liệu cơ bản trong Python.