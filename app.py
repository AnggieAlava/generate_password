import uuid
import base64


def generate_password(length: int = 16) -> str:
    return base64.b64encode(uuid.uuid4().bytes).decode()[0:length]


if __name__ == "__main__":
    print(generate_password())