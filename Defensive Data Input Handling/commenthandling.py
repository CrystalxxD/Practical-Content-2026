while True:
    try:
        comment = input("Enter a comment (max 200 characters): ")
        if len(comment) > 200:
            print("Comment too long!")
            continue
        
        comment_lower = comment.lower()
        if "<script>" in comment_lower:
            comment = comment_lower.replace("<script>", "").replace("</script>", "")
        
        comment = comment.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        print("Your comment is safe:", comment)
        break
    except:
        print("Unexpected error. Try again.")