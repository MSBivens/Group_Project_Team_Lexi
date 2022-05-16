# Generated by Django 2.2.4 on 2022-05-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('alert_code', models.CharField(max_length=200)),
                ('severity', models.CharField(max_length=200)),
                ('agency', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'list',
            },
        ),
    ]