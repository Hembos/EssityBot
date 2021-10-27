from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import VIEWERS_EMAILS, BOT_EMAIL, BOT_EMAIL_PASSWORD


def send_mail(message):
    bot_email = BOT_EMAIL
    bot_email_password = BOT_EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = BOT_EMAIL
    msg['Subject'] = 'Замечание'
    msg.attach(MIMEText(message, 'plain'))
    server = SMTP('smtp.yandex.ru', 587)

    server.set_debuglevel(True)
    server.starttls()
    server.login(bot_email, bot_email_password)

    for email in VIEWERS_EMAILS:
        msg['To'] = email
        server.send_message(msg)

    server.quit()
