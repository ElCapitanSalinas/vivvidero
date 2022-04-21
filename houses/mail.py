import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(email, apid):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "crosswindrepaints@gmail.com"  # Enter your address

    # return FileResponse(open(f'./media/{apartmentid}.pdf', 'rb'), content_type='application/pdf') PDF

    
    receiver_email = email  # Enter receiver address
    # password = input("Type your password and press enter: ")
    subject = "Hemos terminado el proceso de remodelación digital!"
    body = "Nuestro software ha determinado una selección de imagenes que se ajustan a los espacios que has subido en nuestro portal web!, te dejamos un pdf a continuación."

    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = f'./media/{apid}.pdf'  # In same directory as script
    # filename = f'{apartmentid}.pdf'

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

        
        
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, "CWR2020#")
        server.sendmail(sender_email, receiver_email, text)
