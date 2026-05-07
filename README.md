# FIT4012 - Lab 3 - Hệ thống gửi và nhận dữ liệu mã hoá DES qua Socket

Hệ thống mô phỏng truyền nhận dữ liệu mã hóa qua Socket TCP, kết hợp thuật toán DES-CBC và cơ chế đóng gói gói tin chuyên dụng.

## Team members
- **Thành viên 1**: [bùi văn tài ] - **MSSV**: [1871020515]
- **Thành viên 2**: [nguyễn hoàng việt] - **MSSV**: [1871020654 ]



## Task division
- **Thành viên 1 phụ trách chính**: Phát triển `sender.py`, xây dựng logic đóng gói gói tin (Key + IV + Length + Ciphertext) và quản lý `logs/`.
- **Thành viên 2 phụ trách chính**: Phát triển `receiver.py`, xây dựng bộ kiểm thử tự động `tests/` và phân tích rủi ro trong `threat-model-1page.md`.
- **Phần làm chung**: Thiết kế thư viện `des_socket_utils.py`, cài đặt thủ công logic Padding PKCS#7 và viết báo cáo hệ thống.

## Demo roles
- **Bạn nào demo Sender / gói tin / log gửi**: [bùi văn tài]
- **Bạn nào demo Receiver / giải mã / log nhận**: [nguyễn hoàng việt  2]
- **Cả hai cùng trả lời threat model và ethics**: Cả hai thành viên tham gia trả lời vấn đáp.

## Input / Output
- **Input**:
    - Sender: Nhận bản tin văn bản (string) từ bàn phím hoặc qua biến môi trường `MESSAGE`.
    - Receiver: Nhận luồng dữ liệu nhị phân (bytes) từ TCP Socket.
- **Output**:
    - Sender: Hiển thị trạng thái gửi, giá trị Key, IV và Ciphertext đã mã hóa.
    - Receiver: Hiển thị bản tin gốc sau khi giải mã thành công.
    - Logs: Ghi lại toàn bộ quá trình giao tiếp vào thư mục `logs/`.

## Threat-model awareness
Vì bài lab này sử dụng mô hình gửi trực tiếp **Key và IV dưới dạng plaintext** trên cùng luồng TCP, nhóm nhận diện được đây là một lỗ hổng bảo mật nghiêm trọng. Trong file `threat-model-1page.md`, chúng tôi đã phân tích kỹ các khía cạnh:
- **Assets**: Nội dung tin nhắn gốc và tính toàn vẹn của dữ liệu trên đường truyền.
- **Attacker model**: Kẻ tấn công Man-in-the-Middle (MitM).
- **Threats**: Kẻ tấn công có thể lấy được Key/IV để giải mã bản tin hoặc sửa đổi Ciphertext.
- **Mitigations**: Đề xuất sử dụng RSA/Diffie-Hellman và HMAC.
- **Residual risks**: Rủi ro từ máy trạm bị nhiễm mã độc.

## How to run
### 1) Cài môi trường
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
