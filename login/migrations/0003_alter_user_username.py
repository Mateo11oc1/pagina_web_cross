# Generated by Django 4.2.4 on 2023-11-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre de usuario'),
        ),
    ]
