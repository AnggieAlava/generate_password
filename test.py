from app import generate_password


def test_password_length():
    assert len(generate_password()) == 16
    print("Longitud de contraseña por defecto es correcta")


def test_password_length_if_set():
    assert len(generate_password(8)) == 8
    print("Longitud de contraseña personalizada es correcta")
