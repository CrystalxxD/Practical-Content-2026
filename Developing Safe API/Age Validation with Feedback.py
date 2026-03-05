def validate_age(age):
    if not age.isdigit():
        return "Age must be a number"
    age_num = int(age)
    if not (0 <= age_num <= 120):
        return "Age must be between 0 and 120"
    return "Valid"

# Test examples
print(validate_age("abc"))  # Age must be a number
print(validate_age("150"))  # Age must be between 0 and 120
print(validate_age("25"))   # Valid