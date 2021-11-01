# Generated by Django 3.2.8 on 2021-11-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the publisher', max_length=50)),
                ('website', models.CharField(help_text="The Publisher's website", max_length=50)),
                ('email', models.EmailField(help_text="The Publisher's email address.", max_length=254)),
            ],
        ),
    ]