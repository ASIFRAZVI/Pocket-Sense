# Generated by Django 5.1.3 on 2025-01-03 10:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMaster',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField()),
                ('phone_number', models.BigIntegerField()),
                ('roll_number', models.CharField(max_length=200)),
                ('semister', models.CharField(max_length=200)),
                ('section', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('default_payment_method', models.CharField(choices=[('upi', 'UPI'), ('cash', 'CASH')], null=True)),
            ],
            options={
                'db_table': 'student_master',
            },
        ),
    ]
