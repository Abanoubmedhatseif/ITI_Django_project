# Generated by Django 4.0.10 on 2024-04-08 15:10

import User.models
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must contain only alphanumeric characters.', regex='^[a-zA-Z0-9]+$'), django.core.validators.MinLengthValidator(5, message='Username must be at least 5 characters long.')])),
                ('first_name', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_first_name', message='First name must contain only letters.', regex='^[a-zA-Z]+$'), django.core.validators.MinLengthValidator(5, message='first name must be at least 5 characters long.')])),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Invalid email format.')])),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(code='invalid_password', message='Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character.', regex='^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])[0-9a-zA-Z!@#$%^&*()_+]{8,}$')])),
                ('shipping_address', models.CharField(blank=True, max_length=100)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to=User.models.upload_to)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
