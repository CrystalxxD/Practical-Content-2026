import re
import html

def sanitise_comment(comment):
    # Remove <script> tags
    comment = re.sub(r'<script.*?>.*?</script>', '', comment, flags=re.I|re.S)
    # Remove <img> tags
    comment = re.sub(r'<img.*?>', '', comment, flags=re.I|re.S)
    # Escape remaining HTML
    return html.escape(comment)

# Test example
test_comment = '<script>alert(1)</script> Hello <img src="pic.jpg"> World!'
print(sanitise_comment(test_comment))  # " Hello  World!"