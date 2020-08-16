# Generated by Django 3.0.7 on 2020-08-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('user', models.CharField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]