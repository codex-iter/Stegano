
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
data1 = (open("pt1.txt","rb")).read()
ciphertext, tag = cipher.encrypt_and_digest(data1)
file = open("key.txt","wb")                                           
file.write(key)
file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]