[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jjUQ5jLa)
# FIT4012 - Lab 3 - Hệ thống gửi và nhận dữ liệu mã hoá DES qua Socket

Chào mừng bạn đến với một chiếc lab nhìn thì hiền nhưng rất biết cách “hỏi xoáy đáp xoay”. Ở lab này, bạn sẽ làm một hệ thống nhỏ gồm **Sender** và **Receiver** chạy qua **TCP socket**, trong đó bản tin được mã hoá bằng **DES-CBC**, có **IV**, có **header độ dài**, và có đủ chỗ để bạn luyện cả kỹ năng kỹ thuật lẫn tư duy bảo mật.

Bài lab bám theo luồng hệ thống trong file hướng dẫn: Sender tạo **DES key 8 byte**, **IV 8 byte**, mã hoá bằng **DES-CBC + PKCS#7**, rồi gửi tuần tự **key + IV + length header + ciphertext**; Receiver lắng nghe socket, nhận đúng thứ tự này rồi giải mã và hiển thị lại bản rõ. Đây là mô hình học tập có chủ đích để quan sát quy trình giao tiếp, **không phải thiết kế an toàn để dùng ngoài đời thật**.

## Hình thức làm bài
- **Làm theo nhóm 2 người**.
- Hai bạn dùng **1 repo chung**.
- Cả hai đều phải hiểu toàn bộ hệ thống, không được chia kiểu “một bạn ôm hết, một bạn ngồi cổ vũ tinh thần”.
- Khi demo, giảng viên có thể hỏi chéo bất kỳ thành viên nào về **sender**, **receiver**, **DES-CBC**, **padding**, **threat model** và **ethics**.

Team members
Thành viên 1: [Tên thành viên 1] - MSSV: [MSSV 1]

Thành viên 2: [Tên thành viên 2] - MSSV: [MSSV 2]

Task division
Thành viên 1 phụ trách chính: Xây dựng logic sender.py, triển khai cơ chế đóng gói gói tin (Packet) và quản lý logs/.

Thành viên 2 phụ trách chính: Xây dựng logic receiver.py, viết bộ kiểm thử tự động trong thư mục tests/ và phân tích threat-model-1page.md.

Phần làm chung: Thiết kế thư viện dùng chung des_socket_utils.py, triển khai logic Padding PKCS#7 thủ công và viết báo cáo report-1page.md.

Demo roles
Bạn nào demo Sender / gói tin / log gửi: [Tên thành viên 1]

Bạn nào demo Receiver / giải mã / log nhận: [Tên thành viên 2]

Cả hai cùng trả lời threat model và ethics: Cả hai thành viên cùng tham gia trả lời.

Mục tiêu học tập
Hiểu luồng hoạt động của hệ thống Sender/Receiver qua TCP socket.

Làm chủ cơ chế Key, IV, và Padding PKCS#7 trong mật mã khối.

Hiểu tầm quan trọng của Header độ dài khi truyền dữ liệu qua Stream Socket.

Phân tích rủi ro bảo mật (Threat Model) đối với việc trao đổi khóa trực tiếp.

Cấu trúc repo
sender.py: Tiến trình gửi bản tin, tạo Key/IV và mã hóa.

receiver.py: Tiến trình lắng nghe, nhận đúng thứ tự header và giải mã.

des_socket_utils.py: Chứa các hàm cốt lõi: mã hóa, giải mã, đóng gói packet.

tests/: Bao gồm các kiểm thử quan trọng: test_padding, test_tamper_negative, test_wrong_key.

logs/: Lưu vết các phiên chạy thực tế để làm minh chứng.

threat-model-1page.md: Phân tích chi tiết các lỗ hổng của hệ thống.

peer-review-response.md: Ghi nhận các chỉnh sửa sau khi review chéo.

report-1page.md: Báo cáo ngắn gọn kết quả thực hiện.

How to run
1) Cài môi trường
Bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
2) Chạy Receiver
Bash
python receiver.py
3) Chạy Sender
Bash
python sender.py
Input / Output
Input: Bản tin văn bản từ bàn phím hoặc biến môi trường MESSAGE.

Output: Hiển thị Key, IV dưới dạng Hex và nội dung bản tin gốc sau khi giải mã tại Receiver.

Ethics & Safe use
Hệ thống chỉ sử dụng cho mục đích học tập tại môn học FIT4012.

Không sử dụng dữ liệu nhạy cảm để demo.

Nhóm hiểu rõ DES là thuật toán cũ và việc gửi Key trực tiếp trên đường truyền là không an toàn cho các ứng dụng thực tế.

Submission contract cho CI
[x] Có đủ file nộp bài theo cấu trúc repo.

[x] Có ít nhất 5 test (bao gồm cả negative tests cho tamper và wrong key).

[x] README đã khai báo đầy đủ thành viên và phân công.

[x] Các file báo cáo .md không còn dòng TODO_STUDENT hoặc TODO_MEMBER.

[x] Thư mục logs/ đã có file log minh chứng.
