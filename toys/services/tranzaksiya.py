from toys.models import *
from django.db import transaction


def my_transaction():
    with transaction.atomic():
        cmp = Company.objects.get(pk=2)
        cmp.name = 'Facebook'
        cmp.save()
        try:
            with transaction.atomic():
                for e in Employee.objects.filter(company__name='Facebook'):
                    e.salary += e.salary / 10
                    e.save()
                raise Exception('Google nomi Facebook ka o\'zgardi, lekin oyliklar oshmadi')
        except:
            pass

