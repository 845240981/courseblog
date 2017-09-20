# -*- coding: UTF-8 -*-

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRcord
from courseblog.settings import EMAIL_FROM



def send_email(email,send_type):
    email_record=EmailVerifyRcord()
    code = generate_random_str()
    email_record.email = email
    email_record.code = code
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "在线注册激活链接"
        email_body = "请点击下面的链接激活你的帐号:http://127.0.0.1:8000/active/{0}".format(code)

    elif send_type == "forget":
        email_title = "忘记密码"
        email_body = "请点击下面的链接找回你的密码:http://127.0.0.1:8000/resetpwd/{0}".format(code)


    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        print 'ok'


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUu123456789'
    length = len(chars)-1
    random = Random()
    for i in range(0,randomlength):
        str+=chars[random.randint(0,length)]
    return str
