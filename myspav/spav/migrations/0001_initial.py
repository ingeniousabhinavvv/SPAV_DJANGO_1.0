# Generated by Django 4.0.4 on 2022-05-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carouselImage', models.ImageField(null=True, upload_to='carousel')),
                ('carouseTitle', models.CharField(max_length=250)),
            ],
        ),
    ]
