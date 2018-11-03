key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    result = ''
    for x in plaintext.lower():
        i = (key.index(x) + n) % 26
        result += key[i]
    return result.lower()

def decrypt(n, ciphertext):
    result = ''
    for x in ciphertext:
        i = (key.index(x) - n) % 26
        result += key[i]
    return result
text = "TheDieHasBeenCast"
offset = 3
encrypted = encrypt(offset, text)
print('Encrypted:', encrypted)
decrypted = decrypt(offset, encrypted)
print('Decrypted:', decrypted)
