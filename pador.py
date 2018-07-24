from Crypto.Cipher import AES
# import os
key = "0123456789heylow"
iv = "1111222233334444"
blocksize=16

def decr(ciphertext):
  cipher = AES.new(key, AES.MODE_CBC, iv)
  return ispkcs7(cipher.decrypt(ciphertext))

def ispkcs7(plaintext):
  l = len(plaintext)
  c = ord(plaintext[l-1])                       
  if (c > blocksize) or (c < 1):
    return "PADDING ERROR"
  if plaintext[l-c:] != chr(c)*c:
    return "PADDING ERROR"
  return plaintext

def encr(plaintext):
  cipher = AES.new(key, AES.MODE_CBC, iv)
  ciphertext = cipher.encrypt(pkcs7(plaintext))
  return ciphertext

def pkcs7(plaintext):
  padbytes = blocksize - len(plaintext) % blocksize
  pad = padbytes * chr(padbytes)
  return plaintext + pad 
