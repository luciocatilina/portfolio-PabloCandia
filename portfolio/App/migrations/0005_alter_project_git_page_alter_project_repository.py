# Generated by Django 4.1 on 2023-02-15 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_remove_project_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git_page',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='repository',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
