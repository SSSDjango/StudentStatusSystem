# Generated by Django 4.2.5 on 2023-11-30 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0020_term_current_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offeredsubject',
            name='units',
        ),
        migrations.AddField(
            model_name='offeredsubject',
            name='department',
            field=models.CharField(default='DPSM', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='first_enrollment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='first_term', to='login_app.term'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_enrollment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recent_term', to='login_app.term'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='units',
            field=models.IntegerField(default=3),
        ),
    ]
