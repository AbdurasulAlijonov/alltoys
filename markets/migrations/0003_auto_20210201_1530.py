# Generated by Django 3.1.5 on 2021-02-01 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0002_market'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='market',
        ),
        migrations.AddField(
            model_name='product',
            name='market',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='markets.market', verbose_name="Do'kon"),
        ),
    ]
