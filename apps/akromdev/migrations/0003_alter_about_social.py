# Generated by Django 5.0.3 on 2024-07-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akromdev", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="social",
            field=models.ManyToManyField(
                blank=True, related_name="url_about", to="akromdev.aboutsocialurl"
            ),
        ),
    ]