# Generated by Django 4.0.5 on 2022-07-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
