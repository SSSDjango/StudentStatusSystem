# Generated by Django 4.2.5 on 2023-09-29 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_offeredsubject_student_term_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='end_date',
            field=models.DateField(default=datetime.date(2023, 9, 30)),
        ),
        migrations.AlterField(
            model_name='term',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 9, 30)),
        ),
    ]
