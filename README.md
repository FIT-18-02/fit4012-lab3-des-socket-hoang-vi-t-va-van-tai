# FIT4012 - Lab 3 - Hệ thống gửi và nhận dữ liệu mã hoá DES qua Socket

Hệ thống mô phỏng truyền nhận dữ liệu mã hóa qua Socket TCP, kết hợp thuật toán DES-CBC và cơ chế đóng gói gói tin chuyên dụng.

## Team members
- **Thành viên 1**: Bùi Văn Tài - **MSSV**: 1871020515
- **Thành viên 2**: Nguyễn Hoàng Việt - **MSSV**: 1871020654

## Task division
- **Thành viên 1 phụ trách chính**: Phát triển `sender.py`, xây dựng logic đóng gói gói tin (Key + IV + Length + Ciphertext) và quản lý thư mục `logs/`.
- **Thành viên 2 phụ trách chính**: Phát triển `receiver.py`, xây dựng bộ kiểm thử tự động trong `tests/` và phân tích rủi ro trong `threat-model-1page.md`.
- **Phần làm chung**: Thiết kế thư viện `des_socket_utils.py`, cài đặt thủ công logic Padding PKCS#7 và viết báo cáo hệ thống.

## Demo roles
- **Bạn nào demo Sender / gói tin / log gửi**: Bùi Văn Tài
- **Bạn nào demo Receiver / giải mã / log nhận**: Nguyễn Hoàng Việt
- **Cả hai cùng trả lời threat model và ethics**: Cả hai thành viên cùng tham gia trả lời vấn đáp.

## Input / Output
- **Input**:
    - Sender: Nhận bản tin văn bản (string) từ bàn phím hoặc qua biến môi trường `MESSAGE`.
    - Receiver: Nhận luồng dữ liệu nhị phân (bytes) từ TCP Socket.
- **Output**:
    - Sender: Hiển thị trạng thái gửi, giá trị Key, IV và Ciphertext dưới dạng Hex.
    - Receiver: Hiển thị bản tin gốc sau khi giải mã và gỡ padding thành công.
    - Logs: Ghi lại toàn bộ lịch sử giao tiếp vào thư mục `logs/`.

## Threat-model awareness
Vì bài lab này sử dụng mô hình gửi trực tiếp **Key và IV dưới dạng plaintext** trên cùng luồng TCP, nhóm nhận diện được đây là một lỗ hổng bảo mật nghiêm trọng. Trong file `threat-model-1page.md`, chúng tôi đã phân tích kỹ các khía cạnh:
- **Assets**: Nội dung tin nhắn gốc và tính toàn vẹn của dữ liệu trên đường truyền.
- **Attacker model**: Kẻ tấn công Man-in-the-Middle (MitM) có khả năng nghe lén.
- **Threats**: Kẻ tấn công có thể lấy được Key/IV để giải mã bản tin hoặc sửa đổi nội dung.
- **Mitigations**: Đề xuất sử dụng RSA/Diffie-Hellman để trao đổi khóa an toàn.

## Ethics & Safe use
- Chỉ triển khai và chạy thử nghiệm trên máy cá nhân hoặc mạng nội bộ được cho phép phục vụ học tập.
- Tuyệt đối không quét cổng (port scanning) hoặc thử nghiệm lên các hệ thống bên ngoài phạm vi lớp học.
- Không sử dụng dữ liệu cá nhân thật hoặc dữ liệu nhạy cảm để demo hệ thống.
- Không trình bày hệ thống này như một giải pháp bảo mật hoàn thiện để sử dụng ngoài thực tế.
- Tôn trọng nguyên tắc trung thực học thuật và ghi nhận nguồn tham khảo đầy đủ.

## How to run
### 1) Cài môi trường
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
