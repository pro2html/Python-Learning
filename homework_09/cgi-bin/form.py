import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("login", "не задано")
text2 = form.getfirst("password", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>login: {}</p>".format(text1))
print("<p>password: {}</p>".format(text2))

print("""</body>
        </html>""")

import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("login", "не задано")
text2 = form.getfirst("password", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>login: {}</p>".format(text1))
print("<p>password: {}</p>".format(text2))

print("""</body>
        </html>""")