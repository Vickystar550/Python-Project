import smtplib

PASSWORD = "enter your password"
EMAIL = "Enter your email"


class NotificationManager:
    def __init__(self):
        # initializing with login info
        self.MY_PASSWORD = PASSWORD
        self.MY_EMAIL = EMAIL

    def send_mail(self, user_email, message):
        # send mail notification
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.MY_EMAIL, self.MY_PASSWORD)
            connection.sendmail(from_addr=self.MY_EMAIL,
                                to_addrs=user_email,
                                msg=f"Subject: Your Flight is Ready\n\n{message}".encode("utf-8"))


