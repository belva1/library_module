# Generated by Django 4.2.4 on 2023-08-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_author_book_borrowrequestmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
