import smtplib


class NotificationManager:
    def __init__(self):
        self.MY_PASSWORD = "enter yours here"
        self.MY_EMAIL = "enter yours here"

    def send_mail(self, user_email, message):
        # send mail notification
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.MY_EMAIL, self.MY_PASSWORD)
            connection.sendmail(from_addr=self.MY_EMAIL,
                                to_addrs=user_email,
                                msg=f"Subject: Your Flight is Ready\n\n{message}")



