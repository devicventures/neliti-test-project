# Generated by Django 3.2 on 2021-04-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lattitude', models.DecimalField(decimal_places=7, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=7)),
            ],
        ),
    ]
