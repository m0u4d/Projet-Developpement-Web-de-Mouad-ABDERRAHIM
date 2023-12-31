# Generated by Django 4.1.6 on 2023-11-14 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0005_remove_equipe_unique_adversaire_per_equipe_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipe",
            name="adversaire",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="playground.equipe",
            ),
        ),
        migrations.AddConstraint(
            model_name="equipe",
            constraint=models.UniqueConstraint(
                fields=("adversaire",), name="unique_adversaire_per_equipe"
            ),
        ),
    ]
