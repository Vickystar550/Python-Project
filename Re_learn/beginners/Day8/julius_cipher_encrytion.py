letters = ['.', '8', 'O', 'L', '5', '*', '|', 'l', '{', 'C', ')', ' ', '@', '1', '~', 'k', 'R', 'Q', '2', '_', 'o', 'f', '/',
     '`', '&', 'h', 'V', 'W', 'n', 'a', ';', "'", '%', '+', ':', 'D', 'v', 'q', ']', '(', '4', '0', 'Z', 'Y', 'H', 'g',
     'K', 'B', '6', '}', '3', 'A', 'X', 'z', 'd', 'w', 'S', '-', 'y', '?', '7', 'U', 'i', 'j', ' ', 's', '^', 'r', 'F',
     'E', 'T', 'c', 'p', '9', 'M', 'u', 'b', 'I', '$', '!', '#', 'J', 'e', '[', '"', 't', 'm', 'x', 'N', 'P', 'G']


def encryption(message, shift):
    encrypted_text = ""
    for text in message:
        text_index = letters.index(text)
        shifted_forward = text_index + shift

        while shifted_forward > len(letters):
            shifted_forward -= len(letters)
        
        encrypted_text += letters[shifted_forward]
    print(encrypted_text)

def decryption(message, shift):
    decrypted_text = ""
    for text in message:
        text_index = letters.index(text)
        shifted_backward = text_index - shift

        while shifted_backward < -(len(letters)):
            shifted_backward += len(letters)

        decrypted_text += letters[shifted_backward]
    print(decrypted_text)


encode_decode = input("Do you want to encode or decode??\n").lower()

if encode_decode == "e" or encode_decode == "encode":
    message = input("Enter the message you want to encrypt:\n")
    shift = int(input("Enter your shift number\n"))
    encryption(message, shift)

elif encode_decode == "d" or encode_decode == "decode":
    message = input("Enter the message you want to encrypt:\n")
    shift = int(input("Enter your shift number\n"))
    decryption(message, shift)

else:
    print("Invalid selection")