# Generated by Django 4.0.3 on 2022-04-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_delete_loginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='active',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='logdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
