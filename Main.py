import secrets
import string

def generate_password(length=16):
    """Generates a secure password with letters, numbers, and symbols."""
    if length < 8:
        return "Error: Password length should be at least 8 characters."
        
    # Combine lowercase, uppercase, numbers, and special characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Securely select random characters
    password = "".join(secrets.choice(all_characters) for _ in range(length))
    return password

# Generate and print a 16-character strong password
print("Your strong password is:")
print(generate_password(16))
