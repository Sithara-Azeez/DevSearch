# Generated by Django 4.0.1 on 2022-02-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='photos/'),
        ),
    ]
