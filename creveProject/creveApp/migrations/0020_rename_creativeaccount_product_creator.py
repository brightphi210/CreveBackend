# Generated by Django 4.1.3 on 2023-08-05 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creveApp', '0019_alter_creativeaccount_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='creativeAccount',
            new_name='creator',
        ),
    ]
