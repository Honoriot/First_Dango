# Generated by Django 3.0.2 on 2020-02-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_fruit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='title',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
