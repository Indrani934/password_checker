import re

def check_password_strength(password):
    length_ok = len(password) >= 8
    complexity_ok = bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', password))
    # You may need to update the regex pattern for special characters based on your requirements
    uniqueness_ok = not is_common_password(password)
    
    if length_ok and complexity_ok and uniqueness_ok:
        return "Strong"
    elif length_ok or complexity_ok or uniqueness_ok:
        return "Medium"
    else:
        return "Weak"

def is_common_password(password):
    common_passwords = ["password", "123456", "qwerty"]  # Add more common passwords
    return password in common_passwords

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)
