# Generated by Django 4.0.2 on 2022-02-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0006_alter_author_pob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='edition',
        ),
        migrations.AlterField(
            model_name='author',
            name='pob',
            field=models.CharField(choices=[('C', 'Colombia'), ('E', 'Ecuador'), ('V', 'Venezuela')], max_length=1),
        ),
    ]
