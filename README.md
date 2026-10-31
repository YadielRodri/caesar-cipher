# Caesar Cipher (Python)

A command-line Caesar cipher program I built while learning Python.

## Features

- Encode a message using a rotation from 1 to 25.
- Decode a message by testing rotations against a word from the original text.
- Keep uppercase and lowercase letters as they are, and leave spaces and punctuation unchanged.
- Count how many possible decoding rotations contain the target word.
- Handle invalid menu choices and rotation inputs.

## How to run

Requires Python 3. No third-party packages are needed.

```bash
python proj01.py
```

Choose `e` to encode, `d` to decode, or `q` to quit.

### Example

Encode `Hello, World!` with rotation `3`:

```text
Encoded message: Khoor, Zruog!
```

For decoding, enter `Khoor, Zruog!` and use `hello` as the target word. The program will identify rotation `3` and print the decoded text.

## Example terminal session

Example encoding and decoding (the main menu appears between commands):

```text
Enter your choice: e
Enter a message: Hello, World!
Enter rotation (1-25): 3
Encoded message: Khoor, Zruog!

Enter your choice: d
Enter a message to decode: Khoor, Zruog!
Enter a word in the original message: hello
Rotation: 3
Decoded message: Hello, World!
Matching rotations: 1
```

## What I practiced

Python strings, `if` statements, `for` and `while` loops, input validation, and the remainder operator (`%`). The program is written without custom functions, as required by the original assignment.
