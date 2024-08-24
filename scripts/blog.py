import datetime
import os

# Contents of the blog post
title = input("Title > ")
finished = False
paragraphn = 1
paragraphs = []

while finished == False:
    paragraph = input(f"Paragraph {paragraphn} >")

    if paragraph == "!STOP!":
        break

    paragraphs.append(paragraph)
    paragraphn += 1

day = datetime.datetime.utcnow().strftime("%d-%m-%Y")
time = datetime.datetime.utcnow().strftime("%H:%M")
date = f"{day}-{time}"
title += f" {date}"

# HTML stuff
html_output = f"<html>\n<head>\n<link rel=\"stylesheet\" href=\"../../static/main.css\">\n<title>{title}</title>\n</head>\n<body>\n"

html_output += f"<div class=\"heading\">\n<!-- Generated from scripts/blog.py -->\n<h1>{title}</h1>\n</div>\n<br>"
html_output += f"<div class=\"main-content\">\n"

for p in paragraphs:
    if str(p).startswith("<") and str(p).endswith(">"): # Inline HTML
        html_output += f"{p}\n"
    else:
        html_output += f"<p>{p}</p>\n"

html_output += f"</div>\n</body>\n</html>"

if os.path.exists(f"blog/{day}/") == False:
    os.mkdir(f"blog/{day}/")

html_file = open(f"blog/{day}/{date}.html", "x")
html_file.write(html_output)
html_file.close()

blog_file = open("blog/main.html", "r")
file_contents = blog_file.read()
file_contents = file_contents.replace("</div>\n</body>\n</html>", f"<a href=\"{day}/{date}.html\">{date}</a><br>\n</div>\n</body>\n</html>")
blog_file = open("blog/main.html", "w")
print(file_contents)
blog_file.write(file_contents)
blog_file.close()
