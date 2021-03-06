# Generated by Django 2.2.5 on 2019-12-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('admitter', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=30)),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField(null=True)),
                ('admission_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('vaccinations', models.ManyToManyField(blank=True, to='pet_adoptions.Vaccine')),
            ],
        ),
    ]
