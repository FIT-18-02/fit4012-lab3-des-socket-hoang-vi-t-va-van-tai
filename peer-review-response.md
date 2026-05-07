# Peer Review Response - Lab 3

## Thông tin nhóm
* **Thành viên 1:** Bùi Văn Tài - **MSSV:** 1871020515
* **Thành viên 2:** Nguyễn Hoàng Việt - **MSSV:** 1871020654

## Thành viên 1 góp ý cho thành viên 2
Phần xử lý `receiver.py` đã hoạt động tốt, tuy nhiên cần chú ý bắt lỗi `ValueError` khi giải mã sai (trong trường hợp test case sai khóa) để chương trình không bị dừng đột ngột. Bộ test case cần bao quát thêm trường hợp dữ liệu rỗng.

## Thành viên 2 góp ý cho thành viên 1
Phần `sender.py` nên tách biệt rõ ràng hơn giữa khâu nhập liệu và khâu mã hóa. Nên bổ sung thêm thời gian (timestamp) vào file nhật ký trong thư mục `logs/` để dễ dàng đối soát quá trình gửi nhận theo thời gian thực.

## Nhóm đã sửa gì sau góp ý
Sau khi tiến hành review chéo, nhóm đã thực hiện các thay đổi cụ thể sau:
* **Tối ưu hóa thư viện:** Chuyển toàn bộ logic xử lý Padding và mã hóa vào `des_socket_utils.py` để dùng chung cho cả hai phía.
* **Xử lý ngoại lệ:** Thêm khối `try-except` tại Receiver để thông báo lỗi bảo mật một cách chuyên nghiệp thay vì để hệ thống tự crash.
* **Cải thiện Logging:** Định dạng lại các file log trong thư mục `logs/` để hiển thị Key và IV dưới dạng Hexadecimal dễ quan sát.
* **Bổ sung Test case:** Thêm các ca kiểm thử âm tính (Negative tests) để đảm bảo hệ thống nhận diện được dữ liệu bị can thiệp.
