# Generated by Django 4.0 on 2022-11-24 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.FileField(blank=True, null=True, upload_to='books/%Y%m/%d'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/%Y%m/%d'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
