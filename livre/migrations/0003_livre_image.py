# Generated by Django 4.1 on 2023-07-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livre', '0002_livre_delete_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
