cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

# Reverse the cipher dictionary to create a decryption dictionary
decryption_cipher = {v: k for k, v in cipher.items()}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

# Decrypt the message
decrypted_message = ''.join([decryption_cipher.get(char, char) for char in encrypted_message])

# Print the decrypted message
print(decrypted_message)

encrypted_file.close()
