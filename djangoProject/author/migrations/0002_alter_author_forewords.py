# Generated by Django 4.0.5 on 2022-07-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='Forewords',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
