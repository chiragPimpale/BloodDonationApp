# Generated by Django 4.0.2 on 2022-03-03 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(max_length=50)),
                ('blood_group', models.CharField(blank=True, max_length=20, null=True)),
                ('full_name', models.CharField(max_length=50)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestToBloodBankModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(max_length=100)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('requested_group', models.CharField(max_length=20)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('blood_requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acceptor', to=settings.AUTH_USER_MODEL)),
                ('blood_requested_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
