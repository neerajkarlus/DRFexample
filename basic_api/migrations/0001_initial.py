# Generated by Django 3.2.7 on 2021-09-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DRFPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('excellent', 1), ('average', 0), ('bad', -1)], default='average', max_length=50)),
            ],
            options={
                'ordering': ['uploaded'],
            },
        ),
    ]
