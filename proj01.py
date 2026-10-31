option = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'

while option != 'q':
    print('==============================')
    print('      CAESAR CIPHER MENU      ')
    print('==============================')
    print('e - Encode a message')
    print('d - Decode a message')
    print('q - Quit')
    print('==============================')

    option = input('Enter your choice: ').lower()

    if option == 'e':
        encMsg = input('Enter a message: ')
        encRot = input('Enter rotation (1-25): ')

        while not encRot.isdigit() or int(encRot) < 1 or int(encRot) > 25:
            print('Invalid rotation. Try again.')
            encRot = input('Enter rotation (1-25): ')

        encRot = int(encRot)
        encoded = ''

        # Move each letter forward
        for letter in encMsg:
            if letter.lower() in alphabet:
                for i in range(len(alphabet)):
                    if alphabet[i] == letter.lower():
                        newPos = (i + encRot) % 26
                        newLetter = alphabet[newPos]

                        if letter.isupper():
                            newLetter = newLetter.upper()

                        encoded = encoded + newLetter
            else:
                encoded = encoded + letter

        print('Encoded message:', encoded)

    elif option == 'd':
        decMsg = input('Enter a message to decode: ')
        decWord = input('Enter a word in the original message: ').lower()

        while decWord == '':
            decWord = input('Please enter a word: ').lower()

        matches = 0

        # Try each rotation to find the word
        for rotation in range(1, 26):
            decoded = ''

            for letter in decMsg:
                if letter.lower() in alphabet:
                    for i in range(len(alphabet)):
                        if alphabet[i] == letter.lower():
                            newPos = (i - rotation) % 26
                            newLetter = alphabet[newPos]

                            if letter.isupper():
                                newLetter = newLetter.upper()

                            decoded = decoded + newLetter
                else:
                    decoded = decoded + letter

            # Separate words when checking for a match
            words = decoded.lower()
            for letter in words:
                if letter not in alphabet:
                    words = words.replace(letter, ' ')

            if decWord in words.split():
                print('Rotation:', rotation)
                print('Decoded message:', decoded)
                matches = matches + 1

        # Custom feature: count matching rotations
        if matches == 0:
            print('No matching rotation found.')

        print('Matching rotations:', matches)

    elif option == 'q':
        print('Thanks for using the Caesar Cipher program. Goodbye!')

    else:
        print('Invalid option. Please try again.')

    print()