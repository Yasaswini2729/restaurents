# Generated by Django 5.0.7 on 2024-07-31 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='itemName',
            new_name='item',
        ),
    ]