from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 2)

    with pytest.raises(TypeError):
        encrypt_message("Guilherme", "a")

    assert_one = encrypt_message("Guilherme", 15)
    assert assert_one == "emrehliuG"

    assert_two = encrypt_message("Guilherme", 4)
    assert assert_two == "emreh_liuG"

    assert_three = encrypt_message("Guilherme", 5)
    assert assert_three == "hliuG_emre"
