# Generated by Django 4.1.6 on 2023-02-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, upload_to='dishes/%Y_%m_%d'),
        ),
    ]
