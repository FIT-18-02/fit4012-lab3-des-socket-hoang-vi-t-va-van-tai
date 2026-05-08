from des_socket_utils import (
    encrypt_des_cbc,
    decrypt_des_cbc,
    build_packet,
    parse_header,
    HEADER_SIZE,
)


# =========================================================
# Tests for Sender / Receiver Contract
# =========================================================

def test_protocol_contract_order_is_key_iv_length_ciphertext():
    """
    Kiểm tra packet được đóng gói đúng thứ tự:
    Key -> IV -> Length -> Ciphertext
    """

    plaintext = b"FIT4012 contract test"

    key, iv, cipher_bytes = encrypt_des_cbc(
        plaintext,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    packet = build_packet(key, iv, cipher_bytes)

    # -----------------------------------------------------
    # Packet format:
    # [0:8]   -> Key
    # [8:16]  -> IV
    # [16:20] -> Cipher length
    # [20:]   -> Ciphertext
    # -----------------------------------------------------

    assert packet[:8] == key
    assert packet[8:16] == iv

    # Ciphertext bắt đầu từ byte thứ 20
    assert len(packet[20:]) == len(cipher_bytes)

    # DES block size phải chia hết cho 8
    assert len(cipher_bytes) % 8 == 0


def test_sender_receiver_roundtrip():
    """
    Kiểm tra toàn bộ luồng:
    Encrypt -> Build Packet -> Parse Header -> Decrypt
    """

    plaintext = b"Hello FIT4012 DES Socket Lab"

    # Sender encrypt
    key, iv, cipher_bytes = encrypt_des_cbc(
        plaintext,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    # Sender build packet
    packet = build_packet(key, iv, cipher_bytes)

    # Receiver parse header
    recv_key, recv_iv, recv_length = parse_header(
        packet[:HEADER_SIZE]
    )

    # Receiver lấy ciphertext
    recv_cipher = packet[HEADER_SIZE:]

    # Kiểm tra độ dài
    assert recv_length == len(recv_cipher)

    # Receiver decrypt
    decrypted = decrypt_des_cbc(
        recv_key,
        recv_iv,
        recv_cipher
    )

    # So sánh plaintext ban đầu
    assert decrypted == plaintext


def test_packet_header_size():
    """
    Kiểm tra header luôn đúng 20 bytes.
    """

    plaintext = b"Header size test"

    key, iv, cipher_bytes = encrypt_des_cbc(
        plaintext,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    packet = build_packet(key, iv, cipher_bytes)

    header = packet[:HEADER_SIZE]

    assert len(header) == 20


def test_ciphertext_exists_after_header():
    """
    Kiểm tra ciphertext tồn tại sau phần header.
    """

    plaintext = b"DES CBC mode test"

    key, iv, cipher_bytes = encrypt_des_cbc(
        plaintext,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    packet = build_packet(key, iv, cipher_bytes)

    ciphertext = packet[HEADER_SIZE:]

    assert ciphertext == cipher_bytes
    assert len(ciphertext) > 0
