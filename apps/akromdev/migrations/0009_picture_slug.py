# Generated by Django 5.0.3 on 2024-07-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akromdev", "0008_alter_picture_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="picture",
            name="slug",
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]