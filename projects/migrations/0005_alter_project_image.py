# Generated by Django 4.1.4 on 2023-02-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
