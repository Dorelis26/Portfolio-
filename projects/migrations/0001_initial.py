# Generated by Django 4.1.4 on 2023-02-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desciption', models.TextField()),
                ('technology', models.CharField(max_length=100)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
