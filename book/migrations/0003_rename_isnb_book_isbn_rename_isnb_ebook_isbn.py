# Generated by Django 4.1.2 on 2022-11-01 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_ebook_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isnb',
            new_name='isbn',
        ),
        migrations.RenameField(
            model_name='ebook',
            old_name='isnb',
            new_name='isbn',
        ),
    ]
