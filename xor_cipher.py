def xor_encryption(text, key):
    
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted_text


def xor_decryption(message, key):
    decrypted_text = ""
    for i in range(len(message)):
        decrypted_text += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return decrypted_text



key = input()
plain_text = input()
secret = input()

encrypted_text = xor_encryption(plain_text, key)
decrypted_text = xor_decryption(secret, key)

print(f'Plain Text: {plain_text}')
print(f'Encrypted Text: {encrypted_text}')
print(f'Decrypted Text: {decrypted_text}')
