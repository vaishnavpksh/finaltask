# Generated by Django 3.1.8 on 2024-04-26 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_auto_20240421_1149'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
