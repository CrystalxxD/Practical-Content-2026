while True:
    username = input("Please enter your username: ")
    
    if '<script>' in username:
        print("name cannot contain <script>")

    elif username.isalnum() == False:
        print("name cannot contain special characters")
    
    elif len(username) <3 or len(username)>15:
        print('username cannot be longer than 15 and less than 3')

    else:
        print("username is valid")
