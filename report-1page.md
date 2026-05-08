# Phân tích Threat Model - Lab 3

## 1. Asset Identification (Tài sản cần bảo vệ)
* **Nội dung bản rõ (Plaintext):** Thông tin nhạy cảm ngưi dùng gửi đi.ờ
* **Tính toàn vẹn dữ liệu:** Đảm bảo gói tin không bị chỉnh sửa trên đường truyền.
* **Tính riêng tư:** Đảm bảo chỉ người nhận (Receiver) hợp lệ mới có thể đọc tin nhắn.

## 2. Attacker Model (Mô hình kẻ tấn công)
* **Kẻ tấn công nghe lén (Sniffer):** Có khả năng bắt gói tin trên cùng mạng nội bộ hoặc qua các nút mạng trung gian.
* **Kẻ tấn công xen giữa (Man-in-the-Middle):** Có khả năng chặn gói tin, sửa đổi nội dung và gửi tiếp đến đích.

## 3. Threat Analysis (Phân tích mối đe dọa)

| Threat ID | Phân loại (STRIDE) | Mô tả chi tiết |
| :--- | :--- | :--- |
| **T1** | **Information Disclosure** | **Nghiêm trọng:** Vì Key và IV được gửi kèm ngay đầu gói tin dưới dạng plaintext, bất kỳ ai bắt được gói tin đều có thể giải mã nội dung dễ dàng. |
| **T2** | **Tampering** | Kẻ tấn công có thể thay đổi bit trong Ciphertext. Do hệ thống thiếu mã xác thực (MAC), Receiver sẽ giải mã ra dữ liệu rác mà không biết đã bị tấn công. |
| **T3** | **Information Disclosure** | Thuật toán DES với khóa 56-bit hiện nay đã quá yếu, dễ bị tấn công vét cạn (Brute-force) bằng máy tính hiện đại. |

## 4. Mitigations (Biện pháp giảm nhẹ đề xuất)
* **Trao đổi khóa an toàn:** Sử dụng giao thức Diffie-Hellman hoặc RSA để trao đổi khóa bí mật thay vì gửi trực tiếp.
* **Xác thực dữ liệu:** Thêm mã HMAC (Hash-based Message Authentication Code) vào gói tin để kiểm tra tính toàn vẹn.
* **Nâng cấp thuật toán:** Sử dụng AES-256 thay cho DES để tăng cường độ bảo mật chống vét cạn.

## 5. Residual Risks (Rủi ro còn sót lại)
* **Endpoint Compromise:** Nếu máy tính của người gửi hoặc người nhận bị nhiễm mã độc, kẻ tấn công vẫn có thể lấy trộm khóa trực tiếp từ bộ nhớ RAM.
