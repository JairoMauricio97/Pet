# Generated by Django 4.2.1 on 2023-05-06 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=100)),
                ('historia', models.TextField()),
                ('imagen', models.FilePathField(path='/img')),
            ],
        ),
    ]
