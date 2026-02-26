while True:
    filename = input("Enter a filename: ")
    
    if "/" in filename or "\\" in filename:
        print("Filename cannot contain '/' or '\\'.")
        continue
    
    valid = True
    for char in filename:
        if not (char.isalnum() or char in "-_."):
            valid = False
            break
    
    if valid:
        print("Safe filename:", filename)
        break
    else:
        print("Filename can only contain letters, numbers, -, _, and .")