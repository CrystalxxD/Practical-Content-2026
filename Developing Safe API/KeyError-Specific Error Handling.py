def get_username(data):
    try:
        return data['username']
    except KeyError:
        return "Error: Missing username"
    except Exception:
        return "Error: Invalid data"

# Test examples
print(get_username({}))                    # Error: Missing username
print(get_username({'username': 'Chris'})) # Chris