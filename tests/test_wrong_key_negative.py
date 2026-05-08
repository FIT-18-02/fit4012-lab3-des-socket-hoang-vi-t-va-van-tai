import pytest

from des_socket_utils import (
    encrypt_des_cbc,
    decrypt_des_cbc,
)


# =========================================================
# Negative Tests:
# Wrong Key
# =========================================================

def test_wrong_key_should_not_recover_original_plaintext():
    """
    Kiểm tra dùng sai key sẽ:
    - giải mã lỗi
    hoặc
    - không khôi phục đúng plaintext
    """

    plain = b"Thong diep dung de test wrong key"

    # =====================================================
    # Encrypt với key đúng
    # =====================================================

    key, iv, cipher_bytes = encrypt_des_cbc(
        plain,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    # =====================================================
    # Giả lập attacker / receiver dùng sai key
    # =====================================================

    wrong_key = b"87654321"

    try:
        recovered = decrypt_des_cbc(
            cipher_bytes,
            wrong_key,
            iv
        )

        # Nếu không lỗi thì plaintext phải khác
        assert recovered != plain

    except ValueError:
        # Padding lỗi -> expected
        assert True


def test_another_wrong_key():
    """
    Kiểm tra với một key sai khác.
    """

    plain = b"FIT4012 DES CBC test"

    key, iv, cipher_bytes = encrypt_des_cbc(
        plain,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    wrong_key = b"ABCDEFGH"

    try:
        recovered = decrypt_des_cbc(
            cipher_bytes,
            wrong_key,
            iv
        )

        assert recovered != plain

    except ValueError:
        assert True


def test_wrong_key_random_data():
    """
    Kiểm tra giải mã bằng key sai với dữ liệu dài hơn.
    """

    plain = (
        b"This is a longer plaintext message "
        b"for testing wrong DES key behavior."
    )

    key, iv, cipher_bytes = encrypt_des_cbc(
        plain,
        key=b"12345678",
        iv=b"abcdefgh"
    )

    wrong_key = b"ZZZZZZZZ"

    try:
        recovered = decrypt_des_cbc(
            cipher_bytes,
            wrong_key,
            iv
        )

        assert recovered != plain

    except ValueError:
        assert True
