# Generated by Django 3.1.5 on 2021-01-11 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0002_toy'),
    ]

    operations = [
        migrations.CreateModel(
            name='addres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=25)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='toy',
            name='tags',
            field=models.ManyToManyField(related_name='toys', to='toys.tag'),
        ),
        migrations.AddField(
            model_name='user',
            name='Addres',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='toys.addres'),
        ),
    ]
