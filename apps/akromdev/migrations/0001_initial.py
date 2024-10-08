# Generated by Django 5.0.3 on 2024-07-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        help_text="Required. 120 charecters.",
                        max_length=120,
                        verbose_name="title",
                    ),
                ),
                (
                    "content",
                    models.TextField(help_text="Required.", verbose_name="content"),
                ),
            ],
            options={
                "verbose_name": "About",
                "verbose_name_plural": "Abouts",
                "db_table": "abouts",
            },
        ),
        migrations.CreateModel(
            name="AboutSocialUrl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Required. 100 charecters.",
                        max_length=100,
                        verbose_name="name",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="200 charecters.",
                        max_length=200,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                ("url", models.URLField(verbose_name="url")),
            ],
            options={
                "verbose_name": "About social url",
                "verbose_name_plural": "Avout social urls",
                "db_table": "about_social_urls",
            },
        ),
        migrations.CreateModel(
            name="Audio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        help_text="Required. 120 charecters.",
                        max_length=120,
                        verbose_name="title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        error_messages={"unique": "With that slug already exists."},
                        help_text="Required. 200 charecters or fewer.",
                        max_length=200,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        upload_to="audio/cover/%Y/%m/%d/", verbose_name="cover"
                    ),
                ),
                (
                    "audio",
                    models.FileField(
                        upload_to="audio/audio/%Y/%m/%d/", verbose_name="audio"
                    ),
                ),
            ],
            options={
                "verbose_name": "Audio",
                "verbose_name_plural": "Audios",
                "db_table": "audios",
            },
        ),
        migrations.CreateModel(
            name="AudioCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Required. 100 charecters",
                        max_length=100,
                        verbose_name="name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Audio Category",
                "verbose_name_plural": "Audio Categories",
                "db_table": "audio_categories",
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Required. 100 charecters.",
                        max_length=100,
                        verbose_name="name",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Required. 120 charecters.",
                        max_length=120,
                        verbose_name="email address",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        help_text="Required. 100 charecters",
                        max_length=100,
                        verbose_name="subject",
                    ),
                ),
                (
                    "message",
                    models.TextField(help_text="Required.", verbose_name="message"),
                ),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
                "db_table": "contacts",
            },
        ),
        migrations.CreateModel(
            name="Picture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "slug",
                    models.SlugField(
                        error_messages={"unique": "With that slug already exists."},
                        help_text="Required. 200 charecters or fewer.",
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                ("image", models.ImageField(upload_to="pictures/images/%Y/%m/%d")),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="description",
                    ),
                ),
            ],
            options={
                "verbose_name": "Picture",
                "verbose_name_plural": "Pictures",
                "db_table": "pictures",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        help_text="Required. 150 charecters",
                        max_length=150,
                        verbose_name="title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        error_messages={"unique": "With that slug already exists"},
                        help_text="Required. 200 charecters.",
                        max_length=200,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "content",
                    models.TextField(help_text="Required.", verbose_name="content"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="active"),
                ),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
                "db_table": "posts",
            },
        ),
        migrations.CreateModel(
            name="PostComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "message",
                    models.TextField(help_text="Required.", verbose_name="message"),
                ),
            ],
            options={
                "verbose_name": "Post comment",
                "verbose_name_plural": "Post Comments",
                "db_table": "post_comments",
            },
        ),
        migrations.CreateModel(
            name="PostCommentLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "Post comment like",
                "verbose_name_plural": "Post comment likes",
                "db_table": "post_comment_likes",
            },
        ),
        migrations.CreateModel(
            name="PostLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "Post like",
                "verbose_name_plural": "Post likes",
                "db_table": "post_likes",
            },
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        db_index=True,
                        help_text="Required. 150 charecters",
                        max_length=150,
                        verbose_name="title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        error_messages={"unique": "With that slug already exists."},
                        help_text="Required. 200 charecters or fewer.",
                        max_length=200,
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "content",
                    models.TextField(help_text="Required.", verbose_name="content"),
                ),
                ("cover", models.ImageField(upload_to="video/covers/%Y/%m/%d/")),
                ("video", models.FileField(upload_to="video/videos/%Y/%m/%d/")),
                ("watched", models.IntegerField(default=0, verbose_name="watched")),
            ],
            options={
                "verbose_name": "Video",
                "verbose_name_plural": "Videos",
            },
        ),
        migrations.CreateModel(
            name="VideoCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Required. 100 charecters",
                        max_length=100,
                        verbose_name="name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Video category",
                "verbose_name_plural": "Video categories",
            },
        ),
        migrations.CreateModel(
            name="VideoComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "message",
                    models.TextField(help_text="Required.", verbose_name="message"),
                ),
            ],
            options={
                "verbose_name": "Video comment",
                "verbose_name_plural": "Video comments",
                "db_table": "video_comments",
            },
        ),
        migrations.CreateModel(
            name="VideoLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "Video like",
                "verbose_name_plural": "Video likes",
                "db_table": "video_likes",
            },
        ),
    ]
