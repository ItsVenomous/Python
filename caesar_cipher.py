def caesar_cipher_encode(message):
    # Define a mapping for the Caesar cipher
    cipher_mapping = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
        'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
        'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
        'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
        'z': 'a'
    }

    # Convert the message to lowercase
    message = message.lower()

    # Initialize the encoded message
    encoded_message = ''

    # Encode each character in the message
    for char in message:
        # Check if the character is alphabetic
        if char.isalpha():
            # Encode alphabetic characters using the cipher mapping
            encoded_message += cipher_mapping.get(char, char)
        else:
            # If user inputs non alphabetic characters, leave them unchanged
            encoded_message += char
    return encoded_message


def main():
    # Welcome message
    print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
    print("𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓣𝓸 𝓒𝓪𝓮𝓼𝓪𝓻 𝓒𝓲𝓹𝓱𝓮𝓻")
    print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")

    # Get user input
    user_input = input("Enter your message: ").strip()

    # Encode the message using the Caesar cipher
    encoded_message = caesar_cipher_encode(user_input)

    # Print the encoded message
    print("\nHere is your message after encoding:")
    print(encoded_message)


if __name__ == "__main__":
    main()
