# Generated by Django 5.1.2 on 2024-12-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_userquizhistory_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='category_image'),
            preserve_default=False,
        ),
    ]
