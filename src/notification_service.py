import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

class NotificationService:
    """
    Manages the sending of notifications for the trading bot.
    """

    def __init__(self, email_host, email_port, email_user, email_password):
        """
        Initializes the notification service with email server settings.
        Args:
        email_host (str): SMTP server host.
        email_port (int): SMTP server port.
        email_user (str): Sender email username.
        email_password (str): Sender email password.
        """
        self.email_host = email_host
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, subject, message, recipient):
        """
        Sends an email notification.
        Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        recipient (str): The recipient's email address.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP(self.email_host, self.email_port)
            server.starttls()
            server.login(self.email_user, self.email_password)
            text = msg.as_string()
            server.sendmail(self.email_user, recipient, text)
            server.quit()
            logging.info(f"Email sent to {recipient}: {subject}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {str(e)}")

# Example usage:
if __name__ == "__main__":
    email_host = 'smtp.example.com'
    email_port = 587
    email_user = 'your-email@example.com'
    email_password = 'your-email-password'
    notification_service = NotificationService(email_host, email_port, email_user, email_password)
    notification_service.send_email('Test Subject', 'This is a test message', 'recipient@example.com')
