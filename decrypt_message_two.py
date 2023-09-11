# Read the encrypted message from the file
with open("encrypted_message_two.txt", 'r') as encrypted_file:
    encrypted_message = encrypted_file.readline().strip()

# Calculate the length of the message
message_length = len(encrypted_message)

# Initialize an empty list to store the decrypted characters
decrypted_characters = [''] * message_length

# Perform the reverse transposition decryption
start = 0
end = message_length - 1
swap = True  # Initialize swap as True to start swapping

while start <= end:
    if swap:
        decrypted_characters[start] = encrypted_message[end]
        decrypted_characters[end] = encrypted_message[start]
    else:
        decrypted_characters[start] = encrypted_message[start]
        decrypted_characters[end] = encrypted_message[end]
    start += 1
    end -= 1
    swap = not swap

# Join the characters to form the decrypted message
decrypted_message = ''.join(decrypted_characters)

# Split the decrypted message into words
words = decrypted_message.split()

# Reverse the order of the words
reversed_words = words[::-1]

# Reverse the characters within each word
reversed_characters_words = [''.join(word[::-1]) for word in reversed_words]

# Join the reversed words with reversed characters into a single string
final_decrypted_message = ' '.join(reversed_characters_words)

# Print the decrypted message
print(final_decrypted_message)



