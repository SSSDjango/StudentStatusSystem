# Generated by Django 4.2.5 on 2023-10-20 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0010_alter_userprofile_role_delete_studyplanrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='contact_number',
            field=models.CharField(default='09369216454', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_number',
            field=models.CharField(default=202105277, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(default='DPSM', max_length=200),
            preserve_default=False,
        ),
    ]
