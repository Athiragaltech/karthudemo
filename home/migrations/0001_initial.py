# Generated by Django 5.1 on 2024-08-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('desig', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
            ],
        ),
    ]
