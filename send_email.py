import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

username = 'alikhaniatiyeh@gmail.com'
password = 'ati@2002'

receiver = 'atialikhani8@gmail.com'
context = ssl.create_default_context()

message ="""
Hi !
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

