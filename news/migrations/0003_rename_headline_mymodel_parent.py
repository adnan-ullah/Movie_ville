# Generated by Django 3.2.5 on 2022-03-10 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_mymodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='headline',
            new_name='parent',
        ),
    ]
