# Generated by Django 4.2.7 on 2024-08-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=64)),
                ("rollNo", models.IntegerField()),
                ("marks", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("name", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=64)),
                ("subject", models.CharField(max_length=64)),
                ("salary", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
