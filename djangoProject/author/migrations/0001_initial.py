# Generated by Django 4.0.5 on 2022-07-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('Id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200, unique=True)),
                ('Forewords', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
