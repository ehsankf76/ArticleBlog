# Generated by Django 4.2.3 on 2023-07-12 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_author_image'),
        ('blog', '0008_sad_delete_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sad',
            new_name='Comment',
        ),
    ]
