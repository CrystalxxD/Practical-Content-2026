def check_api_key(key):
    valid_keys = ["key1", "key2", "mysecret"]
    if key in valid_keys:
        return True
    else:
        return False

# Test examples
print(check_api_key("key2"))      # True
print(check_api_key("wrongkey"))  # False