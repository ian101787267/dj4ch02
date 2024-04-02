# Generated by Django 5.0.3 on 2024-04-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Location",
        ),
        migrations.RemoveField(
            model_name="post",
            name="subject",
        ),
        migrations.AddField(
            model_name="post",
            name="body",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
