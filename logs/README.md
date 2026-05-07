# FIT4012 - Lab 3 - Hệ thống gửi và nhận dữ liệu mã hoá DES qua Socket

## Team members
- **Thành viên 1**: Bùi Văn Tài - **MSSV**: 1871020515
- **Thành viên 2**: Nguyễn Hoàng Việt - **MSSV**: 1871020654

## Task division
- **Bùi Văn Tài**: Phát triển `sender.py`, xây dựng logic đóng gói packet và quản lý logs.
- **Nguyễn Hoàng Việt**: Phát triển `receiver.py`, viết bộ kiểm thử `tests/` và phân tích Threat Model.

## Input / Output
- **Input**: Bản tin văn bản từ bàn phím hoặc biến môi trường `MESSAGE`.
- **Output**: Hiển thị Key, IV, Ciphertext (Hex) và bản tin gốc sau khi giải mã.

## Threat-model awareness
Hệ thống hiện tại gửi trực tiếp Key và IV dưới dạng plaintext kèm theo gói tin. Đây là lỗ hổng nghiêm trọng cho phép kẻ tấn công nghe lén có thể giải mã toàn bộ dữ liệu.

## Ethics & Safe use
- Chỉ sử dụng cho mục đích học tập.
- Không dùng dữ liệu thật hoặc nhạy cảm để demo.
- Không trình bày hệ thống này như một giải pháp bảo mật hoàn thiện.

## How to run
1. Chạy Receiver: `python receiver.py`
2. Chạy Sender: `python sender.py`
