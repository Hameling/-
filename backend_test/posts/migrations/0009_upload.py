# Generated by Django 2.2 on 2019-05-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_merge_20190518_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
