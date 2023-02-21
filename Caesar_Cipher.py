alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def choice(direction):
    if "encode" == direction:
        encrypt(text,shift)
    elif "decode" == direction:
        decrypt(text,shift)
    else:
        print("Wrong Input")
def decrypt(text,shift):
    original_message = ''
    for i in range(0,len(text)):
        if text[i] in alphabet:
            index = alphabet.index(text[i])
            negative_shift = (index - shift)
            if negative_shift<0:
                original_message += alphabet[(negative_shift+26)]
            else:
                original_message += alphabet[(negative_shift)]
        else:
            original_message += text[i]
    print(f"Original Message:{original_message}")
def encrypt(text,shift):
    # print(f"The plain text message:{text}")
    cipher_txt = ''
    for i in range(0,len(text)):
       if text[i] in alphabet:
           index = alphabet.index(text[i])
           cipher_txt += alphabet[(index+shift)%26]
       else:
           cipher_txt+=text[i]
    print(f"Cipher_txt:{cipher_txt}")

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = list(input("Plain Text:").lower())
shift = int(input("Type the shift number:"))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
choice(direction)