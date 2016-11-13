from Crypto.Cipher import AES
import base64
import pyqrcode



msg = 'passwords you want to store'.rjust(32)
secret_key = 'my_secretkey123'.rjust(16)
cipher = AES.new(secret_key,AES.MODE_ECB)
encode = base64.b64encode(cipher.encrypt(msg))
qr = pyqrcode.create(encode)
qr.png("qrimg.png",scale=20)

