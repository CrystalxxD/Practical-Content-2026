import re

def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9_.]{4,19}$'
    if re.fullmatch(pattern, username):
        return "Valid username"
    else:
        return "Invalid username"

# Test examples
print(validate_username("Pass_123"))  # Valid
print(validate_username("12Hello"))     # Invalid (starts with number)
print(validate_username("h.i"))        # Invalid (too short)