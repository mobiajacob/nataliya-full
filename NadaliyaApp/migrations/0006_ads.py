# Generated by Django 4.2 on 2023-07-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NadaliyaApp', '0005_remove_user_registration_pro_pic_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.FileField(upload_to='images/banner')),
            ],
        ),
    ]
