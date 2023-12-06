# Generated by Django 3.2.21 on 2023-12-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('topic', models.CharField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]