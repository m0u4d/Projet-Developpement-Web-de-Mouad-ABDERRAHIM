# Generated by Django 4.1.6 on 2023-11-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0010_alter_equipe_adversaire_alter_equipe_logo_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="equipe",
            name="unique_adversaire_per_equipe",
        ),
        migrations.AlterField(
            model_name="equipe",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="logos/"),
        ),
    ]
