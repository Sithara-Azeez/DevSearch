# Generated by Django 4.0.1 on 2022-02-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_tags_tag_remove_project_tags_project_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='VOte_ratio',
            new_name='Vote_ratio',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='website.jpg', null=True, upload_to='photos/'),
        ),
    ]
