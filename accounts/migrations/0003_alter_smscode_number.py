# Generated by Django 4.1.7 on 2023-04-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_smscode_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smscode',
            name='number',
            field=models.CharField(max_length=6),
        ),
    ]