# Generated by Django 4.2.5 on 2023-10-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0012_subject_enrolled_subject_slots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.CharField(choices=[('ENROLLED', 'Currently Enrolled'), ('UNENROLLED', 'Not Enrolled'), ('LEAVE OF ABSENCE', 'Leave of Absence')], max_length=200),
        ),
    ]
