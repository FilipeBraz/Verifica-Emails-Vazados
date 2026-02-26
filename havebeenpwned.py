import hashlib
import requests

senha = "teste123"
sha1 = hashlib.sha1(senha.encode()).hexdigest().upper()
prefixo = sha1[:5]
sufixo = sha1[5:]

res = requests.get(f"https://api.pwnedpasswords.com/range/{prefixo}")
if sufixo in res.text:
    print("Senha comprometida!")