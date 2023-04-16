""" This program encrypt or decrypt a message based on the user secret shift code"""

# LISTS OF ALPHABETS AND A WHITESPACE --- CAN BE UPDATED WITH SYMBOLS AND NUMBERS IF NEED BE:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
           '%', '&', '(', ')', '*', '+', '/', '[', ']', '{', '}', '-', '.', '@', '"', "'", '^', '_', '?', ':', ';', '~',
           '`', '|', ' ']

# THE CIPHER LOGO IN ASCII ART
logo = """
          88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88  """

# PRINTING A WELCOME MESSAGE:
print(logo)
print("Welcome to your favourite Caesar Cipher Encryption and Decryption Machine")
print("This machine works well but slows down as the shift number approaches a large value😨😨😨\n\n")


# START GAME:
game_not_over = True
while game_not_over:

    # ASK FOR USER'S INPUT:
    what_to_do = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:\n").lower()
    message = input("Input your message. Note: All cases are allowed:\n")
    shift_key = int(input("By how many numbers do you want to shift your message:\n"))

    # BUILD AN ENCRYPTION AND DECRYPTION FUNCTION:

    def encrypt(texts=message, key=shift_key):
        """This function encrypt the message"""
        encrypted_texts = ""
        # Loop through each element in the user's inputted message
        for text in texts:
            # For every element(text) in texts, add its index in letter to key to a variable Shift_forward:
            shift_forward = letters.index(text) + key
            # while shift_forward is greater than the length of letter, reduce it till it becomes less
            while shift_forward > len(letters):
                shift_forward = shift_forward - len(letters)
            # make an encrypted text from letter using the shift_forward
            encrypted_texts += letters[shift_forward]
        # print your encrypted text
        print(encrypted_texts)


    def decrypt(texts=message, key=shift_key):
        """This function decrypt an encrypted message given the shift code"""
        decrypted_texts = ""
        # Loop through each element in the user's encrypted message
        for text in texts:
            # For element in texts, subtract its index in letter from key, store in a variable Shift_backward
            shift_backward = letters.index(text) - key
            while shift_backward < -(len(letters)):
                shift_backward = shift_backward + len(letters)
            decrypted_texts += letters[shift_backward]
        # print your decrypted text
        print(decrypted_texts)


    # FROM USER'S CHOICE, SELECT WHAT TO DO:
    if what_to_do == "encode":
        encrypt()
    if what_to_do == "decode":
        decrypt()

    # CHECK IF USER WILL WANT TO PERFORM AN ACTION AGAIN:
    contd_game = input("Do you want to try again? Type y for yes and any other letter to stop:\n").lower()
    if contd_game == "y":
        game_not_over = True
    else:
        game_not_over = False
