def xor_encryption(text, key):
    
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted_text
    

key = input()
plain_text = input()

encrypted_text = xor_encryption(plain_text, key)

print(f'Plain Text: {plain_text}')
print(f'Encrypted Text: {encrypted_text}')
