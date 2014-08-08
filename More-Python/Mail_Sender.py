import smtplib
import os


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# take password variable from .bashrc file
mail_pass = str(os.getenv("MAIL_PASS"))
server.login('root_dck@gmail.com', mail_pass)

server.sendmail('from_root_dck@gmail.com',
                'sent_to_address_dck@gmail.com',
                'my mail content is DCK was here')