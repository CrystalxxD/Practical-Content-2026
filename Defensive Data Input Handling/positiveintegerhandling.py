while True:
    value = input("Enter a positive integer: ")
    if value.isdigit():
        num = int(value)
        if num > 0:
            print("You entered", num)
            break
        else:
            print("Number must be positive.")
    else:
        print("Please enter a valid integer.")