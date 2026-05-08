import pytest
import struct

from des_socket_utils import (
    pad,
    unpad,
    build_packet,
    parse_header,
    BLOCK_SIZE,
    HEADER_SIZE,
)

# =========================================================
# Tests for PKCS#7 Padding & Unpadding
# =========================================================

def test_pad_basic():
    """Kiểm tra padding PKCS#7 được thêm đúng."""
    
    data = b"12345"   # 5 bytes
    padded = pad(data)

    # Sau padding phải đủ 8 bytes
    assert len(padded) == BLOCK_SIZE

    # Thiếu 3 bytes -> thêm \x03\x03\x03
    assert padded == b"12345\x03\x03\x03"


def test_pad_full_block():
    """Nếu dữ liệu đủ 1 block, phải thêm 1 block padding mới."""

    data = b"12345678"  # đúng 8 bytes
    padded = pad(data)

    # Sau padding sẽ thành 16 bytes
    assert len(padded) == BLOCK_SIZE * 2

    # Block cuối phải toàn bộ là \x08
    assert padded[8:] == b"\x08" * BLOCK_SIZE


def test_unpad_valid():
    """Kiểm tra gỡ padding hợp lệ."""

    data = b"FIT4012\x01"

    result = unpad(data)

    assert result == b"FIT4012"


def test_unpad_invalid_value():
    """Kiểm tra lỗi khi padding không hợp lệ."""

    invalid_data = b"FIT4012\x05"

    with pytest.raises(ValueError, match="Padding PKCS#7 không hợp lệ"):
        unpad(invalid_data)


def test_unpad_empty():
    """Kiểm tra lỗi khi dữ liệu rỗng."""

    with pytest.raises(ValueError, match="Dữ liệu rỗng"):
        unpad(b"")


# =========================================================
# Tests for Header & Packet Construction
# =========================================================

def test_build_packet_structure():
    """Kiểm tra cấu trúc packet đúng định dạng."""

    key = b"KEY12345"
    iv = b"IV123456"
    cipher = b"ENCRYPTED_DATA"

    packet = build_packet(key, iv, cipher)

    # Tổng độ dài:
    # 8 bytes key
    # 8 bytes iv
    # 4 bytes length
    # len(cipher) bytes ciphertext

    expected_length = 8 + 8 + 4 + len(cipher)

    assert len(packet) == expected_length

    # Kiểm tra key
    assert packet[:8] == key

    # Kiểm tra iv
    assert packet[8:16] == iv

    # Kiểm tra độ dài ciphertext
    length_in_packet = struct.unpack("!I", packet[16:20])[0]

    assert length_in_packet == len(cipher)


def test_parse_header_success():
    """Kiểm tra parse header thành công."""

    header_raw = (
        b"K" * 8 +
        b"I" * 8 +
        struct.pack("!I", 100)
    )

    key, iv, length = parse_header(header_raw)

    assert key == b"KKKKKKKK"
    assert iv == b"IIIIIIII"
    assert length == 100


def test_parse_header_wrong_size():
    """Kiểm tra lỗi khi header không đủ kích thước."""

    with pytest.raises(ValueError, match="Header phải dài đúng 20 byte"):
        parse_header(b"short")


def test_roundtrip_packet():
    """Kiểm tra đóng gói và đọc lại packet."""

    key = b"8bytekey"
    iv = b"8byte_iv"
    cipher = b"some_secret_payload"

    packet = build_packet(key, iv, cipher)

    # Parse lại header
    parsed_key, parsed_iv, parsed_length = parse_header(
        packet[:HEADER_SIZE]
    )

    # Lấy ciphertext
    parsed_cipher = packet[HEADER_SIZE:]

    assert parsed_key == key
    assert parsed_iv == iv
    assert parsed_length == len(cipher)
    assert parsed_cipher == cipher
