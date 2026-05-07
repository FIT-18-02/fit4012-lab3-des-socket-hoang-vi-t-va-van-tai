import pytest
import struct
from des_socket_utils import pad, unpad, build_packet, parse_header, BLOCK_SIZE, HEADER_SIZE

# --- Tests cho Padding & Unpadding ---

def test_pad_basic():
    """Kiểm tra padding thêm đúng số lượng byte còn thiếu."""
    data = b"12345"  # 5 bytes, thiếu 3 bytes để đủ 8
    padded = pad(data)
    assert len(padded) == 8
    assert padded == b"12345\x03\x03\x03"

def test_pad_full_block():
    """Nếu dữ liệu đã đủ 8 bytes, PKCS#7 phải thêm 1 block mới (8 bytes \x08)."""
    data = b"12345678"
    padded = pad(data)
    assert len(padded) == 16
    assert padded[8:] == b"\x08" * 8

def test_unpad_valid():
    """Kiểm tra gỡ padding chính xác."""
    data = b"FIT4012\x01"
    assert unpad(data) == b"FIT4012"

def test_unpad_invalid_value():
    """Trường hợp giá trị padding không khớp với số lượng (Negative Test)."""
    invalid_data = b"FIT4012\x05" # Khai báo padding 5 nhưng chỉ có 1 byte cuối
    with pytest.raises(ValueError, match="Padding PKCS#7 không hợp lệ"):
        unpad(invalid_data)

def test_unpad_empty():
    """Kiểm tra lỗi khi unpad dữ liệu rỗng."""
    with pytest.raises(ValueError, match="Dữ liệu rỗng"):
        unpad(b"")


# --- Tests cho Header & Packet Construction ---

def test_build_packet_structure():
    """Kiểm tra cấu trúc gói tin có đúng thứ tự Key, IV, Length, Ciphertext."""
    key = b"KEY12345"
    iv = b"IV123456"
    cipher = b"ENCRYPTED_DATA"
    
    packet = build_packet(key, iv, cipher)
    
    # Kiểm tra tổng độ dài: 8 (key) + 8 (iv) + 4 (length) + 14 (cipher) = 34
    assert len(packet) == 8 + 8 + 4 + len(cipher)
    assert packet.startswith(key)
    assert packet[8:16] == iv
    
    # Kiểm tra độ dài được đóng gói ở byte 16-20
    length_in_packet = struct.unpack('!I', packet[16:20])[0]
    assert length_in_packet == len(cipher)

def test_parse_header_success():
    """Kiểm tra phân tách header 20 bytes thành các thành phần chuẩn."""
    header_raw = b"K" * 8 + b"I" * 8 + struct.pack('!I', 100)
    key, iv, length = parse_header(header_raw)
    
    assert key == b"KKKKKKKK"
    assert iv == b"IIIIIIII"
    assert length == 100

def test_parse_header_wrong_size():
    """Kiểm tra lỗi khi header không đủ 20 bytes (Negative Test)."""
    with pytest.raises(ValueError, match="Header phải dài đúng 20 byte"):
        parse_header(b"too_short_header")

def test_roundtrip_packet():
    """Kiểm tra luồng: Đóng gói -> Phân tích header -> Kết quả khớp nhau."""
    key, iv, cipher = b"8bytekey", b"8byte_iv", b"some_secret_payload"
    packet = build_packet(key, iv, cipher)
    
    p_key, p_iv, p_len = parse_header(packet[:HEADER_SIZE])
    p_cipher = packet[HEADER_SIZE:]
    
    assert p_key == key
    assert p_iv == iv
    assert p_len == len(cipher)
    assert p_cipher == cipher
