# Generated by Django 3.2 on 2021-10-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users_new',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('mobilenumber', models.CharField(error_messages={'unique': 'This mobile number is already registered. Please login or enter different mobile number '}, max_length=10, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('emailid', models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, max_length=50, unique=True)),
                ('friendslist', models.CharField(blank=True, max_length=20, null=True)),
                ('private', models.BooleanField(default=False, error_messages={'blank': 'Please choose public or private', 'null': 'make private or public check!!'}, null=True)),
                ('otp', models.CharField(max_length=4)),
                ('acc_created', models.CharField(max_length=20)),
            ],
        ),
    ]
