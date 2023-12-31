# Generated by Django 4.1.6 on 2023-11-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0013_equipe_unique_adversaire_per_equipe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipe",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AlterField(
            model_name="stade",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]
