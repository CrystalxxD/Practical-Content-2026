#sessions = {}

#def create_session(user_id):
#    # Sets login_time to None - improve this to capture the actual login time (current timestamp)
#    sessions[user_id] = {'data': {}, 'login_time': None}

#def login_user(user_id):
#    sessions[user_id]['login_time'] = 0  # This should be replaced with the real current time

# Task:
# - Update create_session and login_user to correctly store the current login timestamp.
# - Implement a function is_session_active(user_id, timeout) that returns True if the user session is active within the timeout period.

import time

sessions = {}

def create_session(user_id):
    # Store the current timestamp when the session is created
    sessions[user_id] = {
        'data': {},
        'login_time': time.time()
    }

def login_user(user_id):
    # Update login_time to the current timestamp
    if user_id in sessions:
        sessions[user_id]['login_time'] = time.time()

def is_session_active(user_id, timeout):
    if user_id not in sessions:
        return False
    
    login_time = sessions[user_id]['login_time']
    
    if login_time is None:
        return False
    
    current_time = time.time()
    
    # Check if session is within timeout period
    return (current_time - login_time) <= timeout