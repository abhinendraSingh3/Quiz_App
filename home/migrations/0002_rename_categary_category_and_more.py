# Generated by Django 4.1 on 2022-10-12 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categary',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categary_name',
            new_name='category_name',
        ),
    ]
