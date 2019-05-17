# Generated by Django 2.2 on 2019-05-17 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_permissionstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setion',
            fields=[
                ('memberid', models.ForeignKey(db_column='memberid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='posts.Member')),
                ('token', models.CharField(max_length=45)),
                ('expiretime', models.DateTimeField()),
            ],
            options={
                'db_table': 'Setion',
                'managed': False,
            },
        ),
    ]
