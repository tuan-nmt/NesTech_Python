# Python là một ngôn ngữ lập trình mạnh mẽ, dễ học. Nó có cấu trúc dữ liệu cấp cao hiệu quả và
# một cách tiếp cận đơn giản nhưng hiệu quả đối với lập trình hướng đối tượng. Cú pháp tao nhã và năng động của Python
# đánh máy, cùng với bản chất diễn giải của nó, làm cho nó trở thành một ngôn ngữ lý tưởng để viết kịch bản và ứng dụng nhanh chóng
# phát triển trong nhiều lĩnh vực trên hầu hết các nền tảng.
# Trình thông dịch Python và thư viện chuẩn mở rộng có sẵn miễn phí ở dạng nguồn hoặc nhị phân cho tất cả
# nền tảng chính từ trang web Python, https://www.python.org/, và có thể được phân phối miễn phí. Các
# cùng một trang web cũng chứa các bản phân phối và con trỏ tới nhiều chương trình, mô-đun Python miễn phí của bên thứ ba
# và các công cụ, và tài liệu bổ sung.
# Trình thông dịch Python dễ dàng mở rộng với các hàm và kiểu dữ liệu mới được triển khai trong C hoặc C++
# (hoặc các ngôn ngữ khác có thể gọi được từ C). Python cũng phù hợp làm ngôn ngữ mở rộng để tùy chỉnh
# các ứng dụng.
# Hướng dẫn này giới thiệu cho người đọc một cách không chính thức về các khái niệm và tính năng cơ bản của ngôn ngữ Python
# và hệ thống. Sẽ rất hữu ích khi có một trình thông dịch Python tiện dụng cho trải nghiệm thực hành, nhưng tất cả các ví dụ đều
# khép kín, vì vậy hướng dẫn cũng có thể được đọc ngoại tuyến.
# Để biết mô tả về các đối tượng và mô-đun tiêu chuẩn, hãy xem thư viện-index. chỉ mục tham chiếu cung cấp một cách chính thức hơn
# định nghĩa của ngôn ngữ. Để viết các phần mở rộng bằng C hoặc C++, hãy đọc chỉ mục mở rộng và chỉ mục c-api. Ở đó
# cũng có một số cuốn sách chuyên sâu về Python.
# Hướng dẫn này không cố gắng toàn diện và bao gồm mọi tính năng đơn lẻ hoặc thậm chí mọi tính năng phổ biến.
# tính năng đã sử dụng. Thay vào đó, nó giới thiệu nhiều tính năng đáng chú ý nhất của Python và sẽ cung cấp cho bạn
# ý tưởng về hương vị và phong cách của ngôn ngữ. Sau khi đọc nó, bạn sẽ có thể đọc và viết các mô-đun Python
# và các chương trình, đồng thời bạn sẽ sẵn sàng tìm hiểu thêm về các mô-đun thư viện Python khác nhau được mô tả trong
# thư viện-index.
# Bảng thuật ngữ cũng đáng để xem qua.


# KÍCH THÍCH KHỨC CẢM CỦA BẠN
# Nếu bạn làm việc nhiều trên máy tính, cuối cùng bạn sẽ nhận ra rằng có một số công việc bạn muốn tự động hóa. 
# Ví dụ, bạn có thể muốn thực hiện tìm và thay thế trên một số lượng lớn các tệp văn bản, hoặc đổi tên và sắp xếp lại một loạt các tệp ảnh theo cách phức tạp. 
# Có lẽ bạn muốn viết một cơ sở dữ liệu tùy chỉnh nhỏ, hoặc một ứng dụng GUI chuyên dụng, hoặc một trò chơi đơn giản.

# Nếu bạn là một nhà phát triển phần mềm chuyên nghiệp, 
# bạn có thể phải làm việc với một số thư viện C/C++/Java nhưng thấy chu trình viết/ biên dịch/ kiểm thử/ biên dịch thông thường quá chậm. 
# Có thể bạn đang viết một bộ kiểm thử cho một thư viện như vậy và thấy viết mã kiểm thử là một công việc tẻ nhạt. 
# Hoặc có thể bạn đã viết một chương trình có thể sử dụng một ngôn ngữ mở rộng và bạn không muốn thiết kế và triển khai một ngôn ngữ hoàn toàn mới cho ứng dụng của bạn.

# Python chính là ngôn ngữ dành cho bạn.

# Bạn có thể viết một script shell Unix hoặc tệp batch Windows cho một số công việc này, 
# nhưng script shell chỉ tốt trong việc di chuyển các tệp và thay đổi dữ liệu văn bản, không phù hợp cho ứng dụng GUI hoặc trò chơi. 
# Bạn cũng có thể viết một chương trình C/C++/Java, nhưng việc phát triển một chương trình sơ bộ thậm chí cũng có thể mất rất nhiều thời gian.

# Python dễ sử dụng hơn, có thể sử dụng trên các hệ điều hành Windows, Mac OS X và Unix, và giúp bạn hoàn thành công việc nhanh hơn.

# Python dễ sử dụng, nhưng đó là một ngôn ngữ lập trình thực sự, cung cấp nhiều cấu trúc và hỗ trợ cho các chương trình lớn hơn hơn là script shell hoặc tệp batch có thể cung cấp. 
# Từ phía khác, Python cũng cung cấp nhiều kiểm tra lỗi hơn C và, với việc là một ngôn ngữ cấp cao, nó tích hợp sẵn các loại dữ liệu cấp cao, như mảng linh hoạt và từ điển. 
# Vì có các loại dữ liệu tổng quát hơn, Python có thể áp dụng cho một lĩnh vực vấn đề lớn hơn nhiều so với Awk hoặc thậm chí Perl, nhưng nhiều điều trong Python ít nhất cũng dễ dàng như trong các ngôn ngữ đó.

# Python cho phép bạn chia chương trình của mình thành các module có thể được sử dụng lại trong các chương trình Python khác. 
# Nó đi kèm với một bộ sưu tập các module chuẩn lớn mà bạn có thể sử dụng làm cơ sở cho các chương trình của bạn - hoặc như các ví dụ để bắt đầu học lập trình Python. 
# Một số module này cung cấp các chức năng như đọc/ghi tệp, gọi hệ thống, socket, và thậm chí các giao diện đồ họa với các bộ công cụ giao diện người dùng đồ họa như Tk.

# Python là một ngôn ngữ thông dịch, điều này có thể tiết kiệm thời gian đáng kể trong quá trình phát triển chương trình vì không cần biên dịch và liên kết. 
# Trình thông dịch có thể sử dụng tương tác, giúp dễ dàng thử nghiệm các tính năng của ngôn ngữ, viết các chương trình tạm thời, hoặc kiểm tra các chức năng trong quá trình phát triển chương trình từ phía dưới lên. Nó cũng là một máy tính để bàn tiện dụng.

# Python cho phép viết các chương trình gọn gàng và dễ đọc. Các chương trình viết bằng Python thường ngắn gọn hơn rất nhiều so với các chương trình tương đương bằng C, C++ hoặc Java, vì một số lý do sau:
# • Các loại dữ liệu cấp cao cho phép bạn thể hiện các phép toán phức tạp trong một câu lệnh duy nhất;
# • Nhóm câu lệnh được thực hiện bằng thụt lề thay vì các dấu ngoặc mở và đóng;
# • Không cần khai báo biến hoặc đối số.

# Python có tính mở rộng: nếu bạn biết cách lập trình bằng C, thì việc thêm một hàm hoặc module mới vào trình thông dịch là d

# ễ dàng, cho phép thực hiện các hoạt động quan trọng với tốc độ tối đa hoặc liên kết chương trình Python với các thư viện có sẵn dưới dạng nhị phân (như một thư viện đồ họa cụ thể của nhà cung cấp).