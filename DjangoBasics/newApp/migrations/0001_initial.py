# Generated by Django 5.1.4 on 2024-12-30 09:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChaiVariety",
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
                ("price", models.FloatField()),
                ("quantity", models.IntegerField()),
                ("image", models.ImageField(upload_to="images/")),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BL", "Black"),
                            ("GR", "Green"),
                            ("OO", "Oolong"),
                            ("WH", "White"),
                            ("HE", "Herbal"),
                            ("CH", "Chai"),
                        ],
                        default="CH",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
