# Generated by Django 3.0.1 on 2019-12-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='employer',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
