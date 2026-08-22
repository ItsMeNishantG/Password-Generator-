# Password-Generator-
🔐  Generates cryptographically secure passwords using python

A lightweight, zero-dependency Python script that generates cryptographically secure passwords using the built-in `secrets` module. 

## Features

- **Cryptographically Secure**: Uses Python's `secrets` module rather than `random`, making it safe against predictability attacks.
- **High Entropy**: Combines uppercase letters, lowercase letters, numbers, and special symbols to ensure maximum complexity.
- **Customizable**: Allows you to easily change the password length by modifying a single argument.
- **Built-in Validation**: Safety check ensures passwords meet a minimum recommended length of 8 characters.

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses standard Python libraries)

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Run the script using Python:

```bash
python password_generator.py
```

## Code Preview

```python
import secrets
import string

def generate_password(length=16):
    """Generates a secure password with letters, numbers, and symbols."""
    if length < 8:
        return "Error: Password length should be at least 8 characters."
        
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(all_characters) for _ in range(length))
    return password

print("Your strong password is:")
print(generate_password(16))
```

## How It Works

- **`secrets.choice()`**: Standard random generators (like Python's `random` module) are predictable. This script utilizes the `secrets` module, which generates tokens secure enough for handling passwords, account authentication, and security keys.
- **`string.punctuation`**: Automatically includes standard special characters (such as `!`, `@`, `#`, `$`, etc.) to fulfill modern website security policies.

## License

This project is open-source and available for personal use.
