# Generated by Django 3.0.6 on 2021-03-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0005_auto_20210301_0957"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="share_code",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
