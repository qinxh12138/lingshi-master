# -*- coding: utf-8 -*-  
# __author__:ZHANGJIN
# __time__:2019/1/25 11:11


# 发送邮件
from celery import shared_task
from django.core.mail import send_mail

from group import settings


@shared_task
def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )
