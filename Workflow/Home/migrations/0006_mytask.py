# Generated by Django 3.2.4 on 2021-09-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='mytask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
