def xor_decryption(message, key):
    decrypted_text = ""
    for i in range(len(message)):
        decrypted_text += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return decrypted_text
    
key = input()
secretmessage = input()
decrypted_text = xor_decryption(secretmessage, key)
print(f'Decrypted Text: {decrypted_text}')