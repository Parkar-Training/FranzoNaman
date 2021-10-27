# Generated by Django 3.2 on 2021-10-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_users_new_acc_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_new',
            name='emailid',
            field=models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exists.'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='users_new',
            name='private',
            field=models.BooleanField(default=False, error_messages={'blank': 'Please choose public or private', 'null': 'make private or public check!!'}),
        ),
    ]
