# Generated by Django 4.0.4 on 2022-05-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0004_rename_goi_goiinitiative'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altText', models.CharField(max_length=250)),
                ('studentworksImage', models.ImageField(null=True, upload_to='studentworks')),
            ],
        ),
    ]
