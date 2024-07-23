# Generated by Django 5.0.3 on 2024-07-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useraccount",
            name="bg_account_image",
        ),
        migrations.AlterField(
            model_name="useraccount",
            name="socials",
            field=models.ManyToManyField(
                blank=True,
                db_index=True,
                related_name="user_acccount",
                to="users.useraccountsocialurl",
            ),
        ),
    ]