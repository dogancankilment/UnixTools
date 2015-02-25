from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
from django.http import HttpResponse

# from django.template.loader import get_template
# from django.shortcuts import render


def mail_sender():
    subject, from_email, to = 'hello',\
                              'surveydck@gmail.com',\
                              'dogancankilment@gmail.com'

    hash_key_example = "123"  # example variable to send
    transmitted_key = Context({'hash_key': hash_key_example})

    # plaintext = get_template('email/email_content.html')
    # text_content = plaintext.render(transmitted_key)

    # sending view's variable to template
    text_content = render_to_string('email/email_content.html',
                                    transmitted_key)

    msg = EmailMultiAlternatives(subject,
                                 text_content,
                                 from_email,
                                 [to])
    msg.send()

    return HttpResponse("Mission complete. Everything is perfect.. :) ")

if __name__ == '__main__':
    mail_sender()