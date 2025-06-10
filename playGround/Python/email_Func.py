import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Send(sender_email, sender_password, receiver_email, subject, body):
    """
    Sends an email using Gmail's SMTP server.

    Args:
        sender_email (str): The sender's Gmail address.
        sender_password (str): The sender's Gmail password or app password.
        receiver_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body (plain text )
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    part = MIMEText(body, "plain")
    message.attach(part)

    try:
        # Use port 587 and starttls() for Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"Email sent successfully to {receiver_email}!")
        return True  # Indicate success
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")
        return False  # Indicate failure

def Send_Email_Saved_Session(setting, session):
    """
    Reads sender credentials from a JSON file and email content from a JSON file, then sends emails.

    Args:
        setting (str): Path to the JSON file containing sender email and password.
        session (str): Path to the JSON file containing email subjects, bodies, and a list of recipient emails.
    """
    try:
        with open(setting, 'r', encoding='utf-8') as file1:
            sender_data = json.load(file1)
            # The JSON in 'setting' is a list containing a dictionary. Access it correctly:
            sender_email = sender_data[0].get('account')
            sender_password = sender_data[0].get('password')

            if not sender_email or not sender_password:
                print(f"Invalid sender credentials in {setting}.")
                return

        with open(session, 'r', encoding='utf-8') as file2:
            session_data = json.load(file2)
            emails = []
            all_emails_sent_successfully = True # Assume all emails will be sent successfully
            for row in session_data:
                subject = row.get('subject')
                body = row.get('body')
                recipients = row.get('emails',)  # Get the list of emails, default toif not present.

                if not isinstance(recipients, list):
                    print(f"Emails must be a list in session data: {row}")
                    continue # Skip to the next row

                for receiver_email in recipients:
                    if sender_email and sender_password and receiver_email and subject and body:
                        if not Send(sender_email, sender_password, receiver_email, subject, body):
                            all_emails_sent_successfully = False # If any email send fails, change the flag
                    else:
                        print("One or more email data is missing")
            if all_emails_sent_successfully:
                print("All emails in the session were sent successfully!")
            else:
                print("One or more emails failed to send.")

    except FileNotFoundError:
        print("One or both files not found.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
Send_Email_Saved_Session('setting.json','test1.json')