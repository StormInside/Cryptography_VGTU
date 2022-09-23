A = "YuriiAhafonov"
B = 20220362
C = "VILNIUSGEDIMINASTECHNIKALUNIVERSITY"

# Task 1
print("\nTask1\n")


def text_to_a1z26(text: str):
    return [(ord(i)-96)%27 for i in text.lower()]

def a1z26_to_text(numbers: list):
    res = ""
    for i in numbers:
        if i <=26 and i >=1:
            res = res + chr(i+96)
        else:
            raise KeyError("Number must be from a=1 to 26=z")
    return res

result = text_to_a1z26(A)
print(f"A1Z26 code of A = {result}")
print(a1z26_to_text(result))
print()



def text_to_ascii(text: str):
    return [ord(i) for i in text]

def ascii_to_text(numbers: list):
    res = ""
    for i in numbers:
        if i <=127 and i >=0:
            res = res + chr(i)
        else:
            raise KeyError("Number must be from 0 to 127")
    return res
        
result = text_to_ascii(A)
print(f"ASCII code of A = {result}")
print(ascii_to_text(result))
print()



def dec_to_bin(number: int):
    res = ""
    while number >= 1:
        res += str(number % 2)
        number = number // 2
    return res[::-1]

def bin_to_dec(bin_string: str):
    res = 0
    for i in bin_string:
        res = res*2 + int(i) 
    return res

result = dec_to_bin(B)
# Also we can use dec_to_base(B, 2)
print(f"Binary representation of B = {result}")
print(bin_to_dec(result))
print()



def dec_to_base(number: int, base: int):
    res = ""
    while number>0:
        mod = int(number % base)
        if mod<10:
            res += str(mod)
        else:
            res += chr(ord('a')+mod-10) # Small letters to have possibility to made base 36+
        number //= base
    return res[::-1]

def base_to_dec(base_string: str, base: int):
    base_string = base_string[::-1]
    res = 0
    for i in range(len(base_string)):
        mod = base_string[i]
        if mod.isdigit():
            mod = int(mod)
        else:
            mod = ord(mod.lower())-ord('a')+10
        res += mod*(base**i)
    return res

result = dec_to_base(B, 8)
print(f"Octal representation of B = {result}")
print(base_to_dec(result, 8))
print()

result = dec_to_base(B, 16)
print(f"Hexadecimal representation of B = {result}")
print(base_to_dec(result, 16))
print()

result = dec_to_base(B, 64)
print(f"Base64 representation of B = {result}")
print(base_to_dec(result, 64))
print()

result = dec_to_base(B, 58)
print(f"Base58 representation of B = {result}")
print(base_to_dec(result, 58))
print()


# Task 2
print("\nTask2\n")


def encrypt_Caesar(text, k):
    return "".join([chr((ord(i)-95+k)%26+95) for i in text.lower()])

def decrypt_Caesar(text, k):
    return "".join([chr((ord(i)-96-k)%26+96) for i in text.lower()])

result = encrypt_Caesar(A, B%26)
print(f"A using Caesar = {result}")
print(decrypt_Caesar(result, B%26))
print()



def encrypt_Vigenere(text: str, key: str):
    res = []
    while len(key) < len(text):
        key += key
    key = key[:len(text)]
    for i in range(len(text)):
        letter = (ord(text[i])+ord(key[i]))%26
        letter += ord('A')
        res.append(chr(letter))
    return "".join(res)
     
def decrypt_Vigenere(encrypted_text: str, key: str):
    res = []
    while len(key) < len(encrypted_text):
        key += key
    key = key[:len(encrypted_text)]
    for i in range(len(encrypted_text)):
        letter = (ord(encrypted_text[i])-ord(key[i])+26)%26
        letter += ord('A')
        res.append(chr(letter))
    return "".join(res)

result = encrypt_Vigenere(C, str(B))
print(f"C using Vigenere = {result}")
print(decrypt_Vigenere(result, str(B)))
print()


# Task 3
print("\nTask3\n")

from Crypto.Cipher import DES
from Crypto.Util import Padding

# Addind additional characters to key to fit 8 bytes(64 bits) blocks(for situations when key is shorter)
key = Padding.pad(bytes(str(B), 'utf-8'), 8)
# Taking only first 8 bytes block
key = key[:8]
# Addind additional characters to plaintext to fit 8 bytes(64 bits) blocks
text = Padding.pad(bytes(A, 'utf-8'), 8)

des = DES.new(key, DES.MODE_ECB)
encrypted_text = des.encrypt(text)

print(encrypted_text)

decrypted_text = des.decrypt(encrypted_text)
# Removing additional characters
decrypted_text = Padding.unpad(decrypted_text, 8)

print(decrypted_text.decode('utf-8'))

