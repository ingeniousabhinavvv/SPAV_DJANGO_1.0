# Generated by Django 4.0.4 on 2022-05-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0006_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='facultyPhone',
            field=models.IntegerField(max_length=20),
        ),
    ]
