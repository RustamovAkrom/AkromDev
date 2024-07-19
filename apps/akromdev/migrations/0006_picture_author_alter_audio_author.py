# Generated by Django 5.0.3 on 2024-07-19 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akromdev', '0005_alter_videocomment_user_alter_videolike_user'),
        ('users', '0007_useraccount_bg_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='users.useraccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audio',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audios', to='users.useraccount'),
        ),
    ]
