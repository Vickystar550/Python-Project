import smtplib

PASSWORD = "dzcshwpgyrhmgckn"
MY_EMAIL = "vickystarnice550@gmail.com"
receivers_address = "victornice550@gmail.com"


# open a connection
connection = smtplib.SMTP("smtp.gmail.com")

# secure the connection with TLS to avoid interception:
connection.starttls()

# login:
connection.login(user=MY_EMAIL, password=PASSWORD)

# send mail:
connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Hello\n\nVictor Nice")

# close the connection
connection.close()


