import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationManager:
    """
    A class to manage sending notifications via various channels.
    Currently supports sending emails.
    """
    
    def __init__(self, email_host, email_port, email_user, email_password):
        """
        Initializes the NotificationManager with email server settings.
        
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
        Sends an email to a specified recipient.
        
        Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        recipient (str): The recipient's email address.
        """
        msg = MIMEMultipart()
        msg['From'] = self.email_user
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Establish a connection to the SMTP server and send the email
        server = smtplib.SMTP(self.email_host, self.email_port)
        server.starttls()  # Encrypts the email
        server.login(self.email_user, self.email_password)
        text = msg.as_string()
        server.sendmail(self.email_user, recipient, text)
        server.quit()

# Example usage:
if __name__ == "__main__":
    email_host = 'smtp.example.com'
    email_port = 587
    email_user = 'your-email@example.com'
    email_password = 'your-email-password'
    notification_manager = NotificationManager(email_host, email_port, email_user, email_password)
    notification_manager.send_email('Test Subject', 'Hello, this is a test message', 'recipient@example.com')
