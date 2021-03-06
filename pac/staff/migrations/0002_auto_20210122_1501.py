# Generated by Django 3.1.5 on 2021-01-22 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job',
            field=models.CharField(blank=True, choices=[('staf', 'کارمند'), ('send', 'مدیر محصول'), ('plan', 'حسابدار')], max_length=4, null=True, verbose_name='سمت'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Ustaff', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
