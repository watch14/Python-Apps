import smtplib
import os
from email.message import EmailMessage

def sendEmail(message: EmailMessage):
    username = "maamounchebbi@gmail.com"
    password = os.environ.get("MC_EMAIL_PASSWORD")  # Make sure this environment variable is set

    # Check if the password is not None
    if password is None:
        print("Error: Email password is not set in environment variables.")
        return False

    try:
        # Use the correct SMTP server address and port
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(username, password)
            server.send_message(message)
        return True
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Please check your username and password.")
        return False
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


# def test_sendEmail():
#     mail = EmailMessage()
#     mail.set_content("This is a test email.")
#     mail['Subject'] = 'Test Email'
#     mail['From'] = 'maamounchebbi@gmail.com'
#     mail['To'] = 'maamounchebbi@gmail.com'  

#     result = sendEmail(mail)
#     if result:
#         print("Test email sent successfully.")
#     else:
#         print("Failed to send test email.")

# test_sendEmail()