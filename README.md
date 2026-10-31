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

## What I practiced

Python strings, `if` statements, `for` and `while` loops, input validation, and the remainder operator (`%`). The program is written without custom functions, as required by the original assignment.
