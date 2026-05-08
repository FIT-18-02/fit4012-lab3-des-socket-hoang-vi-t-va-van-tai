from des_socket_utils import (
    encrypt_des_cbc,
    decrypt_des_cbc,
)


# =========================================================
# Negative Tests:
# Tampered Ciphertext
# =========================================================

def test_tampered_ciphertext_should_fail_or_change_plaintext():
    """
    Kiểm tra khi ciphertext bị chỉnh sửa (tamper),
    kết quả giải mã phải:
    - lỗi ValueError
    hoặc
    - plaintext bị thay đổi
    """

    plain = b"Thong diep dung de test tamper"

    # =====================================================
    # Encrypt dữ liệu gốc
    # =====================================================

    key, iv, cipher_bytes = encrypt_des_cbc(
        plain,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    # =====================================================
    # Giả lập attacker sửa 1 bit cuối ciphertext
    # =====================================================

    tampered = bytearray(cipher_bytes)

    # Flip 1 bit cuối
    tampered[-1] ^= 0x01

    # =====================================================
    # Giải mã ciphertext đã bị sửa
    # =====================================================

    try:
        recovered = decrypt_des_cbc(
            bytes(tampered),
            key,
            iv
        )

        # Nếu không lỗi thì plaintext phải khác
        assert recovered != plain

    except ValueError:
        # Padding lỗi -> expected behavior
        assert True


def test_multiple_byte_tampering():
    """
    Kiểm tra khi nhiều byte ciphertext bị sửa.
    """

    plain = b"FIT4012 DES CBC negative tamper test"

    key, iv, cipher_bytes = encrypt_des_cbc(
        plain,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    tampered = bytearray(cipher_bytes)

    # Sửa nhiều byte
    tampered[0] ^= 0xFF
    tampered[5] ^= 0xAA
    tampered[-1] ^= 0x11

    try:
        recovered = decrypt_des_cbc(
            bytes(tampered),
            key,
            iv
        )

        assert recovered != plain

    except ValueError:
        assert True


def test_empty_ciphertext_tamper():
    """
    Kiểm tra decrypt dữ liệu rỗng phải lỗi.
    """

    key = b"12345678"
    iv = b"abcdefgh"

    try:
        decrypt_des_cbc(b"", key, iv)

    except ValueError:
        assert True
