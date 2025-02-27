from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class PasswordCrypto:
    def __init__(self):
        self.key = ("llpjEp8bx/zox4BIx0HkaETf0zOuHuiDmQXOBeQIwko=")
        if self.key is None:
            raise ValueError("La clé CRYPTO_KEY n'est pas définie dans les variables d'environnement.")
        self.key = base64.b64decode(self.key)
        self.iv = b'This is an IV456'  # IV fixe de 16 octets

    def encrypt(self, password):
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            padded_password = pad(password.encode(), AES.block_size)
            encrypted_password = cipher.encrypt(padded_password)
            return base64.b64encode(encrypted_password).decode('utf-8')
        except Exception as e:
            raise Exception(f"Erreur lors du chiffrement: {str(e)}")

    def decrypt(self, encrypted_password):
        try:
            encrypted_bytes = base64.b64decode(encrypted_password.encode('utf-8'))
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            decrypted_password = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
            return decrypted_password.decode('utf-8')
        except Exception as e:
            raise Exception(f"Erreur lors du déchiffrement: {str(e)}")

    def verify_password(self, plain_password, encrypted_password):
        try:
            decrypted = self.decrypt(encrypted_password)
            return plain_password == decrypted
        except Exception:
            return False
