# Generated by Django 4.2.3 on 2023-08-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0004_alter_sinhvien_xep_hang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinhvien',
            name='diem_tb',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]