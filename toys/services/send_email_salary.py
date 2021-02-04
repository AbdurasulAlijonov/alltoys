from django.core.mail import send_mail
from toys.models import *

def send_email():
    for company in Company.objects.all():
        jami_oylik = 0
        q = Employee.objects.filter(company=company.id)
        for i in q:
            jami_oylik += int(i['salary'])

        send_mail(
            'Sizning bu oydagi ishchilarga beradigan oyligingiz',
            'miqdori: {0}'.format(jami_oylik),
            [company.admin_email],fail_silently=False,
        )

