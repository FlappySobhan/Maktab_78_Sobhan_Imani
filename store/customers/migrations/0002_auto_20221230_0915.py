# Generated by Django 3.1.14 on 2022-12-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=60, null=True, unique=True),
        ),
    ]
