#def process_data(a, b):
#    try:
#        print("Starting process")
#        result = a / b  # Can throw ZeroDivisionError
#        print("Process complete")
#    except:
#        print("An error occurred")  # Too broad - catch specific exceptions instead
#    return result  # This returns result even if exception happened, which could cause errors

# Task:
# - Modify to catch specific exceptions (e.g., ZeroDivisionError).
# - Return None or an appropriate value if an exception occurs.
# - Add a finally block that prints a message indicating function execution has finished.


def process_data(a, b):
    result = None
    try:
        print("Starting process")
        result = a / b
        print("Process complete")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid data type")
    finally:
        print("Function execution has finished")
    