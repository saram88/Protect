# Generated by Django 3.2.21 on 2023-09-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230906_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='renewal',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tag_line',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
