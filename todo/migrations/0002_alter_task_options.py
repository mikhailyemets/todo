# Generated by Django 5.0.6 on 2024-05-22 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_done"]},
        ),
    ]
