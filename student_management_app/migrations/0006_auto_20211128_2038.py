# Generated by Django 3.0.7 on 2021-11-28 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='Enum',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
