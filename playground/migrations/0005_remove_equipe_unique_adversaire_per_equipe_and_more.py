# Generated by Django 4.1.6 on 2023-11-14 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0004_equipe_unique_adversaire_per_equipe"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="equipe",
            name="unique_adversaire_per_equipe",
        ),
        migrations.AlterField(
            model_name="equipe",
            name="adversaire",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="playground.equipe",
            ),
        ),
    ]
