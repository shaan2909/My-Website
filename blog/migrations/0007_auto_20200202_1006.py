# Generated by Django 3.0.2 on 2020-02-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_authorinterview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
