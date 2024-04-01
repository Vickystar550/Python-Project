""" Welcome to Text to Morse Code Converter

___________________
For convenient measures, here are our symbols and what they represent in the International Morse Code system:

1.   "." (the keyboard full stop or dot character) --> The dit or dot

2.   "_" (the keyboard underscores character) --> The dash

____________________
MORSE's CODE RULES:

1. The space between morse elements for a letter is One Dit

2. The space between letters is Three Dits

3. The space between words is Seven Dits

4. One Dits is one unit length

5. One Dash is Three Dits in unit

6. No difference between uppercase and lowercase
"""

morse_code = {
    'alphabet': {
        'a': '. _',
        'b': '_ . . .',
        'c': '_ . _ .',
        'd': '_ . .',
        'e': '.',
        'f': '. . _ .',
        'g': '_ _ .',
        'h': '. . . .',
        'i': '. .',
        'j': '. _ _ _',
        'k': '_ . _',
        'l': '. _ . .',
        'm': '_ _',
        'n': '_ .',
        'o': '_ _ _',
        'p': '. _ _ .',
        'q': '_ _ . _',
        'r': '. _ .',
        's': '. . .',
        't': '_',
        'u': '. . _',
        'v': '. . . _',
        'w': '. _ _',
        'x': '_ . . _',
        'y': '_ . _ _',
        'z': '_ _ . .',
    },
    'numbers': {
        '1': '. _ _ _ _',
        '2': '. . _ _ _',
        '3': '. . . _ _',
        '4': '. . . . _',
        '5': '. . . . .',
        '6': '_ . . . .',
        '7': '_ _ . . .',
        '8': '_ _ _ . .',
        '9': '_ _ _ _ .',
        '0': '_ _ _ _ _',
    },
    'punctuation': {
        ',': '_ _ . . _ _',
        '?': '. . _ _ . .',
        ':': '_ _ _ . . .',
        '-': '_ . . . . _',
        '"': '. _ . . _ .',
        '(': '_ . _ _ .',
        '=': '_ . . . _',
        '*': '_ . . _',
        '.': '. _ . _ . _',
        ';': '_ . _ . _ .',
        '/': '_ . . _ .',
        "'": '. _ _ _ _ .',
        '_': '. . _ _ . _',
        ')': '_ . _ _ . _',
        '+': '. _ . _ .',
        '@': '. _ _ . _ .',
    }
}

text_input = input('Please enter your text:\n').lower()

results = ''

for character in text_input:
    # Checking for letters
    if character in morse_code.get('alphabet').keys():
        results += f'{morse_code.get("alphabet").get(character)}'
        # adding 3 dits of space between the subsequents morse code for the next letter or number or punctuation
        results += ' '*3
    # Checking for numbers
    elif character in morse_code.get('numbers').keys():
        results += f'{morse_code.get("numbers").get(character)}'
        # adding 3 dits of space between the subsequents morse code for the next letter or number or punctuation
        results += ' '*3
    # Checking for punctuations
    elif character in morse_code.get('punctuation').keys():
        results += f'{morse_code.get("punctuation").get(character)}'
        # adding 3 dits of space between the subsequents morse code for the next letter or number or punctuation
        results += ' '*3
    # Checking for space between words, and adding 7 dits according to Morse's Code Rules
    elif character == " ":
        results += ' '*7

print(results)
