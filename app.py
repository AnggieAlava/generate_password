import uuid
import base64


def generate_password(length: int = 16) -> str:
    return base64.b64encode(uuid.uuid4().bytes).decode()[0:length]


if __name__ == "__main__":
    print(generate_password())


# Generación del UUID: uuid.uuid4()  = 4e6f6c75-9fa4-41b9-80d3-8d5e69c73c0b

# Conversión a Bytes: uuid.uuid4().bytes = b'Nolu\x9f\xa4A\xb9\x80\xd3\x8d^i\xc7<\x0b'

# Codificación en Base64 = Tm9sdWn6RBudwNw1Ym0DBw==