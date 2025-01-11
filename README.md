# PySec
**Protect your Python Src, and load it external from your Backend Server**


**Python Explaination**
- This is the Algorithm for decrypt the script server-side based from your backend.
-  Its use **Rc4** encryption for decrypt the python source code from the backend.
```python

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
```

**Php Algo Explained**
- Its basically the same, just to encrypt it.
```php
function encrypt($n, $o) {
    $d = range(0, 255);
    $j = 0;
    for ($i = 0; $i < 256; $i++) {
        $j = ($j + $d[$i] + ord($o[$i % strlen($o)])) % 256;
        $temp = $d[$i];
        $d[$i] = $d[$j];
        $d[$j] = $temp;
    }

    $i = 0;
    $j = 0;
    $azar = '';

    for ($k = 0; $k < strlen($n); $k++) {
        $i = ($i + 1) % 256;
        $j = ($j + $d[$i]) % 256;
        $temp = $d[$i];
        $d[$i] = $d[$j];
        $d[$j] = $temp;
        $azar .= chr(ord($n[$k]) ^ $d[($d[$i] + $d[$j]) % 256]);
    }
    return base64_encode($azar);
}
```

**Example Output**
- here is a encrypted example how its would look.
```json
{
  "stub": "QCi/nQ/DHTA1QCvz5kPPGtgop3Xc1yk6Ya/KSvYP7T/7TQ5sVE8eRFCOGoTvQ1ricGQ+56sfjHuDyzxYKYLXXRPflyF9DveeswfUviyOLA==",
  "now": 1736579805000
}
```

**Overall Explanation**
- You just get the python source encrypted from your backend, **decrypt** it and execute it basically with ```exec```
# Here is the example:
```python
stub = PySec().decrypt(auth['stub'], 'MySecKey!**1')
exec(stub)
```

**⚠️Remember**
- Never run untrusted code or malicius src from anyone, always check the src if possible.

# Star this Repo if you think it helped you!⭐
