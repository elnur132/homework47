# Generated by Django 4.2.7 on 2023-12-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customuser", "0006_alter_createuser_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="createuser",
            name="role",
            field=models.CharField(default="user", max_length=100),
        ),
    ]