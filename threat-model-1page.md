# Phân tích Threat Model - Lab 3

## Thông tin nhóm
- **Thành viên 1**: Bùi Văn Tài - **MSSV**: 1871020515
- **Thành viên 2**: Nguyễn Hoàng Việt - **MSSV**: 1871020654

## Assets
Các tài sản quan trọng cần bảo vệ trong hệ thống bao gồm:
- **Nội dung tin nhắn (Plaintext):** Thông tin nhạy cảm được truyền giữa Sender và Receiver.
- **Khóa bí mật (DES Key):** Chìa khóa dùng để mã hóa và giải mã toàn bộ dữ liệu.
- **Tính toàn vẹn của dữ liệu:** Đảm bảo bản tin không bị chỉnh sửa hay giả mạo trên đường truyền mạng.

## Attacker model
Đối tượng tấn công mục tiêu thường là kẻ tấn công xen giữa (Man-in-the-Middle - MitM) hoặc kẻ nghe lén trên mạng nội bộ (Sniffer). Kẻ tấn công có khả năng:
- Chặn bắt các gói tin truyền qua giao thức TCP.
- Đọc được toàn bộ dữ liệu trong Packet (bao gồm cả Key và IV vì chúng được gửi công khai).
- Thay đổi nội dung của bản tin mã hóa (Ciphertext) trước khi nó tới được Receiver.

## Threats
Dưới đây là 3 mối đe dọa cụ thể đối với hệ thống hiện tại:
1. **Lộ thông tin bí mật (Information Disclosure):** Do Key và IV được gửi kèm ngay đầu gói tin dưới dạng plaintext, kẻ tấn công chỉ cần bắt được gói tin là có thể giải mã hoàn toàn nội dung.
2. **Tấn công thay đổi dữ liệu (Tampering):** Kẻ tấn công có thể thay đổi các bit trong Ciphertext. Vì hệ thống thiếu cơ chế xác thực thông điệp, Receiver sẽ giải mã ra dữ liệu sai lệch mà không thể phát hiện.
3. **Tấn công vét cạn (Brute-force):** Thuật toán DES với độ dài khóa 56-bit hiện nay đã quá yếu, có thể bị phá vỡ trong thời gian ngắn bằng các hệ thống máy tính hiện đại.

## Mitigations
Để giảm thiểu các rủi ro trên, nhóm đề xuất các biện pháp sau:
1. **Sử dụng mã hóa bất đối xứng (RSA/Diffie-Hellman):** Thay vì gửi trực tiếp Key, các bên sẽ trao đổi khóa bí mật thông qua các giao thức an toàn.
2. **Áp dụng HMAC (Hash-based Message Authentication Code):** Thêm một mã băm xác thực đi kèm gói tin để Receiver có thể kiểm tra tính toàn vẹn của dữ liệu và phát hiện mọi sự can thiệp.
3. **Nâng cấp thuật toán mã hóa:** Thay thế DES bằng AES-256 để chống lại các cuộc tấn công Brute-force hiệu quả hơn.

## Residual risks
Rủi ro còn sót lại (Residual risks) lớn nhất là **Endpoint Compromise**: Nếu máy tính của người gửi hoặc người nhận bị nhiễm phần mềm độc hại (Malware/Keylogger), kẻ tấn công có thể trích xuất khóa bí mật hoặc bản rõ trực tiếp từ bộ nhớ RAM ngay trước khi quá trình mã hóa diễn ra, dù đường truyền mạng có an toàn đến đâu.
