while True:
    age_input = input("Enter your age (0-120): ")
    try:
        age = int(age_input)
        if 0 <= age <= 120:
            print(f"Your age is {age}.")
            break
        else:
            print("Age must be between 0 and 120.")
    except ValueError:
        print("Please enter a valid integer.")