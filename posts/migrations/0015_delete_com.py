# Generated by Django 5.0 on 2024-10-21 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_com_delete_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Com',
        ),
    ]