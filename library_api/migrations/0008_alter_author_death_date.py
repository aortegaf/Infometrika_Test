# Generated by Django 4.0.2 on 2022-02-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0007_remove_book_edition_alter_author_pob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(),
        ),
    ]
