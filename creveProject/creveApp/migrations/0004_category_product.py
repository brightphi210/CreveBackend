# Generated by Django 4.1.3 on 2023-08-02 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creveApp', '0003_rename_phone_number_creativeaccount_accountname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('category', models.ForeignKey(default='Unknown Value', on_delete=django.db.models.deletion.SET_DEFAULT, to='creveApp.category')),
                ('creativeAccount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='creveApp.creativeaccount')),
            ],
        ),
    ]
