Peer Review Response - Lab 3
Thông tin nhóm
Thành viên 1: [BUi VAN TAI] - [1871020515]

Thành viên 2: [TÊN_SINH_VIÊN_2] - [MSSV_2]

Thành viên 1 góp ý cho thành viên 2
Phần logic xử lý tại Receiver rất ổn định, tuy nhiên ban đầu bộ test trong tests/ còn thiếu trường hợp bản tin có độ dài đúng bằng bội số của 8 (block size của DES). Ngoài ra, các thông báo lỗi khi giải mã sai (unpad error) cần được bắt exception cụ thể hơn để chương trình không bị crash đột ngột khi nhận dữ liệu rác.

Thành viên 2 góp ý cho thành viên 1
Code của Sender viết rất sạch và dễ hiểu. Tuy nhiên, việc tạo Key và IV nên được tách hẳn thành các hàm riêng biệt trong des_socket_utils.py thay vì để trực tiếp trong sender.py. Điều này giúp code tái sử dụng tốt hơn và dễ dàng viết unit test cho khâu tạo khóa ngẫu nhiên. Phần log cũng nên bổ sung thêm timestamp để dễ theo dõi quá trình gửi nhận.

Nhóm đã sửa gì sau góp ý
Sau khi tiến hành review chéo, nhóm đã thực hiện các thay đổi cụ thể sau:

Tái cấu trúc code: Di chuyển toàn bộ hàm tạo Key/IV và mã hóa/giải mã vào des_socket_utils.py để chuẩn hóa thư viện dùng chung.

Cải thiện bộ test: Bổ sung thêm case test_exact_block_size và test_unpad_error để kiểm tra tính bền bỉ của hệ thống khi gặp dữ liệu không hợp lệ.

Xử lý ngoại lệ: Thêm khối try-except quanh phần giải mã và unpad ở Receiver để in ra thông báo lỗi bảo mật thay vì dừng chương trình.

Cập nhật Logging: Thêm thời gian thực (timestamp) và định dạng Hexadecimal cho Key/IV trong logs để phục vụ việc đối soát dữ liệu dễ dàng hơn.
