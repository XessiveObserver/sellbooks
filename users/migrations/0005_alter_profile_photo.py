# Generated by Django 4.0 on 2022-12-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_age_alter_profile_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='avatar.jpg', upload_to='users/%d/%m/%Y/'),
        ),
    ]
