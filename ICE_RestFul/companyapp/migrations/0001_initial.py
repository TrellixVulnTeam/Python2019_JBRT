# Generated by Django 2.1.10 on 2019-07-29 02:18

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('share_price_date', models.DateField(default=django.utils.timezone.now)),
                ('share_price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('comments', models.TextField(default='', validators=[django.core.validators.MaxLengthValidator(256)])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
